from django import forms
from .models import Sheet
from django.shortcuts import get_object_or_404

class SheetForm(forms.ModelForm):
    class Meta:
        model = Sheet
        fields = [
            'title',
            'category',
            't_img',
            't_debut',
            't_form',
            't_affil',
            't_bday',
            't_bplace',
            't_age',
            'body',
            #'section1',
            #'section2',
            #'section3',
            #'section4',
            #'section5',
            'rank_s',
            'rank_e',
            'rank_m',
            'rank_i',
            'rank_r',
            'rank_t',
            'section6',
        ]

    # Ensures validity of null ImageField
    def __init__(self, *args, **kwargs):
        super(SheetForm, self).__init__(*args, **kwargs)
        self.fields['t_img'].required = False

