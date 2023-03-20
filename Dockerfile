FROM python:3.8
WORKDIR /app
ADD . .
RUN pip install flask
CMD ["flask", "--app", "api", "run", "--host", "0.0.0.0"]