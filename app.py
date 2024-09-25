from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_login import LoginManager, UserMixin, logout_user, login_required, login_user
from flask_sqlalchemy import SQLAlchemy

from random import randrange
from app_forms import RegistrationForm, LoginForm, OrderForm
from user_registration import user_registration, user_login, User




app = Flask(__name__)
users_dict = dict()
#login_manager= LoginManager()
#login_manager.init_app(app)
with open("secret_key.txt") as file:
    key = file.readline().strip()
    app.secret_key = key

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        users_dict, message = user_registration(User(form.username.data, form.password.data))
        flash(message)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data)
        users_dict, message = user_login(user)
        flash(message)
        if message == "login succesfully":
            #login_user(user)
            return redirect(url_for('order'))
    return render_template('login.html', form=form)
@app.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm(request.form)
    if request.method == 'POST' and form.validate():
        message = "успешный заказ"
        flash(message)
        man_order = [form.pepperoni.data, form.spagetti.data, form.diablo.data, form.order_time.data]
        print(man_order)
        
    return render_template('order.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)