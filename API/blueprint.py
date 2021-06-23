from flask import Blueprint

api = Blueprint('api', __name__)


@api.errorhandler(AssertionError)
def handle_assertion_exception(error):
    return {'error': 'AssertionError'}


@api.errorhandler(Exception)
def handle_exception(error):
    print(error)
    return {'error': 'Exception'}
