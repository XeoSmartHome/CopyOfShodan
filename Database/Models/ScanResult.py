import datetime
import json
from sqlalchemy.orm import Query

from ..connection import db


class ScanResult(db.Model):
    __tablename__ = 'SCAN_RESULT'
    query: Query

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)

    host_name = db.Column(db.String(), name='HOST_NAME', nullable=False, unique=True, index=True)
    ip_address = db.Column(db.String(), name="IP_ADDRESS", nullable=False)
    is_secure = db.Column(db.Boolean(), name='IS_SECURE', nullable=False)
    protocol = db.Column(db.String(), name='PROTOCOL', nullable=True)
    certificate = db.Column(db.String(), name='CERTIFICATE', nullable=True)

    timestamp = db.Column(db.DateTime(), name='TIMESTAMP', nullable=False)

    def __init__(self, host_name: str, ip_address: str, is_secure: bool, protocol: str, certificate: str):
        self.host_name = host_name
        self.ip_address = ip_address
        self.is_secure = is_secure
        self.protocol = protocol
        self.certificate = certificate
        self.timestamp = datetime.datetime.now()

    def to_dict(self):
        return {
            'hostName': self.host_name,
            'ipAddress': self.ip_address,
            'isSecure': self.is_secure,
            'protocol': self.protocol,
            'certificate': json.loads(self.certificate),
            'timestamp': self.timestamp
        }
