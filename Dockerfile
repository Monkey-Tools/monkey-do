FROM python:3.9-slim 

# babanana
EXPOSE 8484 

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

#allow app to resolve imports
ENV PYTHONPATH=${PYTHONPATH}:/app/src

WORKDIR /app
COPY . /app

#install dependencies
RUN pip install pipenv
RUN pipenv install
RUN pipenv lock -r > requirements.txt
RUN python -m pip install -r requirements.txt

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8484", "src.app:app"]
