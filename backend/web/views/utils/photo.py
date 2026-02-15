from backend import settings
import os

def remove_old_photo(photo):
    if photo and photo.name != "user/photos/default.jpg":
        old_path = settings.MEDIA_ROOT / photo.name
        if old_path.exists():
            os.remove(old_path)