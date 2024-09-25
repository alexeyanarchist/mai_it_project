from wtforms import Form, BooleanField, StringField, PasswordField, validators, TimeField, IntegerField

class RegistrationForm(Form):
    username = StringField('Имя пользователя', [validators.Length(min=4, max=25)])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Пароли должны совпадать')
    ])
    confirm = PasswordField('Повторите пароль')

class LoginForm(Form):
    username = StringField('Имя пользователя', [validators.Length(min=4, max=25)])
    password = PasswordField('Пароль', [validators.DataRequired()])

class OrderForm(Form):
    pepperoni = IntegerField("Пепперони")
    spagetti = IntegerField("Спагетти")
    diablo = IntegerField("Диабло")
    order_time = TimeField("Время доставки заказа")