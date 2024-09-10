import falcon
import logging

class HealthcheckResource():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def on_get(self, req, resp, placeholder=""):
        self.logger.info("I'm Alive!")

        resp.media  = {
            "health": "OK"
        }
        resp.status = falcon.HTTP_200