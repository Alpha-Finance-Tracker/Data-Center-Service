from app.utils.responses import UnsupportedImageFormat, FileSizeLimit
import filetype


class ImageValidator:
    @staticmethod
    async def validate_image(file):
        try:
            file_bytes = await file.read()
            if len(file_bytes) > 4 * 1024 * 1024:
                raise FileSizeLimit()


            kind = filetype.guess(file.file)
            if not kind:
                raise UnsupportedImageFormat()

            if kind.mime not in ['image/jpeg','image/png'] :
                raise UnsupportedImageFormat()


            await file.seek(0)
            return file
        except Exception as e:
            raise e
