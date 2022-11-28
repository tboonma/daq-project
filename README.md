# KU Talai weather

## About the Project

This project is part of Data Acquisition and Integration 2022. You can find the bus number to take you from A to B, and also monitor population density for each KU Talai bus stop. We also have weather condition for each bus stop too.

### Built With

## Getting Started

### Prerequisites

| Name   | Version |
| ------ | ------- |
| npm    | any     |
| Python | 3.9     |

### Installation

1. Clone the repository and use Python virtual environment.
2. Create an `.env` file from [example.env](example.env)
3. Generate new server stub
```
npm run gen-server
```
4. Install all dependencies

```
pip install -r requirements.txt
npm i
```

5. Run project locally

```
npm start
```

### Add an endpoint
1. Write endpoint info on [talai-api.yaml](openapi/talai-api.yaml)
2. Generate new server stub
3. Create function in [controller.py](controller.py) based on swagger operation id.