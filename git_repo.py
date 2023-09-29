import git
import local_settings

MAX_COUNT = 15


def get_last_branch(env):
    try:
        with open(f"last_branch_{env}.txt", "r") as file:
            last_branch = file.read().strip()
    except FileNotFoundError:
        last_branch = None
    return last_branch


def write_last_branch(env, merged_branches):
    if merged_branches:
        with open(f"last_branch_{env}.txt", "w") as file:
            file.write(merged_branches[0])
            file.close()


def get_merged_branches_list(commits, env):
    last_branch = get_last_branch(env)
    merged_branches = []

    for commit in commits:
        branch_name = commit.message.split("'")[1]

        if branch_name != last_branch:
            merged_branches.append(branch_name)
        else:
            break

    write_last_branch(env, merged_branches)

    return merged_branches


def fill_report_by_env(env, branches, deploy_report=None):
    deploy_report = deploy_report if deploy_report != None else ""
    len_branches = len(branches)
    if len_branches == 0:
        return deploy_report + \
            f"There are no changes from the last deploy in the {env}." + '\n' + '\n'

    deploy_report = deploy_report + \
        f"Showing {len_branches} merge requests in {env}:" + '\n' + '\n'

    for branch in branches:
        deploy_report = deploy_report + "    " + branch + '\n'

    if branches:
        deploy_report = deploy_report + '\n' + '\n'

    return deploy_report


def get_deploy_report() -> str:

    frontend = git.Repo(local_settings.LOCAL_REPO_FRONT)
    backend = git.Repo(local_settings.LOCAL_REPO_BACK)

    commits_frontend = frontend.iter_commits(
        'HEAD', max_count=MAX_COUNT, merges=True)
    branches_frontend = get_merged_branches_list(commits_frontend, "frontend")

    commits_backend = backend.iter_commits(
        'HEAD', max_count=MAX_COUNT, merges=True)
    branches_backend = get_merged_branches_list(commits_backend, "backend")

    deploy_report = fill_report_by_env("frontend", branches_frontend)
    deploy_report = fill_report_by_env(
        "backend", branches_backend, deploy_report)

    return deploy_report
