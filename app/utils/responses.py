from fastapi import HTTPException

class BadRequest(HTTPException):
    def __init__(self, content='Bad Request'):
        super().__init__(status_code=400, detail=content)

class NotFound(HTTPException):
    def __init__(self, content='Not Found'):
        super().__init__(status_code=404, detail=content)

class Unauthorized(HTTPException):
    def __init__(self, content='Unauthorized'):
        super().__init__(status_code=401, detail=content)

class NoContent(HTTPException):
    def __init__(self, content='No Content'):
        super().__init__(status_code=204, detail=content)

class InternalServerError(HTTPException):
    def __init__(self, content='Internal Server Error'):
        super().__init__(status_code=500, detail=content)

class FileSizeLimit(HTTPException):
    def __init__(self, content='File size exceeds 4 MB limit'):
        super().__init__(status_code=413, detail=content)


class UnsupportedImageFormat(HTTPException):
    def __init__(self, content='Unsupported image format'):
        super().__init__(status_code=415, detail=content)


class DateFormat(HTTPException):
    def __init__(self, content='Date must be in the format dd.mm.yyyy'):
        super().__init__(status_code=422, detail=content)


class ProcessableEntity(HTTPException):
    def __init__(self, content='Unprocessable Entity'):
        super().__init__(status_code=422, detail=content)
