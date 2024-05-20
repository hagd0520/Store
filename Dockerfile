FROM python:3.12
# EXPOSE 5000

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app
COPY . .
# CMD ["flask", "run", "--host", "0.0.0.0"]
CMD [ "gunicorn", "--bind", "0.0.0.0:80", "app:create_app()" ]