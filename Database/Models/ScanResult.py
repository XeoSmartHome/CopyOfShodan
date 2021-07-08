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
    whois = db.Column(db.String(), name='WHOIS', nullable=True)
    rdap = db.Column(db.String(), name='RDAP', nullable=True)

    timestamp = db.Column(db.DateTime(), name='TIMESTAMP', nullable=False)

    def __init__(self, host_name: str, ip_address: str, is_secure: bool, protocol: str, certificate: str, whois: str, rdap: str):
        self.host_name = host_name
        self.ip_address = ip_address
        self.is_secure = is_secure
        self.protocol = protocol
        self.certificate = certificate
        self.whois = whois
        self.rdap = rdap
        self.timestamp = datetime.datetime.now()

    def to_dict(self):
        return {
            'hostName': self.host_name,
            'ipAddress': self.ip_address,
            'isSecure': self.is_secure,
            'protocol': self.protocol,
            'certificate': json.loads(self.certificate),
            'whois': json.loads(self.whois),
            'rdap': json.loads(self.rdap),
            'timestamp': self.timestamp
        }
