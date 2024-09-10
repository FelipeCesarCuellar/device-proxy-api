import falcon

class ClientException(BaseException):
    def __init__(self, title, description, status_code):
        self.title = title
        self.description = description
        self.status_code = status_code
    
    def get(self):
        return {"title": self.title, "description": self.description}
    
    def http_status(self):
        return self.status_code
    
class ConflictException(ClientException):
    def __init__(self, title, description):
        super().__init__(title, description, falcon.HTTP_409)