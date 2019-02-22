from application.forms import BaseForm
from wtforms import StringField, IntegerField, SelectField, DecimalField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, Length, DataRequired, NumberRange
from application.organizations.models import Organization

class CustomerForm(BaseForm):
    first_name = StringField("Etunimi", validators=[Length(min=2, max=50, message="Etunimen tulee olla vähintään 2 merkkiä ja korkeintaan 50 merkkiä"), 
    DataRequired(message="Etunimi ei voi olla tyhjä")])

    last_name = StringField("Sukunimi", validators=[Length(min=2, max=50, message="Sukunimen tulee olla vähintään 2 merkkiä ja korkeintaan 50 merkkiä"), 
    DataRequired(message="Sukunimi ei voi olla tyhjä")])

    birthday = IntegerField("Syntymäpäivä", validators=[NumberRange(min=0, max=3112, message="Syntymäpäivän tulee olla korkeintaan 3112 ja vähintään 0")])

    balance = DecimalField("Piikki", validators=[NumberRange(min=-1000, message="Piikki tulee olla vähintään -1000")])

    organization_id = SelectField("Järjestö", coerce=int ,validators=[DataRequired(message="Organizaatio ei voi olla tyhjä")])


class CustomerBlockForm(BaseForm):
    date_end = DateField("Eston loppumisaika", format="%Y-%m-%d", validators=[DataRequired(message="Päivämäärä ei voi olla tyhjä")])