from github import Github

g = Github(" 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")


for repo in g.get_user().get_repos():
    try:
        print(repo)
    except(Github.GithubException):
        print(Github.GithubException.message)