import secrets
import string
from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Optional, Union


def generate_number(length: int) -> int:
    """
    Generates random numbers of the provided length.

    Args:
        length: The length the generated number should be.
    Returns:
        The random number.
    """
    return int("".join(secrets.choice(string.digits) for _ in range(length)))


class Gender(IntEnum):
    """An enum of customer genders supported by Kuda."""

    MALE = 1
    FEMALE = 2


class CardChannel(IntEnum):
    """An enum of card channels supported by Kuda."""

    ATM = 1
    POS = 2
    WEB = 3


class TransactionStatus(str, Enum):
    """An enum of possible transaction status."""

    PENDING = "Pending"
    PROCESSING = "Processing"
    SUCCESSFUL = "Successful"
    FAILED = "Failed"


class TransactionType(str, Enum):
    """An enum of possible transaction types."""

    CREDIT = "c"
    DEBIT = "d"


class BillType(str, Enum):
    """An enum of possible bill types."""

    AIRTIME = "airtime"
    BETTING = "betting"
    INTERNET_DATA = "internet_data"
    ELECTRICITY = "electricity"
    CABLE_TV = "cableTv"


@dataclass
class TransferInstruction:
    """A model for transfer instructions.

    Attributes:
        account_number: The beneficiary's account number.
        account_name: The beneficiary's account name.
        beneficiary_bank_code: The beneficiary's bank code.
        amount: The transaction amount. Amount is in naira and kobo.
        bank_code: The beneficiary's bank code.
        narration: Transaction description.
        bank_name: The beneficiary's bank name.
        long_code: The beneficiary's long code.
        reference: A unique identifier for the transfer.
    """

    account_number: str
    account_name: str
    beneficiary_bank_code: str
    amount: int
    bank_code: str
    narration: str
    bank_name: str
    long_code: str
    reference: str

    def to_dict(self) -> dict:
        return {
            "AccountNumber": self.account_number,
            "AccountName": self.account_name,
            "BeneficiaryBankCode": self.beneficiary_bank_code,
            "Amount": self.amount,
            "BankCode": self.bank_code,
            "Narration": self.narration,
            "BankName": self.bank_name,
            "LongCode": self.long_code,
            "Reference": self.reference,
        }


@dataclass
class APIResponse:
    """A model for representing the data gotten from making a call to Kudas' API.

    Attributes:
        status_code: The HTTP status code of the call.
        status: The status of the response.
        message: The message of the response.
        data: The data from the response.
        raw: The original data gotten from the response before separating it.
            into `status`, `message` and `data`. This attribute is provided
            for cases where the response of a call does not comply the default
            format.
    """

    status_code: int
    status: Optional[str]
    message: Optional[str]
    data: Optional[dict]
    raw: Union[list, dict]


class HTTPMethod(str, Enum):
    """An enum of supported HTTP verbs."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


class Mode(str, Enum):
    """Modes the APIWrappers can operate in"""

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
        TRANSACTION_STATUS_QUERY: Get the status of a bank transfer
        RETRIEVE_VIRTUAL_ACCOUNT_BALANCE: Retrieve the account balance on a virtual account
        ADMIN_MAIN_ACCOUNT_TRANSACTIONS: Get all transactions on your account
        ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS: Get a date filtered range of transactions on your account
        ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS: Get all transactions on a virtual account
        ADMIN_VIRTUAL_ACCOUNT_FILTERED_TRANSACTIONS: Get a date filtered range of transactions on a virtual account
        FUND_VIRTUAL_ACCOUNT: Transfer money from your main account to your virtual account
        WITHDRAW_VIRTUAL_ACCOUNT: Transfer money from your virtual account to your main account
        UPDATE_VIRTUAL_ACCOUNT_LIMIT: Updated transfer limits up to N5,000,000 daily on your most critical virtual accounts
        FUND_TRANSFER_INSTRUCTION: Instruction for single transaction above the limit of One (1) million naira
        SEARCH_FUND_TRANSFER_INSTRUCTION: Search for transfer instructions and return the status of the transaction
        RETRIEVE_TRANSACTION_LOGS: Fetch all transaction from logs
        GET_GIFT_CARD: gets a list of all gift card supported
        ADMIN_BUY_GIFT_CARD: purchase gift card from admin account
        BUY_GIFT_CARD: purchase gift card from virtual account
        GIFT_CARD_TSQ: status of all gift cards purchased
        CREATE_PLAIN_SAVE: Create a plain savings account
        GET_PLAIN_SAVE: Gets a specific plain savings account information
        GET_ALL_CUSTOMER_PLAIN_SAVE: Gets all plain savings account information
        PLAIN_SAVE_DEBIT_CREDIT: Credit or debit a plain savings account
        RETRIEVE_PLAIN_SAVE_TRANSACTIONS: Retrieves plain savings account transactions
        CREATE_OPEN_FLEXIBLE_SAVE: Create an open flexible account
        PRE_CREATE_OPEN_FLEXIBLE_SAVE: Pre create an open flexible account
        GET_OPEN_FLEXIBLE_SAVE: Get a specific open flexible savings account information
        GET_ALL_CUSTOMER_OPEN_FLEXIBLE_SAVE: Get all open flexible savings account information
        COMPLETE_OPEN_FLEXIBLE_SAVE_WITHDRAWAL: Withdraw from an open flexible savings account
        RETRIEVE_OPEN_FLEXIBLE_SAVE_TRANSACTIONS: Get all open flexible account transactions
        CREATE_FIXED_SAVE: Create fixed savings account
        GET_FIXED_SAVE: Get a specific fixed account information
        GET_ALL_CUSTOMER_FIXED_SAVE: Get all fixed account information
        COMPLETE_FIXED_SAVE_WITHDRAWAL: Close a fixed savings account
        RETRIEVE_FIXED_SAVE_TRANSACTIONS: Get all fixed savings account transaction
        REQUEST_CARD: Request for a new card
        GET_CUSTOMER_CARDS: Get a list of all the cards requested
        ACTIVATE_CARD: Activates a new card
        DEACTIVATE_CARD: Deactivate a card
        MANAGE_CARD_TRANSACTION_LIMIT: Set a limit for a card
        MANAGE_CARD_CHANNEL: Manage where card can be used
        CHANGE_CARD_PIN: Change a card's 4digit PIN
        BLOCK_CARD: Block a card
        UNBLOCK_CARD: Unblock a card that was blocked
        GET_BILLERS_BY_TYPE: Get type of bill
        VERIFY_BILL_CUSTOMER: Verify customer's identity
        ADMIN_PURCHASE_BILL: Purchase a bill from ADMIN account
        PURCHASE_BILL: Purchase a bill from Virtual account
        BILL_TSQ: Get status of bill
        ADMIN_GET_PURCHASED_BILLS: Get a list of bills purchased with ADMIN account
        GET_PURCHASED_BILLS: Get a list of bills purchased with Virtual account
        NO_OP: This is a non-existent service type. It's used to for endpoints with
            no service type so as not to alter the already existing API.


    """

    ADMIN_CREATE_VIRTUAL_ACCOUNT = "ADMIN_CREATE_VIRTUAL_ACCOUNT"
    ADMIN_VIRTUAL_ACCOUNTS = "ADMIN_VIRTUAL_ACCOUNTS"
    ADMIN_UPDATE_VIRTUAL_ACCOUNT = "ADMIN_UPDATE_VIRTUAL_ACCOUNT"
    ADMIN_DISABLE_VIRTUAL_ACCOUNT = "ADMIN_DISABLE_VIRTUAL_ACCOUNT"
    ADMIN_ENABLE_VIRTUAL_ACCOUNT = "ADMIN_ENABLE_VIRTUAL_ACCOUNT"
    ADMIN_RETRIEVE_MAIN_ACCOUNT_BALANCE = "ADMIN_RETRIEVE_MAIN_ACCOUNT_BALANCE"
    RETRIEVE_SINGLE_VIRTUAL_ACCOUNT = "RETRIEVE_SINGLE_VIRTUAL_ACCOUNT"
    BANK_LIST = "BANK_LIST"
    NAME_ENQUIRY = "NAME_ENQUIRY"
    SINGLE_FUND_TRANSFER = "SINGLE_FUND_TRANSFER"
    VIRTUAL_ACCOUNT_FUND_TRANSFER = "VIRTUAL_ACCOUNT_FUND_TRANSFER"
    TRANSACTION_STATUS_QUERY = "TRANSACTION_STATUS_QUERY"
    RETRIEVE_VIRTUAL_ACCOUNT_BALANCE = "RETRIEVE_VIRTUAL_ACCOUNT_BALANCE"
    ADMIN_MAIN_ACCOUNT_TRANSACTIONS = "ADMIN_MAIN_ACCOUNT_TRANSACTIONS"
    ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS = (
        "ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS"
    )
    ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS = "ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS"
    ADMIN_VIRTUAL_ACCOUNT_FILTERED_TRANSACTIONS = (
        "ADMIN_VIRTUAL_ACCOUNT_FILTERED_TRANSACTIONS"
    )
    FUND_VIRTUAL_ACCOUNT = "FUND_VIRTUAL_ACCOUNT"
    WITHDRAW_VIRTUAL_ACCOUNT = "WITHDRAW_VIRTUAL_ACCOUNT"
    UPDATE_VIRTUAL_ACCOUNT_LIMIT = "UPDATE_VIRTUAL_ACCOUNT_LIMIT"
    FUND_TRANSFER_INSTRUCTION = "FUND_TRANSFER_INSTRUCTION"
    SEARCH_FUND_TRANSFER_INSTRUCTION = "SEARCH_FUND_TRANSFER_INSTRUCTION"
    RETRIEVE_TRANSACTION_LOGS = "RETRIEVE_TRANSACTION_LOGS"
    GET_GIFT_CARD = "GET_GIFT_CARD"
    ADMIN_BUY_GIFT_CARD = "ADMIN_BUY_GIFT_CARD"
    BUY_GIFT_CARD = "BUY_GIFT_CARD"
    GIFT_CARD_TSQ = "GIFT_CARD_TSQ"
    CREATE_PLAIN_SAVE = "CREATE_PLAIN_SAVE"
    GET_PLAIN_SAVE = "GET_PLAIN_SAVE"
    GET_ALL_CUSTOMER_PLAIN_SAVE = "GET_ALL_CUSTOMER_PLAIN_SAVE"
    PLAIN_SAVE_DEBIT_CREDIT = "PLAIN_SAVE_DEBIT_CREDIT"
    RETRIEVE_PLAIN_SAVE_TRANSACTIONS = "RETRIEVE_PLAIN_SAVE_TRANSACTIONS"
    CREATE_OPEN_FLEXIBLE_SAVE = "CREATE_OPEN_FLEXIBLE_SAVE"
    PRE_CREATE_OPEN_FLEXIBLE_SAVE = "PRE_CREATE_OPEN_FLEXIBLE_SAVE"
    GET_OPEN_FLEXIBLE_SAVE = "GET_OPEN_FLEXIBLE_SAVE"
    GET_ALL_CUSTOMER_OPEN_FLEXIBLE_SAVE = "GET_ALL_CUSTOMER_OPEN_FLEXIBLE_SAVE"
    COMPLETE_OPEN_FLEXIBLE_SAVE_WITHDRAWAL = "COMPLETE_OPEN_FLEXIBLE_SAVE_WITHDRAWAL"
    RETRIEVE_OPEN_FLEXIBLE_SAVE_TRANSACTIONS = (
        "RETRIEVE_OPEN_FLEXIBLE_SAVE_TRANSACTIONS"
    )
    CREATE_FIXED_SAVE = "CREATE_FIXED_SAVE"
    GET_FIXED_SAVE = "GET_FIXED_SAVE"
    GET_ALL_CUSTOMER_FIXED_SAVE = "GET_ALL_CUSTOMER_FIXED_SAVE"
    COMPLETE_FIXED_SAVE_WITHDRAWAL = "COMPLETE_FIXED_SAVE_WITHDRAWAL"
    RETRIEVE_FIXED_SAVE_TRANSACTIONS = "RETRIEVE_FIXED_SAVE_TRANSACTIONS"
    REQUEST_CARD = "REQUEST_CARD"
    GET_CUSTOMER_CARDS = "GET_CUSTOMER_CARDS"
    ACTIVATE_CARD = "ACTIVATE_CARD"
    DEACTIVATE_CARD = "DEACTIVATE_CARD"
    MANAGE_CARD_TRANSACTION_LIMIT = "MANAGE_CARD_TRANSACTION_LIMIT"
    MANAGE_CARD_CHANNEL = "MANAGE_CARD_CHANNEL"
    CHANGE_CARD_PIN = "CHANGE_CARD_PIN"
    BLOCK_CARD = "BLOCK_CARD"
    UNBLOCK_CARD = "UNBLOCK_CARD"
    GET_BILLERS_BY_TYPE = "GET_BILLERS_BY_TYPE"
    VERIFY_BILL_CUSTOMER = "VERIFY_BILL_CUSTOMER"
    ADMIN_PURCHASE_BILL = "ADMIN_PURCHASE_BILL"
    PURCHASE_BILL = "PURCHASE_BILL"
    BILL_TSQ = "BILL_TSQ"
    ADMIN_GET_PURCHASED_BILLS = "ADMIN_GET_PURCHASED_BILLS"
    GET_PURCHASED_BILLS = "GET_PURCHASED_BILLS"
    ADMIN_RETRIEVE_SINGLE_VIRTUAL_ACCOUNT = "ADMIN_RETRIEVE_SINGLE_VIRTUAL_ACCOUNT"
    NO_OP = "NO_OP"
