import os


class Constanst:
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    GITHUB_USER = os.environ.get("GITHUB_USER", "eclipse-set-bot")
    GITHUB_USER_EMAIL = os.environ.get("GITHUB_USER_EMAIL", "set-bot@eclipse.org")
    GITHUB_API_URL = "https://api.github.com/repos"

    SET_REPO = "eclipse-set/set"
    PPT_Test_ALL_JOB_API_URL = "https://vl-jenkins-ctl.ki.lan/job/PlanPro/job/PPTTest"

    TABLE_REFERENCE_ARTIFACT_NAME_PATTERN = "table-csv-{}"
    BUILD_SET_WORK_FLOW_ID = 63604658
    # BUILD_SET_WORK_FLOW_ID = 64995101
    SET_REMOTE_URL = "https://github.com/eclipse-set/set.git"
    SET_LOCA_REPO_PATH = "./set"
    SET_TABLE_REFERENCE_PATH = (
        "java/bundles/org.eclipse.set.swtbot/test_res/table_reference"
    )


CONSTANT = Constanst()
