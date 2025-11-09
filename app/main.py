from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

MICROSERVICE_LINK = "https://appbox.qatar.cmu.edu/313-teams/team_name/"

@app.get("/team_info/{team_id}")
def get_team_info(team_id: str):

    if team_id is None:
        raise HTTPException(status_code=404, detail="Missing team id")

    team_id = team_id.lower()

    response = requests.get(MICROSERVICE_LINK + team_id)
    # You can check out what the response body looks like in the terminal using the print statement
    data = response.json()
    print(data)

    team_name = data["team_name"]

    # TODO Fix this to return correct values for correct team ids.
    if team_id == "1":
        return {
            "team_id" : 1,
            "team_name": "nodegpt",
            "mentor": "Seckhen"
        }
    elif team_id == "2":
        return {
            "team_id" : 2,
            "team_name": "bitwise",
            "mentor": "Aadi"
        }
    elif team_id == "3":
        return {
            "team_id" : 3,
            "team_name": "gituardo",
            "mentor": "Steve"
        }
    elif team_id == "4":
        return {
            "team_id" : 4,
            "team_name": "sick fault",
            "mentor": "Seckhen"
        }
    elif team_id == "5":
        return {
            "team_id" : 5,
            "team_name": "Debug Divas",
            "mentor": "Aadi"
        }
    elif team_id == "6":
        return {
            "team_id" : 6,
            "team_name": "Codex",
            "mentor": "Steve"
        }
    else:
        raise HTTPException(status_code=404, detail="Invalid team id")
