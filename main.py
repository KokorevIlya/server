from flask import Flask, render_template, jsonify
from data import db_session
from data.users import User
from data.jobs import Jobs
from data import db_session, news_api
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(news_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
