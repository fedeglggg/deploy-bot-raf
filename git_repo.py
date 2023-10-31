import git
import local_settings
from constants import ENV


def get_last_branch(env):
    try:
        with open(f"last_branch_{env}.txt", "r") as file:
            last_branch = file.read().strip()
    except FileNotFoundError:
        last_branch = None
    return last_branch


def write_last_branch(merged_branches, env):
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

    write_last_branch(merged_branches, env)

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


def get_branches(commits_frontend, frontend_env, commits_backend, backend_env) -> str:

    branches_frontend = get_merged_branches_list(
        commits_frontend, frontend_env)
    branches_backend = get_merged_branches_list(commits_backend, backend_env)

    return branches_frontend, branches_backend


def get_deploy_report(commits_max_count=15) -> str:
    frontend = git.Repo(local_settings.LOCAL_REPO_FRONT)
    backend = git.Repo(local_settings.LOCAL_REPO_BACK)

    commits_frontend = frontend.iter_commits(
        'HEAD', max_count=commits_max_count, merges=True)

    commits_backend = backend.iter_commits(
        'HEAD', max_count=commits_max_count, merges=True)

    branches_frontend, branches_backend = get_branches(
        commits_frontend, ENV.FRONTEND, commits_backend, ENV.BACKEND)

    deploy_report = fill_report_by_env(ENV.FRONTEND, branches_frontend)
    deploy_report = fill_report_by_env(
        ENV.BACKEND, branches_backend, deploy_report)

    return deploy_report

def get_status(rev) -> str:
    frontend = git.Repo(local_settings.LOCAL_REPO_FRONT)
    backend = git.Repo(local_settings.LOCAL_REPO_BACK)  
    found = False
    not_found_msj = f"'{rev}' does not exist in any of the repositories."

    try: 
        # No merge true para que tome todos
        commits_frontend = frontend.iter_commits(rev, max_count=1)
        found = next(commits_frontend, False) # ver como evitar que rompa para sacar try except
        
        if not found:
            commits_backend = backend.iter_commits(rev, max_count=1)
            found = next(commits_backend, False)
        
    except git.exc.GitCommandError as e:
        return not_found_msj
    
    if found:
        return "The commit does exist in the remote repo" + '\n' + '\n' + found.message
    else:
        return not_found_msj
    