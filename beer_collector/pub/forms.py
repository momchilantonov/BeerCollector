from django import forms
from beer_collector.core.utilities import delete_previous_image
from beer_collector.core.validators import Validator
from beer_collector.pub.models import Pub, PubComment


class PubCreateForm(forms.ModelForm):
    def clean_image(self):
        image = self.cleaned_data.get('image', False)

        if image:
            Validator.image_size_validation(image)

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
    def save(self, commit=True):
        delete_previous_image(self, commit, Pub, 'no_beer.jpeg')
        return super().save(commit=commit)


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
