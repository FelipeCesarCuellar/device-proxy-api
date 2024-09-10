import falcon
import logging

from exceptions import ClientException
from controllers.device import DeviceController

class DeviceResource():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def on_post(self, req, resp):
        self.logger.info("Processing device POST request")
        
        try:
            device_controller = DeviceController(req.context.db_session)
            device = device_controller.create_device(req.media)
        except ClientException as ex:
            resp.media  = ex.get()
            resp.status = ex.http_status()
            return

        resp.media  = device
        resp.status = falcon.HTTP_200