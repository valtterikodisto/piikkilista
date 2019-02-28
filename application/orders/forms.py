from application.forms import BaseForm
from wtforms import StringField, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange
from application.orders.models import Drink

class OrderForm(BaseForm):
  first_name = StringField("Etunimi", validators=[DataRequired(message="Etunimi ei voi olla tyhjä")])
  last_name = StringField("Sukunimi", validators=[DataRequired(message="Sukunimi ei voi olla tyhjä")])
  birthday = birthday = IntegerField("Syntymäpäivä")
  organization_id = SelectField("Järjestö", coerce=int ,validators=[DataRequired(message="Organizaatio ei voi olla tyhjä")])

  beer = IntegerField("Olut", default=0)
  long_drink = IntegerField("Lonkero", default=0)
  cider = IntegerField("Siideri", default=0)
  soft_drink = IntegerField("Alkoholiton", default=0)
  special_beer = IntegerField("Erikoisolut", default=0)
  drink = IntegerField("Drinkki", default=0)
  special_drink = IntegerField("Erikoisdrinkki", default=0)
  whisky = IntegerField("Viski", default=0)

  deposit = DecimalField("Talletus", default=0)