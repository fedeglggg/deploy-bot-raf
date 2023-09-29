import git
import local_settings

max_mrs_to_show = 15


def get_new_list_commits(commits, env):
    try:
        with open(f"target_commit_{env}.txt", "r") as file:
            target_commit = file.read().strip()
    except FileNotFoundError:
        target_commit = None

    result = []
    for commit in commits:

        branch_name = commit.message.split("'")[1]
        if branch_name == target_commit:
            break
        else:
            result.append(branch_name)

    if result:
        with open(f"target_commit_{env}.txt", "w") as file:
            file.write(result[0])
            file.close()

    return result


def get_merge_list() -> str:
    merge_list = ""
    frontend = git.Repo(local_settings.LOCAL_REPO_FRONT)

    merge_commits_front = list(frontend.iter_commits(
        'HEAD', max_count=max_mrs_to_show, merges=True))
    branches_front = get_new_list_commits(
        merge_commits_front, "front")

    mr_amount = len(branches_front)
    if mr_amount > 0:
        merge_list = f"Showing {mr_amount} merge requests in frontend:" + '\n' + '\n'
    else:
        merge_list = f"There are no changes from the last deploy in the frontend." + '\n' + '\n'

    for branch in branches_front:
        merge_list = merge_list + "    " + branch + '\n'

    backend = git.Repo(local_settings.LOCAL_REPO_BACK)
    merge_commits_back = list(backend.iter_commits(
        'HEAD', max_count=max_mrs_to_show, merges=True))
    branches_back = get_new_list_commits(merge_commits_back, "back")

    mr_amount = len(branches_back)
    if mr_amount > 0:
        merge_list = merge_list + '\n' + \
            f"Showing {mr_amount} merge requests in backend: " + \
            '\n' + '\n'
    else:
        merge_list = merge_list + \
            f"There are no changes from the last deploy in the frontend." + '\n' + '\n'

    for branch in branches_back:
        merge_list = merge_list + "    " + branch + '\n'

    return merge_list
