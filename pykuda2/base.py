from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional


class Mode(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class ServiceType(str, Enum):
    """
    An enumeration of Service Types Provided by Kuda

    Attributes:
        ADMIN_CREATE_VIRTUAL_ACCOUNT: Create a virtual account under your main account
        ADMIN_VIRTUAL_ACCOUNTS: Get all Virtual account
        ADMIN_UPDATE_VIRTUAL_ACCOUNT: Update virtual account details
        ADMIN_DISABLE_VIRTUAL_ACCOUNT: Deactivate a virtual account
        ADMIN_ENABLE_VIRTUAL_ACCOUNT: Reactivate a virtual account
        RETRIEVE_SINGLE_VIRTUAL_ACCOUNT: Retrieve the details on a created virtual account
        BANK_LIST: Get a list of all banks
        NAME_ENQUIRY: Retrieve the name linked to a bank account
        SINGLE_FUND_TRANSFER: Transfer money from your main account
        VIRTUAL_ACCOUNT_FUND_TRANSFER: Transfer money from a virtual account
    """

    ADMIN_CREATE_VIRTUAL_ACCOUNT = "ADMIN_CREATE_VIRTUAL_ACCOUNT"
    ADMIN_VIRTUAL_ACCOUNTS = "ADMIN_VIRTUAL_ACCOUNTS"
    ADMIN_UPDATE_VIRTUAL_ACCOUNT = "ADMIN_UPDATE_VIRTUAL_ACCOUNT"
    ADMIN_DISABLE_VIRTUAL_ACCOUNT = "ADMIN_DISABLE_VIRTUAL_ACCOUNT"
    ADMIN_ENABLE_VIRTUAL_ACCOUNT = "ADMIN_ENABLE_VIRTUAL_ACCOUNT"
    RETRIEVE_SINGLE_VIRTUAL_ACCOUNT = "RETRIEVE_SINGLE_VIRTUAL_ACCOUNT"
    BANK_LIST = "BANK_LIST"
    NAME_ENQUIRY = "NAME_ENQUIRY"
    SINGLE_FUND_TRANSFER = "SINGLE_FUND_TRANSFER"
    VIRTUAL_ACCOUNT_FUND_TRANSFER = "VIRTUAL_ACCOUNT_FUND_TRANSFER"
    TRANSACTION_STATUS_QUERY = "TRANSACTION_STATUS_QUERY"


class AbstractAPIWrapper(ABC):
    def __init__(self, email: str, api_key: str, mode=Mode.DEVELOPMENT):
        self.mode = mode
        self.email = email
        self.api_key = api_key
        self._token: Optional[str] = None

    @property
    @abstractmethod
    def token(self) -> str:
        ...

    @property
    @abstractmethod
    def headers(self) -> dict:
        ...

    @property
    def base_url(self) -> str:
        return {
            Mode.DEVELOPMENT: "http://kuda-openapi-uat.kudabank.com/v2.1",
            Mode.PRODUCTION: "https://kuda-openapi.kuda.com/v2.1",
        }[self.mode]

    @abstractmethod
    def api_call(self):
        ...


class APIWrapper(AbstractAPIWrapper):
    def __init__(self, email: str, api_key: str, mode=Mode.DEVELOPMENT):
        super().__init__(email=email, api_key=api_key, mode=mode)

    @property
    def token(self) -> str:
        if self._token:
            return self._token
        else:
            ...

    @property
    def headers(self) -> dict:
        return {}

    def api_call(self):
        ...


class AsyncAPIWrapper(AbstractAPIWrapper):
    def __init__(self, email: str, api_key: str, mode=Mode.DEVELOPMENT):
        super().__init__(email=email, api_key=api_key, mode=mode)
