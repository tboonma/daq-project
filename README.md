# KU Travel

## About the Project

### Overview

This project is part of Data Acquisition and Integration 2022. You can find the bus number to take you from A to B, and also monitor population density for each KU Talai bus stop. We also have weather condition for each bus stop too.

### Features

1. See weather statistic for each Talai bus stop in KU.
2. See population density for each Talai bus stop in KU.
3. See PM2.5 for each Talai bus stop in KU.
4. See which bus number user can take from Talai bus stop to another Talai bus stop.
5. GraphQL can be accessed via [`/graphql`](https://ku-travel.tawanb.dev/graphql)
6. Swagger document can be accessed via [`/talai-api/v1/ui`](https://ku-travel.tawanb.dev/talai-api/v1/ui/)

### Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NPM](https://img.shields.io/badge/NPM-%23000000.svg?style=for-the-badge&logo=npm&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![GraphQL](https://img.shields.io/badge/-GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)

## Collaborators

| Name                      | Student ID | Major                                                    |
| ------------------------- | ---------- | -------------------------------------------------------- |
| Tawan BOONMA              | 6310545272 | Software and Knowledge Engineering, Kasetsart University |
| Krittamate CHERDPONGTAGIT | 6310545884 | Software and Knowledge Engineering, Kasetsart University |

## Getting Started

### Prerequisites

| Name   | Version      |
| ------ | ------------ |
| npm    | any          |
| Python | 3.9 or later |

### Installation

1. Initialize database from [Initial.sql](initial.sql)
2. Create an `.env` file from [example.env](example.env)
3. Generate new server stub and graphql document

```
npm i
npm run gen-server
npm run gen-graphql
```

4. Install all dependencies

```
pip install -r requirements.txt
```

6. Build React as static

```
cd clientside
npm i
npm run build
```

5. Run project locally (execute at the root of repository)

```
cd ..
python app.py
```

### Add an endpoint

1. Write endpoint info on [talai-api.yaml](openapi/talai-api.yaml)
2. Generate new server stub
3. Create function in [controller.py](controller.py) based on swagger operation id.
