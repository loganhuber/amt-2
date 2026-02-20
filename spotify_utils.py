import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
artist_id = '0PxamJCparlY9A6VeL3aZB'

def get_spotify_token():
    
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={"grant_type": "client_credentials"}
    )

    return response.json()["access_token"]

def get_artist_albums(artist_id):
    token = get_spotify_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"https://api.spotify.com/v1/artists/{artist_id}/albums",
        headers=headers
    )

    return response.json()