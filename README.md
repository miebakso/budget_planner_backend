# Personal Web Backend

This is a personal backend application for different purposes:
1. Track income and expenditure
2. Coming soon

## Table of Content

- [installation](#installation)
- [Directory & File](#dir_file)

## Instalation <a name="installation"></a>

### Setup FastApi

1. Download or use the following command   
`git clone https://github.com/miebakso/personal_web_backend.git`
2. Install libraries and dependecies  
`pip install -r requirements.txt`
3. Setup database

### Database Setup

1. Install MariaDB. You can used other DB by altering the `config.py` and `dependencies.py`
`sudo apt install mariadb-server`. Install necessary dependencies needed.   
[Mariadb Installation Guide](https://mariadb.com/kb/en/getting-installing-and-upgrading-mariadb/)
2. Create User and Database for Application
3. create `.env` file to store all the settings and the file should be in the same dir as `config.py` `main.py`

```
PROJECT_NAME="App Name"
PROJECT_VERSION="1.0.0"
DB_NAME="SAME DB NAME AS YOU HAVE DEFINE IN STEP 2"
DB_USERNAME="db_username"
DB_PASSWORD="db_password"
DB_ADDRESS="localhost"
```

### Run Fast Api

1. uvicorn app.main:app --reload

2. go to `http://127.0.0.1:8000/docs` to view all the APIS

3. If error occurs, stop the program, pray, start again and hope it work the 2nd time.

## Directory & File <a name="dir_file"></a>

Coming soon

## Data <a name="custom_anchor_name"></a>