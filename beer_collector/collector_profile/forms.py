import os
from django import forms
from django.conf import settings

from beer_collector.account.models import Account
from beer_collector.collector_profile.models import CollectorProfile
from beer_collector.core.views import get_obj_by_pk


class CollectorProfileForm(forms.ModelForm):
    def save(self, commit=True):
        current_profile = get_obj_by_pk(CollectorProfile, self.instance.pk)
        current_user = get_obj_by_pk(Account, self.instance.pk)
        if commit and current_profile.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(current_profile.image)))
            os.rmdir(os.path.join(settings.MEDIA_ROOT, str(current_user.email)))
            current_profile.image.delete()
        return super().save(commit)

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
                    'style': 'width: 145; height: 200'
                }
            ),
        }
