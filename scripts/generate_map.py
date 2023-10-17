import json

from utils import get_all_issues
from geojson import Feature, Point, FeatureCollection

output = FeatureCollection([])

for issue in get_all_issues(state="closed"):
    obj = json.loads(issue.body)
    if not obj["location"]:
        continue
    feature = Feature(
        geometry=Point(obj["location"]),
        properties={
            "title": obj["address"],
            "description": f'<a href="{obj["original_url"]}">Original Link</a>',
            "marker-symbol": "marker",
        },
    )
    output.features.append(feature)

with open("map.json", "w") as fp:
    fp.write(json.dumps(output, ensure_ascii=False, indent=2))
