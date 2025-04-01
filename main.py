from flask import Flask, render_template, jsonify
from data import db_session
from data.users import User
from data import db_session, news_api
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Pierre"
    user.name = "Fermat"
    user.age = 21
    user.position = "king"
    user.speciality = "mathematics"
    user.address = "prime_n2"
    user.email = "ferma228@prime.n"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Leonard"
    user.name = "Euler"
    user.age = 117
    user.position = "student"
    user.speciality = "mathematics"
    user.address = "module_prime"
    user.email = "euler@FEuler.prime"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Claudius"
    user.name = "Ptolemaeus"
    user.age = 1234
    user.position = "captain"
    user.speciality = "geometrya"
    user.address = "module_square10"
    user.email = "geometrya@lines.py"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    # app.register_blueprint(news_api.blueprint)
    # app.run()


if __name__ == '__main__':
    main()
