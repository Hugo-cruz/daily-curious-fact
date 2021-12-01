from django.db.models.base import Model
from django.forms import ModelForm
from .models import Curiosities

class CuriositiesForm(ModelForm):
    class Meta:
        model = Curiosities
        fields = ['text','category_id']