FROM python:3.12
# EXPOSE 5000

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev --system

WORKDIR /app
COPY . .
# CMD ["flask", "run", "--host", "0.0.0.0"]
CMD ["/bin/bash", "docker-entrypoint.sh"]