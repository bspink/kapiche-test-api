# Kapiche Test API

Returns NPS data to use for the Kapiche Test Webapp.

Developed using Python 3.7.0

Exposes an endpoint on http://localhost:5000/nps to return NPS score data.

To use in conjunction with [kapiche-test-webapp](https://github.com/bspink/kapiche-test-webapp) - run this API server first, alongside the webapp server.

# Run me

Run locally:
```bash
# Ideally installed into a virtualenv
pip install -e .
# Runs a flask development server on port 5000
FLASK_APP=kapiche_api/app.py flask run
```

Build and run via docker locally (starts a uwsgi http server for the flask app):
```bash
docker build -f Dockerfile -t kapiche/kapiche-api
# This will run in the background on localhost:5000
docker run -d -it -p 5000:5000 --rm --name kapiche-api kapiche/kapiche-api
```

Or, run from the quay.io image:
```bash
# This will run in the background on localhost:5000
docker run -d -it -p 5000:5000 --rm --name kapiche-api quay.io/bspink/kapiche-api
```

To stop me:
```bash
docker stop kapiche-api
```
