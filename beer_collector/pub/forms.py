from django import forms
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from beer_collector.pub.models import Pub, PubComment


class PubCreateForm(forms.ModelForm):
    MAX_IMAGE_WIDTH = 1200
    MAX_IMAGE_HEIGHT = 900
    MIN_IMAGE_WIDTH = 250
    MIN_IMAGE_HEIGHT = 200

    def clean_image(self):
        image = self.cleaned_data.get('image', False)

        if image:
            width, height = get_image_dimensions(image)
            if PubCreateForm.MIN_IMAGE_WIDTH > width > PubCreateForm.MAX_IMAGE_WIDTH or \
                    PubCreateForm.MIN_IMAGE_HEIGHT > height > PubCreateForm.MAX_IMAGE_HEIGHT:
                raise ValidationError("Width or Height is larger than what is allowed")

        return image

    class Meta:
        model = Pub
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pub name',
                    'style': 'width: 400px',
                    'class': 'form-control',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pub address',
                    'style': 'width: 400px',
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about this pub',
                    'rows': 6,
                    'cols': 60,
                    'style': 'resize: none',
                    'class': 'form-control',
                }
            ),
            'website': forms.URLInput(
                attrs={
                    'placeholder': 'Enter valid url',
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


class PubEditForm(PubCreateForm):
    pass


class PubCommentForm(forms.ModelForm):
    obj_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    def save(self, commit=True):
        pub_pk = self.cleaned_data['obj_pk']
        pub = Pub.objects.get(pk=pub_pk)
        comment = PubComment(
            comment=self.cleaned_data['comment'],
            pub=pub,
        )

        if commit:
            comment.save()

        return comment

    class Meta:
        model = PubComment
        fields = ('comment', 'obj_pk')
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Enter yor comment here.',
                    'rows': 6,
                    'cols': 60,
                    'style': 'resize: none; background-color:transparent',
                    'class': 'form-control',
                }
            )
        }
