from django.forms import ModelForm
from .models import Checked

class CheckedForm(ModelForm):
    class Meta:
        model = Checked
        fields = ['date', 'setup']
        