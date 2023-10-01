from git_repo import generate_deploy_report


class MockAuthor:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class MockCommit:
    def __init__(self, commit_id, author_name, author_email, commit_message):
        self.commit_id = commit_id
        self.author = MockAuthor(author_name, author_email)
        self.message = commit_message


# Mock commits for frontend
mock_commits_frontend = [
    MockCommit("Commit 1 ID", "Author 1 Name", "author1@example.com",
               "Merge branch 'feature/feature1' into 'main'\n\nImplement feature 1\n\nSee merge request username/project!101"),
    MockCommit("Commit 2 ID", "Author 2 Name", "author2@example.com",
               "Merge branch 'fix/bug1' into 'main'\n\nFix bug 1\n\nSee merge request username/project!102"),
    MockCommit("Commit 3 ID", "Author 3 Name", "author3@example.com",
               "Merge branch 'docs/documentation1' into 'main'\n\nUpdate documentation 1\n\nSee merge request username/project!103"),
    MockCommit("Commit 4 ID", "Author 4 Name", "author4@example.com",
               "Merge branch 'chore/cleanup1' into 'main'\n\nCleanup code 1\n\nSee merge request username/project!104"),
    MockCommit("Commit 5 ID", "Author 5 Name", "author5@example.com",
               "Merge branch 'feature/feature2' into 'main'\n\nImplement feature 2\n\nSee merge request username/project!105"),
    MockCommit("Commit 6 ID", "Author 6 Name", "author6@example.com",
               "Merge branch 'fix/bug2' into 'main'\n\nFix bug 2\n\nSee merge request username/project!106"),
    MockCommit("Commit 7 ID", "Author 7 Name", "author7@example.com",
               "Merge branch 'docs/documentation2' into 'main'\n\nUpdate documentation 2\n\nSee merge request username/project!107"),
    MockCommit("Commit 8 ID", "Author 8 Name", "author8@example.com",
               "Merge branch 'chore/cleanup2' into 'main'\n\nCleanup code 2\n\nSee merge request username/project!108"),
    MockCommit("Commit 9 ID", "Author 9 Name", "author9@example.com",
               "Merge branch 'feature/feature3' into 'main'\n\nImplement feature 3\n\nSee merge request username/project!109"),
    MockCommit("Commit 10 ID", "Author 10 Name", "author10@example.com",
               "Merge branch 'fix/bug3' into 'main'\n\nFix bug 3\n\nSee merge request username/project!110"),
    MockCommit("Commit 11 ID", "Author 11 Name", "author11@example.com",
               "Merge branch 'docs/documentation3' into 'main'\n\nUpdate documentation 3\n\nSee merge request username/project!111"),
    MockCommit("Commit 12 ID", "Author 12 Name", "author12@example.com",
               "Merge branch 'chore/cleanup3' into 'main'\n\nCleanup code 3\n\nSee merge request username/project!112"),
    MockCommit("Commit 13 ID", "Author 13 Name", "author13@example.com",
               "Merge branch 'feature/feature4' into 'main'\n\nImplement feature 4\n\nSee merge request username/project!113"),
    MockCommit("Commit 14 ID", "Author 14 Name", "author14@example.com",
               "Merge branch 'fix/bug4' into 'main'\n\nFix bug 4\n\nSee merge request username/project!114"),
    MockCommit("Commit 15 ID", "Author 15 Name", "author15@example.com",
               "Merge branch 'docs/documentation4' into 'main'\n\nUpdate documentation 4\n\nSee merge request username/project!115"),
]

# Mock commits for backend
mock_commits_backend = [
    MockCommit("Commit 16 ID", "Author 16 Name", "author16@example.com",
               "Merge branch 'chore/cleanup4' into 'main'\n\nCleanup code 4\n\nSee merge request username/project!116"),
    MockCommit("Commit 17 ID", "Author 17 Name", "author17@example.com",
               "Merge branch 'feature/feature5' into 'main'\n\nImplement feature 5\n\nSee merge request username/project!117"),
    MockCommit("Commit 18 ID", "Author 18 Name", "author18@example.com",
               "Merge branch 'fix/bug5' into 'main'\n\nFix bug 5\n\nSee merge request username/project!118"),
    MockCommit("Commit 19 ID", "Author 19 Name", "author19@example.com",
               "Merge branch 'docs/documentation5' into 'main'\n\nUpdate documentation 5\n\nSee merge request username/project!119"),
    MockCommit("Commit 20 ID", "Author 20 Name", "author20@example.com",
               "Merge branch 'chore/cleanup5' into 'main'\n\nCleanup code 5\n\nSee merge request username/project!120"),
    MockCommit("Commit 21 ID", "Author 21 Name", "author21@example.com",
               "Merge branch 'feature/feature6' into 'main'\n\nImplement feature 6\n\nSee merge request username/project!121"),
    MockCommit("Commit 22 ID", "Author 22 Name", "author22@example.com",
               "Merge branch 'fix/bug6' into 'main'\n\nFix bug 6\n\nSee merge request username/project!122"),
    MockCommit("Commit 23 ID", "Author 23 Name", "author23@example.com",
               "Merge branch 'docs/documentation6' into 'main'\n\nUpdate documentation 6\n\nSee merge request username/project!123"),
    MockCommit("Commit 24 ID", "Author 24 Name", "author24@example.com",
               "Merge branch 'chore/cleanup6' into 'main'\n\nCleanup code 6\n\nSee merge request username/project!124"),
    MockCommit("Commit 25 ID", "Author 25 Name", "author25@example.com",
               "Merge branch 'feature/feature7' into 'main'\n\nImplement feature 7\n\nSee merge request username/project!125"),
    MockCommit("Commit 26 ID", "Author 26 Name", "author26@example.com",
               "Merge branch 'fix/bug7' into 'main'\n\nFix bug 7\n\nSee merge request username/project!126"),
    MockCommit("Commit 27 ID", "Author 27 Name", "author27@example.com",
               "Merge branch 'docs/documentation7' into 'main'\n\nUpdate documentation 7\n\nSee merge request username/project!127"),
    MockCommit("Commit 28 ID", "Author 28 Name", "author28@example.com",
               "Merge branch 'chore/cleanup7' into 'main'\n\nCleanup code 7\n\nSee merge request username/project!128"),
    MockCommit("Commit 29 ID", "Author 29 Name", "author29@example.com",
               "Merge branch 'feature/feature8' into 'main'\n\nImplement feature 8\n\nSee merge request username/project!129"),
    MockCommit("Commit 30 ID", "Author 30 Name", "author30@example.com",
               "Merge branch 'fix/bug8' into 'main'\n\nImplement feature 8\n\nSee merge request username/project!129")
]
""" message_data = {
    {"content": "/deploy_report", "author_id": 277211883860262913, "channel": "general"}
} """


def clean_testing_files():
    with open("last_branch_testing_backend.txt", "w") as file:
        file.write("")

    with open("last_branch_testing_frontend.txt", "w") as file:
        file.write("")


clean_testing_files()
print("RESULT N°1: \n\n")
deploy_report = generate_deploy_report(
    mock_commits_frontend, mock_commits_backend, True)
print(deploy_report)

mock_commits_frontend = []

mock_commits_backend = [
    MockCommit("Commit 31 ID", "Author 16 Name", "author16@example.com",
               "Merge branch 'chore/cleanup20' into 'main'\n\nCleanup code 4\n\nSee merge request username/project!116"),
    MockCommit("Commit 32 ID", "Author 17 Name", "author17@example.com",
               "Merge branch 'feature/feature66' into 'main'\n\nImplement feature 5\n\nSee merge request username/project!117"),
]

print("RESULT N°1: \n\n")
deploy_report = generate_deploy_report(
    mock_commits_frontend, mock_commits_backend, True)
print(deploy_report)
