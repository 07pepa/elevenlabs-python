# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .extended_subscription_response_model_currency import ExtendedSubscriptionResponseModelCurrency
from .invoice_response_model import InvoiceResponseModel
from .subscription_status import SubscriptionStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Subscription(pydantic.BaseModel):
    tier: str
    character_count: int
    character_limit: int
    can_extend_character_limit: bool
    allowed_to_extend_character_limit: bool
    next_character_count_reset_unix: int
    voice_limit: int
    max_voice_add_edits: typing.Optional[int]
    voice_add_edit_counter: typing.Optional[int]
    professional_voice_limit: int
    can_extend_voice_limit: bool
    can_use_instant_voice_cloning: bool
    can_use_professional_voice_cloning: bool
    status: typing.Optional[SubscriptionStatus]
    has_open_invoices: typing.Optional[bool]
    currency: typing.Optional[ExtendedSubscriptionResponseModelCurrency]
    next_invoice: typing.Optional[InvoiceResponseModel]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}