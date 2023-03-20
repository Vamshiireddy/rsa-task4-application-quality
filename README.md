# Solution

## To run flask api

```bash
$ flask run
```

or using docker

```bash
$ docker build -t flask-app:latest .
$ docker run -p 5000:5000 flask-app:latest 
```

## To Test

```bash
$ curl http://localhost:5000/
$ curl http://localhost:5000/1
$ curl http://localhost:5000/100
$ curl http://localhost:5000/102
```

## Run unit test

```bash
$ docker run flask-app:latest python unit-test.py
```

## Run integration test

```bash
$ docker run flask-app:latest python integration-test.py
```