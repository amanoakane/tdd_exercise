from django import forms
from .models import Clue


class DrillForm(forms.Form):
    answer = forms.TextInput()
    clue_id =  clue = Clue.objects.order_by("?").first().id

    class Meta:
        model = Clue
        fields = ['clue_id','answer']