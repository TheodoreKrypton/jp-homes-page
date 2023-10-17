from github import Github

github = Github()

repo = github.get_repo("TheodoreKrypton/jp-homes-page")


def get_issue(id: int):
    return repo.get_issue(id)
