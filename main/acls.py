import requests
from .keys import ABORTION_API_KEY
import json
from .models import AbortionData


def getAbortionData(state):
    headers = {"token": ABORTION_API_KEY}

    params = {
        "state_name": state,
    }

    url = "https://api.abortionpolicyapi.com/v1/gestational_limits/states/"

    response = requests.get(url, params=params, headers=headers)
    # content=response.json()
    content = json.loads(response.content)

    try:
        return {"policy": content[state]}
    except (KeyError, IndexError):
        return {"policy": None}
