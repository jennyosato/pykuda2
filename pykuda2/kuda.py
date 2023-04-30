from pykuda2.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pykuda2.utils import Mode
from pykuda2.wrappers.sync_wrappers.accounts import Account
from pykuda2.wrappers.sync_wrappers.billing_and_betting import BillingAndBetting
from pykuda2.wrappers.sync_wrappers.card import Card
from pykuda2.wrappers.sync_wrappers.gift_card import GiftCard
from pykuda2.wrappers.sync_wrappers.savings import Savings
from pykuda2.wrappers.sync_wrappers.transaction import Transaction


class Kuda(BaseAPIWrapper):
    """A synchronous API wrapper to Kuda REST API endpoints.

    Args:
        email: The email address of your Kuda account with access to an apiKey
        api_key: Your Kuda apiKey
        mode: The mode you desire to use the wrapper in (development or production)
    """

    def __init__(self, email: str, api_key: str, mode: Mode = Mode.DEVELOPMENT):
        super().__init__(email=email, api_key=api_key, mode=mode)
        self.accounts = Account(email=email, api_key=api_key, mode=mode)
        self.transactions = Transaction(email=email, api_key=api_key, mode=mode)
        self.billing_and_betting = BillingAndBetting(
            email=email, api_key=api_key, mode=mode
        )
        self.gift_cards = GiftCard(email=email, api_key=api_key, mode=mode)
        self.savings = Savings(email=email, api_key=api_key, mode=mode)
        self.cards = Card(email=email, api_key=api_key, mode=mode)
        # All the attributes above are API wrappers in themselves which means
        # they'll individually try to get the access token with the `emai` and
        # `api_key`. This is like to result in some performance issues. this is
        # a hacky solution to this issue. We use this `Kuda` wrapper to get the
        # `access_token` and feed it to all these attributes, so they don't have
        # to make a request to get the access token.
        self.accounts._saved_token = self._token
        self.transactions._saved_token = self._token
        self.billing_and_betting._saved_token = self._token
        self.gift_cards._saved_token = self._token
        self.savings._saved_token = self._token
        self.cards._saved_token = self._token


class AsyncKuda(BaseAsyncAPIWrapper):
    """An asynchronous API wrapper to Kuda REST API endpoints.

    Args:
        email: The email address of your Kuda account with access to an apiKey
        api_key: Your Kuda apiKey
        mode: The mode you desire to use the wrapper in (development or production)
    """

    def __init__(self, email: str, api_key: str, mode: Mode = Mode.DEVELOPMENT):
        super().__init__(email=email, api_key=api_key, mode=mode)
        self.accounts = Account(email=email, api_key=api_key, mode=mode)
        self.transactions = Transaction(email=email, api_key=api_key, mode=mode)
        self.billing_and_betting = BillingAndBetting(
            email=email, api_key=api_key, mode=mode
        )
        self.gift_cards = GiftCard(email=email, api_key=api_key, mode=mode)
        self.savings = Savings(email=email, api_key=api_key, mode=mode)
        self.cards = Card(email=email, api_key=api_key, mode=mode)
