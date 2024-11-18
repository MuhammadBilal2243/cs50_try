from django.forms import ModelForm
from .models import tasks
class taskForms(ModelForm):
    class Meta:
        model=tasks
        fields= '__all__'