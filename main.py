import datetime

from flask import Flask, request, jsonify

from API import api
from Config.BaseConfig import BaseConfig
from Database import db
from Database.Models.ScanResult import ScanResult
from Scanner.scanner3 import scan_domain
from login_manager import login_manager

app = Flask(__name__)
app.config.from_object(BaseConfig)

db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(api)


@app.get('/')
def handle_home():
    return 'CopyOfShodan'


@app.get('/scan')
def handle_scan():
    domain = request.args['domain']

    cached_scan_result: ScanResult
    cached_scan_result = ScanResult.query.filter(ScanResult.host_name == domain).first()

    if cached_scan_result is not None and datetime.datetime.now() - cached_scan_result.timestamp < datetime.timedelta(seconds=60):
        return jsonify({
            **cached_scan_result.to_dict(),
            'fresh': False
        })

    try:
        scan_result = scan_domain(host_name=domain)
    except Exception as e:
        return {
            'error': {
                'type': 'ScanError',
                'message': str(e)
            }
        }, 400

    if cached_scan_result is None:
        db.session.add(scan_result)
    else:
        cached_scan_result.protocol = scan_result.protocol
        cached_scan_result.certificate = scan_result.certificate
        cached_scan_result.timestamp = scan_result.timestamp

    db.session.commit()

    return jsonify({
        **scan_result.to_dict(),
        'fresh': True
    })


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
