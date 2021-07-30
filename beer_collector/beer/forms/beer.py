from django import forms
from beer_collector.beer.models.beer import Beer, BeerComment
from beer_collector.beer.models.beer_style import BeerStyle, BeerStyleComment


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


class BeerCommentForm(forms.ModelForm):
    beer_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    def save(self, commit=True):
        beer_pk = self.cleaned_data['beer_pk']
        beer = BeerStyle.objects.get(pk=beer_pk)
        comment = BeerComment(
            comment=self.cleaned_data['comment'],
            beer=beer,
        )

        if commit:
            comment.save()

        return comment

    class Meta:
        model = BeerStyleComment
        fields = ('comment', 'beer_pk')
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about this beer',
                    'rows': 6,
                    'cols': 54,
                    'style': 'resize: none',
                }
            )
        }
