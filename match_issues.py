from distutils.command.clean import clean
import json
import requests
import re

username = "Apperk274"
token = "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"
urlRoot = "https://api.github.com/repos/flutter/flutter/issues/"

with open("issues_clean.json", 'r') as clean_json_file:
    data = json.load(clean_json_file)

with open("issues_final.json", "w") as final_json_file: 
    final_json_file.write("[")
    for currentObject in data:
        comments = currentObject['comments']
        for comment in comments: 
            finds = re.search('((?:https:\/\/github.com\/flutter\/flutter\/issues\/)(\d+))', comment)
            if(finds and int(finds.group(2)) > 0):
                print("link found", finds.group(2), comment)
                original = requests.get(urlRoot + finds.group(2), auth=(username, token)).json()
                currentObject['originalId'] = original["number"]
                currentObject['originalTitle'] = original["title"]
                currentObject['originalBody'] = original["body"]
                json.dump(currentObject, final_json_file, indent=4, separators=(',', ': '))
                final_json_file.write(",\n")
                break
            else:
                finds = re.search('((?:#)(\d+))', comment)
                if(finds and int(finds.group(2)) > 0):
                    print("number found", finds.group(2), comment)
                    original = requests.get(urlRoot + finds.group(2), auth=(username, token)).json()
                    currentObject['originalId'] = original["number"]
                    currentObject['originalTitle'] = original["title"]
                    currentObject['originalBody'] = original["body"]
                    json.dump(currentObject, final_json_file, indent=4, separators=(',', ': '))
                    final_json_file.write(",\n")
                    break
    final_json_file.write("]")   

clean_json_file.close()
final_json_file.close()  