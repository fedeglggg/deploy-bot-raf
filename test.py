from git_repo import get_merge_list, generate_deploy_report


class MockAuthor:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class MockCommit:
    def __init__(self, commit_id, author_name, author_email, commit_message):
        self.commit_id = commit_id
        self.author = MockAuthor(author_name, author_email)
        self.message = commit_message


# Create a list of mock commits
mock_commits_frontend = [
    MockCommit("Merge branch 'feature/new-feature' into 'main'\n\nAdd new feature\n\nSee merge request username/project!123"),
    MockCommit(
        "Merge branch 'fix/bug-fix' into 'main'\n\nFix a critical bug\n\nSee merge request username/project!124"),
    MockCommit("Merge branch 'docs/documentation' into 'main'\n\nUpdate documentation\n\nSee merge request username/project!125"),
    MockCommit(
        "Merge branch 'chore/cleanup' into 'main'\n\nCleanup code\n\nSee merge request username/project!126"),
    MockCommit("Merge branch 'feature/another-feature' into 'main'\n\nImplement another feature\n\nSee merge request username/project!127"),
    MockCommit("Merge branch 'fix/another-bug-fix' into 'main'\n\nFix another bug\n\nSee merge request username/project!128"),
    MockCommit("Merge branch 'docs/more-documentation' into 'main'\n\nAdd more documentation\n\nSee merge request username/project!129"),
    MockCommit(
        "Merge branch 'chore/optimization' into 'main'\n\nOptimize code\n\nSee merge request username/project!130"),
    MockCommit("Merge branch 'feature/yet-another-feature' into 'main'\n\nImplement yet another feature\n\nSee merge request username/project!131"),
    MockCommit("Merge branch 'fix/yet-another-bug-fix' into 'main'\n\nFix yet another bug\n\nSee merge request username/project!132"),
    MockCommit("Merge branch 'docs/even-more-documentation' into 'main'\n\nAdd even more documentation\n\nSee merge request username/project!133"),
    MockCommit(
        "Merge branch 'chore/refactoring' into 'main'\n\nRefactor code\n\nSee merge request username/project!134"),
    MockCommit("Merge branch 'feature/final-feature' into 'main'\n\nImplement final feature\n\nSee merge request username/project!135"),
    MockCommit(
        "Merge branch 'fix/final-bug-fix' into 'main'\n\nFix final bug\n\nSee merge request username/project!136"),
    MockCommit("Merge branch 'docs/final-documentation' into 'main'\n\nFinalize documentation\n\nSee merge request username/project!137"),
]
mock_commits_backend = [
    MockCommit(
        "Merge branch 'chore/final-cleanup' into 'main'\n\nFinal cleanup\n\nSee merge request username/project!138"),
    MockCommit("Merge branch 'feature/last-feature' into 'main'\n\nImplement last feature\n\nSee merge request username/project!139"),
    MockCommit(
        "Merge branch 'fix/last-bug-fix' into 'main'\n\nFix last bug\n\nSee merge request username/project!140"),
    MockCommit("Merge branch 'docs/last-documentation' into 'main'\n\nUpdate last documentation\n\nSee merge request username/project!141"),
    MockCommit("Merge branch 'chore/last-optimization' into 'main'\n\nOptimize one last time\n\nSee merge request username/project!142"),
    MockCommit("Merge branch 'feature/final-final-feature' into 'main'\n\nImplement the final, final feature\n\nSee merge request username/project!143"),
    MockCommit("Merge branch 'fix/final-final-bug-fix' into 'main'\n\nFix the final, final bug\n\nSee merge request username/project!144"),
    MockCommit("Merge branch 'docs/final-final-documentation' into 'main'\n\nUpdate the final, final documentation\n\nSee merge request username/project!145"),
    MockCommit("Merge branch 'chore/final-final-cleanup' into 'main'\n\nDo the final, final cleanup\n\nSee merge request username/project!146"),
    MockCommit("Merge branch 'feature/ultimate-feature' into 'main'\n\nImplement the ultimate feature\n\nSee merge request username/project!147"),
    MockCommit("Merge branch 'fix/ultimate-bug-fix' into 'main'\n\nFix the ultimate bug\n\nSee merge request username/project!148"),
    MockCommit("Merge branch 'docs/ultimate-documentation' into 'main'\n\nUpdate the ultimate documentation\n\nSee merge request username/project!149"),
    MockCommit("Merge branch 'chore/ultimate-optimization' into 'main'\n\nOptimize to the ultimate level\n\nSee merge request username/project!150"),
]

message_data = {
    {"content": "/deploy_report", "author_id": 277211883860262913, "channel": "general"}
}

deploy_report = generate_deploy_report(
    mock_commits_frontend, mock_commits_backend)


list = get_merge_list
print(list)
