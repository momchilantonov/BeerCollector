from django import forms
from beer_collector.beer.models import BeerStyle, Beer


class BeerStyleCreateForm(forms.ModelForm):
    class Meta:
        mode = BeerStyle
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Enter beer type',
                    'style': 'width: 400px',
                }
            )
        }


class BeerStyleEditForm(BeerStyleCreateForm):
    pass


class BeerCreateForm(forms.ModelForm):
    class Meta:
        model = Beer
        exclude = ('type', 'user',)
        widgets = {
            'label': forms.TextInput(
                attrs={
                    'placeholder': 'Enter beer label',
                    'style': 'width: 400px',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about this beer',
                    'rows': 6,
                    'cols': 54,
                    'style': 'resize: none',
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'style': 'width: 145; height: 200'
                }
            ),
        }


class BeerEditForm(BeerCreateForm):
    pass
