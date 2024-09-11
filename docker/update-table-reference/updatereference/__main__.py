import argparse
from updatereference.github_api_request import get_artifact, get_head_branch_name
from updatereference.constant import CONSTANT
import os
from git import Repo
import shutil
import stat
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prNumber", required=True, type=str)
    pr_number = str(parser.parse_args().prNumber)
    if not pr_number or not pr_number.isnumeric():
        raise SystemError("Invalid pull request number")
    branch_name = get_head_branch_name(pr_number)
    new_reference_zip = get_artifact(
        pr_number, CONSTANT.TABLE_REFERENCE_ARTIFACT_NAME_PATTERN
    )
    if not new_reference_zip:
        raise SystemError("Can't download the new reference artifact")
    apply_changes(branch_name, new_reference_zip)
    shutil.rmtree(CONSTANT.SET_LOCA_REPO_PATH, onexc=on_remove_error_hanlde)


def apply_changes(branch_name: str, download_url: str):
    set_repo = checkout_branch(
        CONSTANT.SET_REMOTE_URL, CONSTANT.SET_LOCA_REPO_PATH, branch_name
    )
    update_table_reference(download_url)
    if set_repo.is_dirty(untracked_files=True):
        set_repo.git.add(A=True)
        set_repo.index.commit(f"{branch_name} update table reference")
        set_repo.remote().push()
        print(f"{branch_name} update table reference")


def update_table_reference(new_reference_zip):
    table_reference_path = (
        f"{CONSTANT.SET_LOCA_REPO_PATH}/{CONSTANT.SET_TABLE_REFERENCE_PATH}"
    )
    try:
        buffer = BytesIO()
        with ZipFile(buffer, "w") as new_zip:
            with ZipFile(new_reference_zip) as zip_file:
                for zip_content in zip_file.filelist:
                    if zip_content.filename.endswith("current.csv"):
                        new_zip.writestr(
                            zip_content.filename.replace(
                                "current.csv", "reference.csv"
                            ),
                            zip_file.read(zip_content.filename),
                        )
                for new_zip_content in new_zip.filelist:
                    if os.path.exists(
                        f"{table_reference_path}/{new_zip_content.filename}"
                    ):
                        new_zip.extract(new_zip_content, table_reference_path)
    except:
        raise SystemError()


def checkout_branch(remote: str, local_repo_path: str, branch_name: str):
    result_repo = None
    print(f"Repo path: {local_repo_path}")
    # When the repository is already create/clone, then check if this repo have correct remote
    if os.path.exists(local_repo_path):
        print("Exist local repo")
        result_repo = Repo(local_repo_path)
        print("Current repo remote: " + result_repo.remote().url)
        if result_repo.remote().url != remote:
            print("Diffrence remote repo")
            shutil.rmtree(local_repo_path, onexc=on_remove_error_hanlde)
            result_repo = None

    if result_repo == None:
        print(f"Clone {remote}")
        result_repo = Repo.clone_from(remote, local_repo_path)
    if result_repo == None:
        raise SystemError
    result_repo.remotes.origin.pull()
    result_repo.git.checkout(branch_name)
    print(result_repo.git.status())
    return result_repo


def on_remove_error_hanlde(func, path, exc_info):
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IRWXU | stat.S_IWUSR)
        func(path)
    else:
        raise


main()
