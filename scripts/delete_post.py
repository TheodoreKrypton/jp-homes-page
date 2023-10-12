import sys
import os

from utils import get_issue, get_telegraph_object

issue_id = sys.argv[1]
issue = get_issue(int(issue_id))

telegraph_post_link = issue.body

date = issue.created_at.strftime("%Y-%m-%d")
obj = get_telegraph_object(telegraph_post_link)

file_path = f"_posts/{date}-{obj['address']}.md"

if os.path.exists(file_path):
    os.remove(file_path)
