import os
from django import forms
from django.conf import settings
from beer_collector.core.views import get_obj_by_pk
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from beer_collector.collector_profile.models import CollectorProfile


class CollectorProfileForm(forms.ModelForm):
    MAX_IMAGE_WIDTH = 1200
    MAX_IMAGE_HEIGHT = 900
    MIN_IMAGE_WIDTH = 250
    MIN_IMAGE_HEIGHT = 200

    def save(self, commit=True):
        current_profile = get_obj_by_pk(CollectorProfile, self.instance.pk)
        new_image = self.files.get('image')
        old_image = str(current_profile.image)
        old_image_path = os.path.join(settings.MEDIA_ROOT, old_image)
        if commit and new_image and old_image and not old_image_path == 'anonymous_profile_img.jpg':
            os.remove(old_image_path)
        return super().save(commit=commit)

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        width, height = get_image_dimensions(image)

        if image:
            if CollectorProfileForm.MIN_IMAGE_WIDTH > width > CollectorProfileForm.MAX_IMAGE_WIDTH or \
                    CollectorProfileForm.MIN_IMAGE_HEIGHT > height > CollectorProfileForm.MAX_IMAGE_HEIGHT:
                raise ValidationError("Width or Height is larger than what is allowed")
        else:
            raise ValidationError("No image found")

        return image

    class Meta:
        model = CollectorProfile
        exclude = ('is_complete', 'user',)
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter username',
                    'style': 'width: 400px',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                    'style': 'width: 400px',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                    'style': 'width: 400px',
                }
            ),
            'about': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about yourself',
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
