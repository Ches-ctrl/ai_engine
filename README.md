# Overview
Multi-agent system for AI Engine Hack

# Technologies Used
Throughout these docs, Terminal commands are provided for Unix shells (i.e. MacOS, Linux).

## Frontend

## Backend
- Python 3.11
- Flask
- Pydantic
- pytest
<br><br>

# Running backend

## Setup
1. Check you have Python 3.11 installed, a specific version number should be returned in the Terminal (e.g. `Python 3.11.11`).
    ```bash
    python3.11 --version
    ```
<br>

2. Navigate to `backend` folder and create an `.env.local` file (copying `.env.example`).
    ```bash
    cd backend && cp .env.example .env.local
    ```
<br>

## Running backend locally
The backend can be run:
* within a virtual environment or a docker container
* in development or production mode

<br>

From the backend folder, there are 4 ways to run the backend:
| **environment** | **mode** | **command** |
|-----------------|----------|-------------|
| virtual env | dev | `./boot.sh venv dev` |
| virtual env | prod | `./boot.sh venv prod` |
| docker | dev | `./boot.sh docker dev` |
| docker | prod | `./boot.sh docker prod` |  

Backend served at [http://localhost:8080](http://localhost:8080) - only route available is 'Hello, World!' smoke test on index route (`/`).
<br><br>

# Testing

## Running backend tests
1. Set up backend following ([setup](#setup)) instructions above.
2. Once in `backend` folder, execute `./test.sh` from Terminal

    | **testing mode** |  **command** |
    |------------------|--------------|
    | running tests normally |  `./test.sh` |
    | running tests with coverage report |  `./test.sh coverage` |
    | running tests with detailed output |  `./test.sh verbose` |
<br><br>

# Deployment
## Requirements for running backend locally
* The following files are used for running the backend locally using a virtual environment (in `dev` or `prod` modes):
    * [boot.sh](/backend/boot.sh)
    * [config.py](/backend/config.py)
    * env files (`.env.local` / `.env.prod`)

* The following files are used for running the backend locally using a docker container (in `dev` and `prod` modes):
    * [config.py](/backend/config.py)
    * env files (`.env.local`, `.env.prod`)
    * docker compose files (dev: [docker-compose.yml](/backend/docker-compose.yml) / prod: [docker-compose.prod.yml](/backend/docker-compose.yml))
    * dockerfile ([Dockerfile.dev](/backend/Dockerfile.dev) / [Dockerfile.prod](/backend/Dockerfile.prod))

NOTE: [boot.sh](/backend/boot.sh) not required for running backend using docker, because we only use the `docker compose` commands at the very end of the file.
<br><br>