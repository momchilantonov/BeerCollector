from django import forms
from beer_collector.beer.models.beer_style import BeerStyle, BeerStyleComment


class BeerStyleCreateForm(forms.ModelForm):
    class Meta:
        model = BeerStyle
        exclude = ('user',)
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Enter beer type',
                    'style': 'width: 400px',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about this style',
                    'rows': 6,
                    'cols': 54,
                    'style': 'resize: none',
                }
            ),
        }


class BeerStyleEditForm(BeerStyleCreateForm):
    pass


class BeerStyleCommentForm(forms.ModelForm):
    beer_style_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    def save(self, commit=True):
        beer_style_pk = self.cleaned_data['beer_style_pk']
        beer_style = BeerStyle.objects.get(pk=beer_style_pk)
        comment = BeerStyleComment(
            comment=self.cleaned_data['comment'],
            beer_style=beer_style,
        )

        if commit:
            comment.save()

        return comment

    class Meta:
        model = BeerStyleComment
        fields = ('comment', 'beer_style_pk')
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Enter yor comment here.',
                    'rows': 6,
                    'cols': 60,
                    'style': 'resize: none; background-color:transparent',
                }
            )
        }
