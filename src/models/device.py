from uuid                           import uuid4
from sqlalchemy                     import Column, DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import JSONB
from models.base                    import Base



class Device(Base):
    __tablename__ = 'device'

    id             = Column(Integer, primary_key=True)
    device_key     = Column(String)
    signature_key  = Column(String)
    name           = Column(String)
    settings       = Column(JSONB)
    created_at     = Column(DateTime, server_default=func.now())
    deactivated_on = Column(DateTime)
