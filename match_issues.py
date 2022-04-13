import json
import requests
import re

username = "Apperk274"
token = "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"
urlRoot = "https://api.github.com/repos/flutter/flutter/issues/"

with open("issues_clean.json", 'r') as clean_json_file:
    data = json.load(clean_json_file)

with open("issues_final.json", "w") as final_json_file: 
    for i in range (5):
        comments = data[i]['comments']
        duplicates = []
        for comment in comments: 

            finds = re.search('((?:https:\/\/github.com\/flutter\/flutter\/issues\/)(\d+))', comment)
            if(finds):
                print(i, "link found", finds.group(2), comment)
                a = requests.get(urlRoot + finds.group(2), auth=(username, token)).json()
                print("link: ", urlRoot + finds.group(2))
                print('karsilik', a['title'])
                break
            else:
                finds = re.search('((?:#)(\d+))', comment)
                if(finds):
                    print(i, "number found", finds.group(2), comment)
                    break
            
finds = re.search('(?:#(\d+))|(https:\/\/github.com\/flutter\/flutter\/issues\/\d+)$', '#45655 https://github.com/flutter/flutter/issues/54565')
print("last finds", finds.group())
            