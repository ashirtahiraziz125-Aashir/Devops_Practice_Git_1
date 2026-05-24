import subprocess
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Linux Command Executor API")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/system/uptime")
def get_uptime():
    try:
        output = subprocess.check_output(["uptime"], text=True)
        return {"command": "uptime", "output": output.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/system/disk")
def get_disk_space():
    try:
        output = subprocess.check_output(["df", "-h"], text=True)
        return {"command": "df -h", "output": output.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/system/memory")
def get_memory():
    try:
        output = subprocess.check_output(["free", "-m"], text=True)
        return {"command": "free -m", "output": output.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/system/user")
def get_user():
    try:
        output = subprocess.check_output(["whoami"], text=True)
        return {"command": "whoami", "output": output.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))