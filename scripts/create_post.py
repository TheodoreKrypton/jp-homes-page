import sys
import requests
import re
import json
import html

from utils import get_issue, get_telegraph_object

issue_id = sys.argv[1]
issue = get_issue(int(issue_id))

telegraph_post_link = issue.body
obj = get_telegraph_object(telegraph_post_link)

date = issue.created_at.strftime("%Y-%m-%d")

title = f'{date}: {obj["address"]}'


def get_image_id(url):
    return url.split("/")[-1].split(".")[0]


photos = obj["photos"]

for url in photos:
    data = requests.get(url).content
    img_id = get_image_id(url)
    with open(f"assets/images/{img_id}.jpg", "wb") as fp:
        fp.write(data)

with open(f"_posts/{date}-{obj['address']}.md", "w", encoding="utf-8") as fp:
    cover_image_id = get_image_id(photos[0])

    for comment in issue.get_comments():
        if comment.user.login == "kongicus":
            description = f"<p>{comment.body}</p>\n"
            break
    else:
        description = ""

    images = "\n".join(
        (
            f'<img src="/assets/images/{get_image_id(url)}.jpg" alt="alt_text"/>'
            for url in photos[1:]
        )
    )

    images = '<div class="scroll-container">' + images + "</div>"

    original_link = f'[Original Link]({obj["original_url"]})'

    city = obj["city"]

    featured = "false"

    for label in issue.get_labels():
        if label.name == "featured":
            featured = "true"
            break

    post = f"""
---
layout: post
title: "{title}"
categories: ["{city}"]
image: assets/images/{cover_image_id}.jpg
comments: false
featured: {featured}
---
{description}
* 价格: {obj['price']} JPY
* 户型: {obj['rooms']}
* 土地面积: {obj['land_area']}m²
* 建筑面积: {obj['floor_area']}m²
* 建造时间: {obj['completed_date']}
* 📍: [{obj['city']}](https://www.google.com/maps/search/?api=1&query={obj['location'][1]}%2C{obj['location'][0]})

{images}
{original_link}
  """.strip()

    fp.write(post)
