from io import BytesIO
from PIL import Image
class ImageValidator:
    @staticmethod
    def validate_image(file: bytes):
        try:
            image = Image.open(BytesIO(file))
            if image.format not in {'JPEG', 'PNG', 'GIF'}:
                raise ValueError("Unsupported image format")
            if len(file) > 5 * 1024 * 1024:  # 5 MB
                raise ValueError("File size exceeds 5 MB limit")
        except Exception as e:
            raise e
