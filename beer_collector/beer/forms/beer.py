from django import forms
from beer_collector.beer.models.beer import Beer, BeerComment
from beer_collector.core.utilities import delete_previous_image
from beer_collector.core.validators import Validator


class BeerCreateForm(forms.ModelForm):
    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            Validator.image_size_validation(image)

        return image

    class Meta:
        model = Beer
        exclude = ('user',)
        widgets = {
            'label': forms.TextInput(
                attrs={
                    'placeholder': 'Enter beer label',
                    'style': 'width: 400px',
                    'class': 'form-control',
                }
            ),
            'type': forms.Select(
                attrs={
                    'style': 'width: 400px',
                    'class': 'form-select'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about this beer',
                    'rows': 6,
                    'cols': 60,
                    'style': 'resize: none',
                    'class': 'form-control',
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'style': 'width: 145; height: 200',
                    'class': 'form-control',
                }
            ),
        }


class BeerEditForm(BeerCreateForm):
    def save(self, commit=True):
        delete_previous_image(self, commit, Beer, 'no_beer.jpeg')
        return super().save(commit=commit)


class BeerCommentForm(forms.ModelForm):
    obj_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    def save(self, commit=True):
        beer_style_pk = self.cleaned_data['obj_pk']
        beer = Beer.objects.get(pk=beer_style_pk)
        comment = BeerComment(
            comment=self.cleaned_data['comment'],
            beer=beer,
        )

        if commit:
            comment.save()

        return comment

    class Meta:
        model = BeerComment
        fields = ('comment', 'obj_pk')
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about this beer',
                    'rows': 6,
                    'cols': 60,
                    'style': 'resize: none; background-color:transparent',
                    'class': 'form-control',
                }
            )
        }
