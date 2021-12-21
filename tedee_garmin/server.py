from fastapi import FastAPI
import requests
import os

lock_app = FastAPI()
personal_key = os.getenv("PKEY")


@lock_app.get("/device")
def get_device_info():
    print("Getting device information...")
    response = requests.get("https://api.tedee.com/api/v1.22/my/device",
                headers={"accept": "application/json",
                         "Authorization": personal_key
                         }
                )
    print(response.text)

@lock_app.post("/open")
def open_lock():
    print("Opening lock...")
    response = requests.post("https://api.tedee.com/api/v1.22/my/lock/17393/operation/unlock",
                headers={"accept": "application/json",
                         "Content-Type": "application/json-patch+json",
                         "Authorization": personal_key
                         },
                params={}
                )
    print(response.text)

@lock_app.post("/close")
def close_lock():
    print("Closing lock...")
    response = requests.post("https://api.tedee.com/api/v1.22/my/lock/17393/operation/lock",
                headers={"accept": "application/json",
                         "Content-Type": "application/json-patch+json",
                         "Authorization": personal_key
                         },
                params={}
                )
    print(response.text)

