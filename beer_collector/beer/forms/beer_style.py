from django import forms
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from beer_collector.beer.models.beer_style import BeerStyle, BeerStyleComment


class BeerStyleCreateForm(forms.ModelForm):
    MAX_IMAGE_WIDTH = 1200
    MAX_IMAGE_HEIGHT = 900
    MIN_IMAGE_WIDTH = 250
    MIN_IMAGE_HEIGHT = 200

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

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        width, height = get_image_dimensions(image)

        if image:
            if BeerStyleCreateForm.MIN_IMAGE_WIDTH > width > BeerStyleCreateForm.MAX_IMAGE_WIDTH or \
                    BeerStyleCreateForm.MIN_IMAGE_HEIGHT > height > BeerStyleCreateForm.MAX_IMAGE_HEIGHT:
                raise ValidationError("Width or Height is larger than what is allowed")
        else:
            raise ValidationError("No image found")

        return image


class BeerStyleEditForm(BeerStyleCreateForm):
    pass


class BeerStyleCommentForm(forms.ModelForm):
    obj_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    def save(self, commit=True):
        beer_style_pk = self.cleaned_data['obj_pk']
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
        fields = ('comment', 'obj_pk')
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
