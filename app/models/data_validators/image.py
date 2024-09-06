from io import BytesIO
from PIL import Image


class ImageValidator:
    @staticmethod
    async def validate_image(file):
        try:
            file_bytes = await file.read()
            if len(file_bytes) > 4 * 1024 * 1024:  # 4 MB
                raise ValueError('File size exceeds 4 MB limit')

            if file.content_type not in {'image/jpeg', 'image/png'}:
                raise ValueError('Unsupported image format')

            await file.seek(0)
            return file
        except Exception as e:
            raise e