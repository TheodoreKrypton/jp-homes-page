from github import Github
import json
import requests
import re
import html

github = Github()

repo = github.get_repo("TheodoreKrypton/jp-homes-page")


def get_issue(id: int):
    return repo.get_issue(id)


def get_telegraph_object(link):
    rsp = requests.get(link)

    obj_matched = re.search(r"\<pre\>(.+?)\<\/pre\>", rsp.text)
    if not obj_matched:
        exit(0)

    obj_str = obj_matched.group(1)
    obj = json.loads(html.unescape(obj_str))
    return obj
