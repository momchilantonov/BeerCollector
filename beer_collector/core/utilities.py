import os
from django.conf import settings
from beer_collector.account.models import Account


def get_obj_by_pk(obj, pk):
    return obj.objects.get(pk=pk)


def delete_previous_image(self, commit, model, previous_image):
    current_profile = get_obj_by_pk(model, self.instance.pk)
    new_image = self.files.get('image')
    old_image = str(current_profile.image)
    old_image_path = os.path.join(settings.MEDIA_ROOT, old_image)
    if commit and new_image and old_image and not old_image_path == previous_image:
        os.remove(old_image_path)


def image_upload_location(instance, filename):
    current_user = get_obj_by_pk(Account, instance.pk)
    return f'{os.path.join(current_user.email, filename)}'
