import requests
import json

def fortniteTracker(nickname,platform):
    response = requests.get("https://api.fortnitetracker.com/v1/profile/{}/{}".format(platform,nickname), headers={"TRN-Api-Key":"c0d701f3-42a6-496e-a9f7-c814cb47c5ef"})
    #return response.content
    #print(response.status_code)
    #print(response.content)
    json_data = json.loads(response.text)
    return json_data