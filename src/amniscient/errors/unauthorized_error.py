# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.api_error import ApiError
from ..types.unauthorized_error_body import UnauthorizedErrorBody


class UnauthorizedError(ApiError):
    def __init__(self, body: UnauthorizedErrorBody, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=401, headers=headers, body=body)
