from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, RegexValidator
from django.utils.translation import ugettext_lazy as _


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

def validate_url(url):
    validator_url = URLValidator()
    try:
        validator_url(url)
    except:
        raise ValidationError(_("Invalid URL!"))
    return url
