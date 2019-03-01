from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, Length, EqualTo
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi", [InputRequired()])
    password = PasswordField("Salasana", [InputRequired()])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField('Käyttäjänimi', [Length(min=2, max=144, message="Etunimen tulee olla vähintään 2 merkkiä ja korkeintaan 144 merkkiä")])
    password = PasswordField('Salasana', [InputRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=8, max=144, message="Salasanan tulee olla vähintään 8 merkkiä ja korkeintaan 144 merkkiä")])
    confirm  = PasswordField('Salasana uudestaan')
