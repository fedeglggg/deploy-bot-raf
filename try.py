import git
import local_settings

def get_status(branch_name):
    print("this is the task id", branch_name)
    frontend = git.Repo(local_settings.LOCAL_REPO_FRONT)

    try: 
        # No merge true para que tome todos
        commits_frontend = frontend.iter_commits(branch_name, max_count=1)
        found = next(commits_frontend, None) # ver como evitar que rompa para sacar try except
    except git.exc.GitCommandError:
        print("Commit not found")

get_status("2ce0c9795c240cb23f4370e428842ba9d99e59bb")