# Examples Machine Learning Services with Flask

This Repository contains simple examples of Machine Learning Services with Flask as REST API.

## Setup Environments

Before running the services, we need to setup environments that saved to `.env` file.

```bash
cp .env.example .env
```

Adjust the environments, then


## Run Services Manually 

Install dependencies

```bash
pipenv install --skip-lock
```

Run Flask APP

```bash
pipenv run python api.py
```

## or Run with Docker 

Build Docker Image
```bash
docker build -t repodevs/ml-service .
```

Run Containers
```bash
docker run -d --name ml-app -p 5001:5001 repodevs/ml-service
```

## Testing

Testing the Services

```bash
http POST http://0.0.0.0:5001/ml-titanic/v1/predict "Pclass:=[1]" 'Sex:=["male"]' "Age:=[32]" "SibSp:=[1]" "Parch:=[0]" "Fare:=[100]" 'Embarked:=["S"]' -v
```


