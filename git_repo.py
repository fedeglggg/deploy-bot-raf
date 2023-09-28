import git
import local_settings

mrs_to_show = 5


def get_merge_list() -> str:
    frontend = git.Repo(local_settings.LOCAL_REPO_FRONT)
    merge_commits_front = frontend.iter_commits(
        'HEAD', max_count=mrs_to_show, merges=True)
    merge_list = f"Showing the last {mrs_to_show} merge requests" + '\n' + '\n'

    merge_list = merge_list + f"Frontend:" + '\n' + '\n'

    for commit in merge_commits_front:
        message = commit.message
        if "Merge branch" in message:
            branch_name = message.split("'")[1]
            merge_list = merge_list + "    " + branch_name + '\n'

    backend = git.Repo(local_settings.LOCAL_REPO_BACK)
    merge_commits_back = backend.iter_commits(
        'HEAD', max_count=mrs_to_show, merges=True)
    merge_list = merge_list + '\n' f"Backend:" + '\n' + '\n'

    for commit in merge_commits_back:
        message = commit.message
        if "Merge branch" in message:
            branch_name = message.split("'")[1]
            merge_list = merge_list + "    " + branch_name + '\n'

    return merge_list
