import logging

class SessionManager:
    def __init__(self, session_maker):
        self.db_session_maker = session_maker
        self.logger = logging.getLogger(__name__)
    
    def process_request(self, req, resp):
        self.logger.info('Processing incoming request')
        if req.method == 'OPTIONS':
            req.context.db_session = None
            return
        
        self.logger.info('Initializing DB Session')
        req.context.db_session = self.db_session_maker()

    def process_response(self, req, resp, resource, req_succeded):
        self.logger.info('Cleaning context')
        if req.method == 'OPTIONS':
            return
        
        if hasattr(req.context, 'db_session') and req.context.db_session is not None:
            if not req_succeded:
                self.logger.info("Rolling back due to request failure")
                req.context.db_session.rollback()
            self.logger.info("Closing DB connection")
            req.context.db_session.close()