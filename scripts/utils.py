from github import Github

github = Github()

repo = github.get_repo("TheodoreKrypton/jp-homes-page")


def get_issue(id: int):
    return repo.get_issue(id)


def get_all_issues(*args, **kwargs):
    return repo.get_issues(*args, **kwargs)
