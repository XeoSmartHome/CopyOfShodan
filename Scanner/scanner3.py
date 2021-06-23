import json
import socket
import ssl

from Database.Models.ScanResult import ScanResult


def jsonify_certificate(cert):
    return json.dumps(cert)


def scan_domain(host_name):
    context = ssl.create_default_context()

    with socket.create_connection((host_name, 443)) as sock:
        ip_address = sock.getpeername()[0]
        is_secure = False
        protocol = None
        certificate = '{}'

        try:
            with context.wrap_socket(sock, server_hostname=host_name) as secure_socket:
                protocol = secure_socket.version()
                certificate = jsonify_certificate(secure_socket.getpeercert())
                is_secure = True
        except socket.error as e:
            pass

    return ScanResult(host_name, ip_address, is_secure, protocol, certificate)


