from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from PIL import Image

from apps.general.variables import COMPANY_VIDEO_MAX_SIZE, COMPANY_LOGO_MAX_SIZE, COMPANY_BANNER_MAX_SIZE


def validate_company_video_size(video_file):
    if video_file.size > COMPANY_VIDEO_MAX_SIZE:
        raise ValidationError(_('File size must be less than 10 MB.'))

    
def validate_company_logo_size(logo_file):
    if logo_file.size > COMPANY_LOGO_MAX_SIZE:
        raise ValidationError(_('File size must be less than 2 MB.'))


def validate_company_banner_size(banner_file):
    if banner_file.size > COMPANY_BANNER_MAX_SIZE:
        raise ValidationError(_('File size must be less than 5 MB.'))


def validate_image_size(image):
    """
    Custom validator to check the uploaded image.
    """
    img = Image.open(image)
    max_width = 500
    max_height = 250
    print(img.width, img.height)
    if img.width > max_width or img.height > max_height:
        raise ValidationError(f"Image dimensions should not exceed"
                              f" {max_width}px in width and {max_height}px in height.")