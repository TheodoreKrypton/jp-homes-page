import sys
import os
import json

from utils import get_issue

issue_id = sys.argv[1]
issue = get_issue(int(issue_id))

date = issue.created_at.strftime("%Y-%m-%d")

obj = json.loads(issue.body)

file_path = f"_posts/{date}-{obj['address']}.md"

if os.path.exists(file_path):
    os.remove(file_path)
