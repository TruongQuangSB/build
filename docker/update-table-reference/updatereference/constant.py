import os


class Constanst:
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    GITHUB_USER = os.environ.get("GITHUB_USER")
    GITHUB_API_URL = "https://api.github.com/repos"

    SET_REPO = "truongquangsb/set"

    TABLE_REFERENCE_ARTIFACT_NAME_PATTERN = "table-csv-{}"
    # BUILD_SET_WORK_FLOW_ID = 63604658
    BUILD_SET_WORK_FLOW_ID = 64995101
    SET_REMOTE_URL = f"https://{GITHUB_TOKEN}@github.com/truongquangsb/set.git"
    SET_LOCA_REPO_PATH = "./set"
    SET_TABLE_REFERENCE_PATH = (
        "java/bundles/org.eclipse.set.swtbot/test_res/table_reference"
    )


CONSTANT = Constanst()
