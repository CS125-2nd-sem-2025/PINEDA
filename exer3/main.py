from fastapi import FastAPI, Request
import platform

app = FastAPI()

@app.get("/")
def welcome_user():
    return {"Welcome": "User!"}

@app.get("/os")
def get_os():
    os_info = platform.system()
    return {"os": os_info}

@app.get("/version")
def get_version():
    version_info = platform.version()
    return {"version": version_info}

@app.get("/ip")
def get_ip(request: Request):
    client_ip = request.client.host
    return {"ip": client_ip}

@app.get("/all")
def get_all_info(request: Request):
    os_info = platform.system()
    version_info = platform.version()
    client_ip = request.client.host
    return {
        "os": os_info,
        "version": version_info,
        "ip": client_ip
    }
