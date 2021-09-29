import requests
import json


with open("conf.json") as file:
    config = json.load(file)
    hub_url = f"https://api.github.com/repos/{config['hub_user']}/{config['hub_repo']}/issues"
    print(f"GET : {hub_url}")
    x = requests.get(hub_url)
    print("Answer : ", x.text)
    issues = x.json()

    for issue in issues:
        if issue["closed_at"] != "null":
            data={
                "title": "[Gihub] " + issue["title"],
                "description": "From : " + issue["html_url"] +"<br />" + issue["body"],
                "author":{ # TODO : not working ...
                    "id": issue["user"]["id"],
                    "name": issue["user"]["login"],
                },
            }
            lab_url = f"https://gitlab.com/api/v4/projects/{config['project_id']}/issues"
            print(f"POST :{lab_url}")
            x = requests.post(lab_url, data=data, headers={'PRIVATE-TOKEN': config["token"]})
            print(issue["title"], x.text)
