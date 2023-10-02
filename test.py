import unittest
from git_repo import get_branches
from constants import ENV


def clean_testing_files():
    with open("last_branch_testing_backend.txt", "w") as file:
        file.write("")

    with open("last_branch_testing_frontend.txt", "w") as file:
        file.write("")


class MockAuthor:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class MockCommit:
    def __init__(self, commit_id, author_name, author_email, commit_message):
        self.commit_id = commit_id
        self.author = MockAuthor(author_name, author_email)
        self.message = commit_message


class TestMyApp(unittest.TestCase):
    def test_get_branches(self):
        mock_branches_frontend = ['feature/feature1',
                                  'fix/bug1',
                                  'docs/documentation1',
                                  'chore/cleanup1',
                                  'feature/feature2',
                                  'fix/bug2',
                                  'docs/documentation2',
                                  'chore/cleanup2',
                                  'feature/feature3',
                                  'fix/bug3',
                                  'docs/documentation3',
                                  'chore/cleanup3',
                                  'feature/feature4',
                                  'fix/bug4',
                                  'docs/documentation4']
        # Mock commits for frontend
        mock_commits_frontend = [
            MockCommit("Commit 1 ID", "Author 1 Name", "author1@example.com",
                       f"Merge branch '{mock_branches_frontend[0]}' into 'main'\n\nImplement feature 1\n\nSee merge request username/project!101"),
            MockCommit("Commit 2 ID", "Author 2 Name", "author2@example.com",
                       f"Merge branch '{mock_branches_frontend[1]}' into 'main'\n\nFix bug 1\n\nSee merge request username/project!102"),
            MockCommit("Commit 3 ID", "Author 3 Name", "author3@example.com",
                       f"Merge branch '{mock_branches_frontend[2]}' into 'main'\n\nUpdate documentation 1\n\nSee merge request username/project!103"),
            MockCommit("Commit 4 ID", "Author 4 Name", "author4@example.com",
                       f"Merge branch '{mock_branches_frontend[3]}' into 'main'\n\nCleanup code 1\n\nSee merge request username/project!104"),
            MockCommit("Commit 5 ID", "Author 5 Name", "author5@example.com",
                       f"Merge branch '{mock_branches_frontend[4]}' into 'main'\n\nImplement feature 2\n\nSee merge request username/project!105"),
            MockCommit("Commit 6 ID", "Author 6 Name", "author6@example.com",
                       f"Merge branch '{mock_branches_frontend[5]}' into 'main'\n\nFix bug 2\n\nSee merge request username/project!106"),
            MockCommit("Commit 7 ID", "Author 7 Name", "author7@example.com",
                       f"Merge branch '{mock_branches_frontend[6]}' into 'main'\n\nUpdate documentation 2\n\nSee merge request username/project!107"),
            MockCommit("Commit 8 ID", "Author 8 Name", "author8@example.com",
                       f"Merge branch '{mock_branches_frontend[7]}' into 'main'\n\nCleanup code 2\n\nSee merge request username/project!108"),
            MockCommit("Commit 9 ID", "Author 9 Name", "author9@example.com",
                       f"Merge branch '{mock_branches_frontend[8]}' into 'main'\n\nImplement feature 3\n\nSee merge request username/project!109"),
            MockCommit("Commit 10 ID", "Author 10 Name", "author10@example.com",
                       f"Merge branch '{mock_branches_frontend[9]}' into 'main'\n\nFix bug 3\n\nSee merge request username/project!110"),
            MockCommit("Commit 11 ID", "Author 11 Name", "author11@example.com",
                       f"Merge branch '{mock_branches_frontend[10]}' into 'main'\n\nUpdate documentation 3\n\nSee merge request username/project!111"),
            MockCommit("Commit 12 ID", "Author 12 Name", "author12@example.com",
                       f"Merge branch '{mock_branches_frontend[11]}' into 'main'\n\nCleanup code 3\n\nSee merge request username/project!112"),
            MockCommit("Commit 13 ID", "Author 13 Name", "author13@example.com",
                       f"Merge branch '{mock_branches_frontend[12]}' into 'main'\n\nImplement feature 4\n\nSee merge request username/project!113"),
            MockCommit("Commit 14 ID", "Author 14 Name", "author14@example.com",
                       f"Merge branch '{mock_branches_frontend[13]}' into 'main'\n\nFix bug 4\n\nSee merge request username/project!114"),
            MockCommit("Commit 15 ID", "Author 15 Name", "author15@example.com",
                       f"Merge branch '{mock_branches_frontend[14]}' into 'main'\n\nUpdate documentation 4\n\nSee merge request username/project!115"),
        ]

        mock_branches_backend = [
            'chore/cleanup4',
            'feature/feature5',
            'fix/bug5',
            'docs/documentation5',
            'chore/cleanup5',
            'feature/feature6',
            'fix/bug6',
            'docs/documentation6',
            'chore/cleanup6',
            'feature/feature7',
            'fix/bug7',
            'docs/documentation7',
            'chore/cleanup7',
            'feature/feature8',
            'fix/bug8'
        ]
        # Mock commits for backend
        mock_commits_backend = [
            MockCommit("Commit 16 ID", "Author 16 Name", "author16@example.com",
                       f"Merge branch '{mock_branches_backend[0]}' into 'main'\n\nCleanup code 4\n\nSee merge request username/project!116"),
            MockCommit("Commit 17 ID", "Author 17 Name", "author17@example.com",
                       f"Merge branch '{mock_branches_backend[1]}' into 'main'\n\nImplement feature 5\n\nSee merge request username/project!117"),
            MockCommit("Commit 18 ID", "Author 18 Name", "author18@example.com",
                       f"Merge branch '{mock_branches_backend[2]}' into 'main'\n\nFix bug 5\n\nSee merge request username/project!118"),
            MockCommit("Commit 19 ID", "Author 19 Name", "author19@example.com",
                       f"Merge branch '{mock_branches_backend[3]}' into 'main'\n\nUpdate documentation 5\n\nSee merge request username/project!119"),
            MockCommit("Commit 20 ID", "Author 20 Name", "author20@example.com",
                       f"Merge branch '{mock_branches_backend[4]}' into 'main'\n\nCleanup code 5\n\nSee merge request username/project!120"),
            MockCommit("Commit 21 ID", "Author 21 Name", "author21@example.com",
                       f"Merge branch '{mock_branches_backend[5]}' into 'main'\n\nImplement feature 6\n\nSee merge request username/project!121"),
            MockCommit("Commit 22 ID", "Author 22 Name", "author22@example.com",
                       f"Merge branch '{mock_branches_backend[6]}' into 'main'\n\nFix bug 6\n\nSee merge request username/project!122"),
            MockCommit("Commit 23 ID", "Author 23 Name", "author23@example.com",
                       f"Merge branch '{mock_branches_backend[7]}' into 'main'\n\nUpdate documentation 6\n\nSee merge request username/project!123"),
            MockCommit("Commit 24 ID", "Author 24 Name", "author24@example.com",
                       f"Merge branch '{mock_branches_backend[8]}' into 'main'\n\nCleanup code 6\n\nSee merge request username/project!124"),
            MockCommit("Commit 25 ID", "Author 25 Name", "author25@example.com",
                       f"Merge branch '{mock_branches_backend[9]}' into 'main'\n\nImplement feature 7\n\nSee merge request username/project!125"),
            MockCommit("Commit 26 ID", "Author 26 Name", "author26@example.com",
                       f"Merge branch '{mock_branches_backend[10]}' into 'main'\n\nFix bug 7\n\nSee merge request username/project!126"),
            MockCommit("Commit 27 ID", "Author 27 Name", "author27@example.com",
                       f"Merge branch '{mock_branches_backend[11]}' into 'main'\n\nUpdate documentation 7\n\nSee merge request username/project!127"),
            MockCommit("Commit 28 ID", "Author 28 Name", "author28@example.com",
                       f"Merge branch '{mock_branches_backend[12]}' into 'main'\n\nCleanup code 7\n\nSee merge request username/project!128"),
            MockCommit("Commit 29 ID", "Author 29 Name", "author29@example.com",
                       f"Merge branch '{mock_branches_backend[13]}' into 'main'\n\nImplement feature 8\n\nSee merge request username/project!129"),
            MockCommit("Commit 30 ID", "Author 30 Name", "author30@example.com",
                       f"Merge branch '{mock_branches_backend[14]}' into 'main'\n\nImplement feature 8\n\nSee merge request username/project!129")
        ]

        clean_testing_files()
        branches_frontend, branches_backend = get_branches(
            mock_commits_frontend, ENV.TESTING_FRONTEND, mock_commits_backend, ENV.TESTING_BACKEND)

        for i in range(0, len(branches_frontend)):
            self.assertEqual(branches_frontend[i], mock_branches_frontend[i])
            self.assertEqual(branches_backend[i], mock_branches_backend[i])

        mock_commits_frontend = []

        mock_branches_backend = ['chore/cleanup20', 'feature/feature66']
        mock_commits_backend = [
            MockCommit("Commit 31 ID", "Author 16 Name", "author16@example.com",
                       f"Merge branch '{mock_branches_backend[0]}' into 'main'\n\nCleanup code 4\n\nSee merge request username/project!116"),
            MockCommit("Commit 32 ID", "Author 17 Name", "author17@example.com",
                       f"Merge branch '{mock_branches_backend[1]}' into 'main'\n\nImplement feature 5\n\nSee merge request username/project!117"),
        ]

        branches_frontend, branches_backend = get_branches(
            mock_commits_frontend, ENV.TESTING_FRONTEND, mock_commits_backend, ENV.TESTING_BACKEND)

        self.assertEqual(len(branches_frontend), len(mock_commits_frontend))

        for i in range(len(branches_backend)):
            self.assertEqual(branches_backend[i], mock_branches_backend[i])


if __name__ == '__main__':
    unittest.main()
