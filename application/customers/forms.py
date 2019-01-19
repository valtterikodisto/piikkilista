from application.forms import BaseForm
from wtforms import StringField, IntegerField, SelectField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, Length, DataRequired, NumberRange
from application.organizations.models import Organization

# class Length(object):
#     def __init__(self, min=-1, max=-1, message=None):
#         self.min = min
#         self.max = max
#         if not message:
#             message = u'Field must be between %i and %i characters long.' % (min, max)
#         self.message = message

#     def __call__(self, form, field):
#         l = field.data and len(field.data) or 0
#         if l < self.min or self.max != -1 and l > self.max:
#             raise ValidationError(self.message)
    

class CustomerForm(BaseForm):
    first_name = StringField("Etunimi", validators=[Length(min=2, max=50, message="Etunimen tulee olla vähintään 2 merkkiä ja korkeintaan 50 merkkiä"), 
    DataRequired(message="Etunimi ei voi olla tyhjä")])

    last_name = StringField("Sukunimi", validators=[Length(min=2, max=50, message="Sukunimen tulee olla vähintään 2 merkkiä ja korkeintaan 50 merkkiä"), 
    DataRequired(message="Sukunimi ei voi olla tyhjä")])

    birthday = IntegerField("Syntymäpäivä", validators=[NumberRange(min=0, max=3112, message="Syntymäpäivän tulee olla korkeintaan 3112 ja vähintään 0")])

    balance = IntegerField("Piikki", validators=[NumberRange(min=-100000, max=100000, message="Piikki tulee olla vähintään -100000 ja korkeintaan 100000")])

    organization_id = SelectField("Järjestö", coerce=int ,validators=[DataRequired(message="Organizaatio ei voi olla tyhjä")])


class CustomerBlockForm(BaseForm):
    date_end = DateField("Eston loppumisaika", format="%Y-%m-%d", validators=[DataRequired(message="Päivämäärä ei voi olla tyhjä")])