import flask
from flask import jsonify, make_response, request
from . import db_session
from .news import News
from .jobs import Jobs
from .users import User

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)
@blueprint.route('/api/users')
def get_jobs():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(('surname', 'name', 'position', 'speciality'))
                 for item in users]
        }
    )
