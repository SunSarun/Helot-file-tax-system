# Helot-tax-filing-syste
Project is about a CRM system, Tax filing agency that is use to contact, manage, delivery consultant service ,information  to customer to help with filing tax to the government as a service. 
## Tech-Stack
1. Frontend: React.ts
2. Backend: Python, Flask
3. Database: Postgressql
## Build
#### 1. Docker
You need have docker and docker compose installed.</br>
**Build using docker compose**
```
docker compose build
```
**Or build and run**
```
docker compose up --build
```
#### 2. Server
You need python3 to create python env and install dependencies by follow the command below.
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
You need npm and install denpendencies to build UI by follow command below.
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
