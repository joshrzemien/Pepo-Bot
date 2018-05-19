import requests
import json
import logging

logger = logging.getLogger(__name__)

def fortniteTracker(nickname,platform):
    try:
        response = requests.get("https://api.fortnitetracker.com/v1/profile/{}/{}".format(platform,nickname), headers={"TRN-Api-Key":"c0d701f3-42a6-496e-a9f7-c814cb47c5ef"})
        json_data = json.loads(response.text)
        lfs = json_data.get("lifeTimeStats")
        responsedict = {item["key"]:item for item in lfs}
        mp = responsedict.get("Matches Played")["value"]
        w = responsedict.get("Wins")["value"]
        wp = responsedict.get("Win%")["value"]
        k = responsedict.get("Kills")["value"]
        kd = responsedict.get("K/d")["value"]
        response = """
        ====================================
    {} playing Fortnite on {} lifetime stats:               
    Matches Played: {}
    Wins: {} 
    Win %: {} 
    Kills: {} 
    K/D: {}
    ====================================
        """.format(nickname,platform,mp,w,wp,k,kd)
        return response
    except Exception:
        return "Invalid syntax or values. Please try again using format ?fortnitestats *nickname* *platform*"