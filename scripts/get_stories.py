import time

import requests

for story_type in ["stories", "stories-nested"]:
    for story in range(184, 315):
        print(f"[{story_type}] Getting story ID {story}...")
        url = (
            f"http://spendingstories.org/api/{story_type}/"
            + str(story)
            + "/?format=api"
        )
        r = requests.get(url)
        filepath = f"../api/{story_type}/" + str(story) + ".html"
        with open(filepath, "wb") as f:
            f.write(r.content)
        time.sleep(0.2)  # let's not be too aggressive with requests
