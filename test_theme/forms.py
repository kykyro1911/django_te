from django.forms import ModelForm
from .models import ex_excel

# Create the form class.

class ex_form(ModelForm):
    class Meta:
        model = ex_excel
        fields = '__all__'
