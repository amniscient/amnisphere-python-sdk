# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UnauthorizedErrorBody(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    A status code denoting success or failure.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A message describing your error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
