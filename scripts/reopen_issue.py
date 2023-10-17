import requests
import sys
import json
import os

url = "https://api.github.com/graphql"

node_id = sys.argv[1]

query = """
mutation reopenIssue($input: ReopenIssueInput!) {
    reopenIssue(input: $input) {
        issue {
            id
        }
    }
}"""
variables = json.dumps({"input": {"issueId": node_id}})

payload = json.dumps({"query": query, "variables": variables})
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}]",
}

response = requests.request("POST", url, headers=headers, data=payload)
