import random

from django import forms

BLUE_CHOICES = (
    ('1', 'Play Feature'),
    ('2', 'Beach '),
    ('3', 'Sails '),
    ('4', 'Break'),
    ('5', 'Peninsula'),
    ('6', 'Lap Chair 1'),
    ('7', 'Lap Chair 2'),
    ('8', 'Duty'),
    ('9', 'Lap chair 3'),
    ('10', 'C. Roam'),
    ('11', 'Lap Chair 4'),
    ('11', 'Break'),
)

GREEN_CHOICES = (
    ('1', 'Adventure Slides'),
    ('2', 'Catch Pool'),
    ('3', 'Lily Pads (Wknd)'),
    ('4', 'Lazy Green'),
    ('5', 'Break'),
    ('6', 'Dive Well'),
    ('7', 'Rock Wall'),
    ('8', 'Plunge Slide'),
    ('9', 'Duty'),
)

RED_CHOICES = (
    ('1', 'Indoor'),
    ('2', 'Kiddie'),
    ('3', 'Kiddie 2 (Wknd)'),
    ('4', 'Red Duty'),
    ('5', 'Lazy River Chair 1'),
    ('6', 'Lazy River Chair 2'),
    ('7', 'Lazy River Chair 3'),
    ('8', 'Break'),
)


class Form(forms.Form):
    names = forms.CharField(
        widget=forms.Textarea(
            attrs=dict(placeholder='Paste Names Here...'),
        ),
    )
    blue = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs=dict(checked=True),
        ),
        choices=BLUE_CHOICES,
    )
    red = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs=dict(checked=True),
        ),
        choices=RED_CHOICES,
    )
    green = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs=dict(checked=True),
        ),
        choices=GREEN_CHOICES,
    )

    def clean_names(self):
        names = [
            name.strip() for name in self.cleaned_data['names'].split('\r\n')
        ]
        random.shuffle(names)
        self.cleaned_data['names'] = names
        return names

    def clean_blue(self):
        blue = len(self.cleaned_data['blue'])
        self.cleaned_data['blue'] = blue
        return blue

    def clean_red(self):
        red = len(self.cleaned_data['red'])
        self.cleaned_data['red'] = red
        return red

    def clean_green(self):
        green = len(self.cleaned_data['green'])
        self.cleaned_data['green'] = green
        return green
