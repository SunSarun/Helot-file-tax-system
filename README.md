# Helot-tax-filing-syste
Project is about a CRM system, Tax filing agency that is use to contact, manage, delivery consultant service ,information  to customer to help with filing tax to the government as a service.\
[Track-Project](https://warp-mat-baa.notion.site/Dashboard-40c6e77623a1804d84f7c9c42428a860?source=copy_link)
## Tech-Stack
1. Frontend: [React.ts](https://react.dev/)
2. Backend: [Python](https://www.python.org/downloads/), [Flask](https://flask.palletsprojects.com/en/stable/)
3. Database: [PostgreSQL](https://flask.palletsprojects.com/en/stable/)
## Build
#### 1. Docker
You need have docker and docker compose installed.\
**Build using docker compose**
```
docker compose build
```
**Or build and run**
```
docker compose up --build
```
#### 2. Server
You need [python3](https://www.python.org/downloads/) to create python env and install dependencies by follow the command below.
**move to core-system directory**
```
cd core-system
```
**Mac/Linux**
```
python3 -m venv .venv
source .venv/bin/activate
```
Then install dependencies using the command below.
```
pip install -r requirements.txt
```
To run the server use the command below.
```
python app.py
```
Or
``` 
flask run --debug
```
#### 3. UI
You need [npm](https://nodejs.org/en/download) and install denpendencies to build UI by follow command below.
**Install dependencies**
```
npm install
```
**Build**
```
npm run build
```
#### 4. Database
## Setup
