from django import forms
from beer_collector.collector_profile.models import CollectorProfile


class CollectorProfileForm(forms.ModelForm):
    class Meta:
        model = CollectorProfile
        exclude = ('user', 'is_complete')
        widgets = {
            'image': forms.FileInput(),
            'about': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about yourself',
                    'rows': 4,
                    'style': 'resize:none',
                }
            )
        }
