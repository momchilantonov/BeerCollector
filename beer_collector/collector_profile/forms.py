from django import forms
from beer_collector.collector_profile.models import CollectorProfile
from beer_collector.core.utilities import delete_previous_image
from beer_collector.core.validators import Validator


class CollectorProfileForm(forms.ModelForm):
    def save(self, commit=True):
        delete_previous_image(self, commit, CollectorProfile, 'anonymous_profile_img.jpg')
        return super().save(commit=commit)

    def clean_image(self):
        image = self.cleaned_data.get('image', False)

        if image:
            Validator.image_size_validation(image)

        return image

    class Meta:
        model = CollectorProfile
        exclude = ('is_complete', 'user',)
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter username',
                    'style': 'width: 400px',
                    'class': 'form-control',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                    'style': 'width: 400px',
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                    'style': 'width: 400px',
                    'class': 'form-control',
                }
            ),
            'about': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about yourself',
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
