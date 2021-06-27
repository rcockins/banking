from github import Github

print("Hello World!")

g = Github(" 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")


for repo in g.get_user().get_repos():
    print(repo.name)