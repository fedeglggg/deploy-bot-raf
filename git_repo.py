import git
import local_settings

mrs_to_show = 5

def get_merge_list() -> str:
    print("el repo es", local_settings.LOCAL_REPO)
    repo = git.Repo(local_settings.LOCAL_REPO)
    merge_commits = repo.iter_commits('HEAD', max_count=mrs_to_show, merges=True)
    # Extract and print the branch names from the merge commit messages
    merge_list = f"Showing the last {mrs_to_show} merge requests:" + '\n' + '\n'

    for commit in merge_commits:
        message = commit.message
        if "Merge branch" in message:
            branch_name = message.split("'")[1]
            merge_list = merge_list + "    " + branch_name + '\n'
    
    return merge_list


