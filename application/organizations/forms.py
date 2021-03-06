from application.forms import BaseForm
from wtforms import StringField, DecimalField, validators
from wtforms.validators import ValidationError, NumberRange

def validate_name(form, field):
    if (len(field.data) < 2):
        raise ValidationError('Järjestön nimen tulee olla vähintään 2 merkkiä')
    elif (len(field.data) > 50):
        raise ValidationError('Järjestön nimen tulee olla korkeintaan 50 merkkiä')
    
    return None

class OrganizationForm(BaseForm):
    name = StringField("Järjestön nimi", [validate_name])
    limit = DecimalField("Jäsenen maksimivelka", validators=[NumberRange(min=0, max=1000, message="Maksimivelan tulee olla positiivinen ja korkeintaan 1000")])