from django import forms
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from beer_collector.beer.models.beer import Beer, BeerComment


class BeerCreateForm(forms.ModelForm):
    MAX_IMAGE_WIDTH = 1200
    MAX_IMAGE_HEIGHT = 900
    MIN_IMAGE_WIDTH = 250
    MIN_IMAGE_HEIGHT = 200

    class Meta:
        model = Beer
        exclude = ('user',)
        widgets = {
            'label': forms.TextInput(
                attrs={
                    'placeholder': 'Enter beer label',
                    'style': 'width: 400px',
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
                    'cols': 54,
                    'style': 'resize: none',
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'style': 'width: 145; height: 200',
                    'class': 'form-control',
                }
            ),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        width, height = get_image_dimensions(image)

        if image:
            if BeerCreateForm.MIN_IMAGE_WIDTH > width > BeerCreateForm.MAX_IMAGE_WIDTH or \
                    BeerCreateForm.MIN_IMAGE_HEIGHT > height > BeerCreateForm.MAX_IMAGE_HEIGHT:
                raise ValidationError("Width or Height is larger than what is allowed")
        else:
            raise ValidationError("No image found")

        return image


class BeerEditForm(BeerCreateForm):
    pass


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
                }
            )
        }
