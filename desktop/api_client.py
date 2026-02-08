import requests

BASE_URL = "http://127.0.0.1:8000/api/"
TOKEN = None

def login(username, password):
    global TOKEN
    res = requests.post(BASE_URL + "token/", json={
        "username": username,
        "password": password
    })
    res.raise_for_status()
    TOKEN = res.json()["access"]

def upload_csv(file_path):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    files = {"file": open(file_path, "rb")}
    res = requests.post(BASE_URL + "upload/", headers=headers, files=files)
    res.raise_for_status()
    return res.json()
