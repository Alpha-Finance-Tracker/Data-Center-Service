from app.utils.responses import UnsupportedImageFormat, FileSizeLimit


class ImageValidator:
    @staticmethod
    async def validate_image(file):
        try:
            file_bytes = await file.read()
            if len(file_bytes) > 4 * 1024 * 1024:  # 4 MB
                raise FileSizeLimit()

            if file.content_type not in {'image/jpeg', 'image/png'}:
                raise UnsupportedImageFormat()

            await file.seek(0)
            return file
        except Exception as e:
            raise e
