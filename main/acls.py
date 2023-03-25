import requests
from .keys import ABORTION_API_KEY
import json

def getAbortionData(state):
    headers = {"Authorization": ABORTION_API_KEY}
    params = {
        "per_page": 1,
        "query":state,
    }

    url = "https://api.abortionpolicyapi.com/v1/waiting_periods/"

    response = requests.get(url, params=params, headers=headers)
    content = json.loads(response.content)
    try:
        return {"Abortion_Data": content["photos"][0]["src"]["original"]}
    except (KeyError, IndexError):
        return {"picture_url": None}
