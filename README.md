# Devops_Practice_Git_1
# Linux Command Executor API

This is a basic FastAPI application that executes predefined Linux system commands using Python's `subprocess` module and returns the output in JSON format.

## Features
- **Health Check:** Monitor API status.
- **System Information:** Fetch system uptime, disk space usage, memory info, and current user.
- **Security:** Strict restriction on custom user input to prevent command injection.

## API Endpoints
- `GET /health` - Check API health status
- `GET /system/uptime` - Execute `uptime` command
- `GET /system/disk` - Execute `df -h` command
- `GET /system/memory` - Execute `free -m` command
- `GET /system/user` - Execute `whoami` command

## Technologies Used
- Python 3
- FastAPI
- Uvicorn
- WSL (Ubuntu)
- Git & GitHub

## How to Run
1. Run the Uvicorn server:
   ```bash
   uvicorn main:app --reload