from io import BytesIO
from PIL import Image


class ImageValidator:
    @staticmethod
    async def validate_image(file):
        try:
            file_bytes = await file.read()
            image = Image.open(BytesIO(file_bytes))

            if image.format not in {'JPEG', 'PNG', 'GIF'}:
                raise ValueError("Unsupported image format")

            if len(file_bytes) > 5 * 1024 * 1024:  # 5 MB
                raise ValueError("File size exceeds 5 MB limit")

            await file.seek(0)
            return file
        except Exception as e:
            raise e