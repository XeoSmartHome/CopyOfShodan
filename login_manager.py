from flask_login import LoginManager


login_manager = LoginManager()


@login_manager.user_loader
def _login_manager_user_loader(user_id):
    # return Developer.query.get(user_id)
    pass


@login_manager.unauthorized_handler
def _unauthorized_handler():
    return {}
