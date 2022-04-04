import json
import requests

username = "Apperk274"
token = "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"
with open("issues.json", 'w') as json_file, open("issues_clean.json", "w") as clean_json_file:
    json_file.write("[")
    clean_json_file.write("[")
    for page in range(1, 5):
        currentArray = (
            requests.get(
                "https://api.github.com/repos/flutter/flutter/issues?per_page=100&labels=r%3A+duplicate&state=all&page=" + str(
                    page),
                auth=(username, token))).json()
        for currentObject in currentArray:
            comments = []
            for comment in requests.get(currentObject["comments_url"], auth=(username, token)).json():
                comments.append(comment["body"])
            cleanObject = {"id": currentObject["number"],
                           "title": currentObject["title"],
                           "body": currentObject["body"],
                           "comments": comments
                           }
            json.dump(cleanObject, clean_json_file, indent=4, separators=(',', ': '))
            clean_json_file.write(",\n")
            json.dump(currentObject, json_file, indent=4, separators=(',', ': '))
            json_file.write(",\n")

    json_file.write("]")
    clean_json_file.write("]")
