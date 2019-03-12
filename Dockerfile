FROM python:3.6
WORKDIR /usr/src/app
COPY . .
EXPOSE 5001
RUN pip install pipenv
RUN pipenv install --skip-lock
ENTRYPOINT ["pipenv", "run", "python", "api.py"]
