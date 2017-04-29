"""Entry point for the server application."""

import logging
import traceback
from flask import jsonify
from gevent.wsgi import WSGIServer
from .models import *
from .factory import create_app
from flask import request

logger = logging.getLogger(__name__)
app = create_app()

@app.route('/api/analytics/get-college-list', methods=['POST'])
def collegesPerYear():
    form = request.json
    print(form)
    result = getCollegesPerYear(str(form["satVerbal"]), str(form["satMath"]), str(form["satWriting"]))
    return jsonify(result)


def main():
    """Main entry point of the app."""
    try:
        http_server = WSGIServer(('0.0.0.0', 8080),
                                 app,
                                 log=logging,
                                 error_log=logging)

        http_server.serve_forever()
    except Exception as exc:
        logger.error(exc.message)
        logger.exception(traceback.format_exc())
    finally:
        # get last entry and insert build appended if not completed
        # Do something here
        pass
