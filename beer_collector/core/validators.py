from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from beer_collector.core.constants import ALLOWED_IMAGE_SIZE


class Validator:

    @staticmethod
    def image_size_validation(image):
        width, height = get_image_dimensions(image)

        if ALLOWED_IMAGE_SIZE['max_image_width'] < width or \
                ALLOWED_IMAGE_SIZE['max_image_height'] < height:
            raise ValidationError('Width or Height is larger than what is allowed.')
