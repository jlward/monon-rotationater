from django import forms

BLUE_CHOICES = (
    ('1', 'Foo'),
    ('2', 'Bar'),
)


class Form(forms.Form):
    names = forms.CharField(
        widget=forms.Textarea(
            attrs=dict(placeholder='Paste Names Here...'),
        ),
    )
    blue = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=BLUE_CHOICES,
    )
    red = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=BLUE_CHOICES,
    )
    yellow = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=BLUE_CHOICES,
    )
