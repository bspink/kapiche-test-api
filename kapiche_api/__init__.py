import os
import logging
import csv
import collections
import werkzeug.exceptions
import datetime

from flask import Flask, jsonify
from flask_cors import CORS
from typing import Dict

from .nps import get_nps_data


logger = logging.getLogger(__name__)


def handle_exception(e):

    logger.exception(e)

    response_code = 500

    if isinstance(e, werkzeug.exceptions.HTTPException):
        # If the exception is a base HTTPException, then the code will be None
        # If this is the case, default to our default status code (500)
        response_code = e.code or response_code

    return jsonify({}), response_code


def create_app(config=None):

    app = Flask(__name__)
    CORS(app)
    app.add_url_rule('/nps', 'nps', get_nps_data)

    # Flask is annoying and requires us to explicitly list every HTTPException child
    # class that we wish to register an exception handler for.
    # So, until they get their act together, register the catch-all exception handler
    # for each of the werkzeug default_exceptions exceptions.
    # This is a mapping of http_code => http_exception_class
    for _, http_exception_class in werkzeug.exceptions.default_exceptions.items():
        app.register_error_handler(http_exception_class, handle_exception)

    app.register_error_handler(Exception, handle_exception)

    return app
