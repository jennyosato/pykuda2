from pykuda2 import Mode, ServiceType, APIResponse
from pykuda2.base import BaseAsyncAPIWrapper
from pykuda2.exceptions import TokenException


class AsyncInstantSettlementService(BaseAsyncAPIWrapper):
    def __init__(self, secret_key: str, client_password: str, mode=Mode.DEVELOPMENT):
        super().__init__(email="", api_key="", mode=mode)
        self.secret_key = secret_key
        self.client_password = client_password

    @property
    def _base_url(self) -> str:
        """Returns the base url.

        The url returned depends on the mode in which the class was instantiated."""
        return {
            Mode.DEVELOPMENT: "https://partners-uat.kudabank.com",
            Mode.PRODUCTION: "https://partners.kuda.com",
        }[self._mode]

    @property
    async def _token(self) -> str:
        if self._token:
            return self._token
        else:
            response = await self._api_call(
                service_type=ServiceType.NO_OP,
                data={
                    "secretKey": self.secret_key,
                    "clientPassword": self.client_password,
                },
                endpoint_path="/api/Auth/authenticate",
                exclude_auth_header=True,
            )
            if response.data:
                self._token = response.data["auth_token"]
                return self._token
            raise TokenException(
                f"Unable to get access token for InstantSettlementService. {response.message}. Please ensure valid credentials were provided"
            )

    async def create_terminal(
        self,
        terminal_id: str,
        merchant_id: str,
        kuda_account_number: int,
        serial_number: str,
        is_receiving_payment: bool,
        is_active: bool,
    ) -> APIResponse:
        """Gives the partner the ability to add certain parameters to a POS device.

        It allows the partner to anchor routing communications between the processor and the Kuda settlement system.

        Args:
            terminal_id: The terminal identifier.
            merchant_id: The merchant identifier.
            kuda_account_number: The client's Kuda account number.
            serial_number: The serial number.
            is_receiving_payment: Set to `True` for receiving payment or `False` for otherwise.
            is_active: Set to `True` for an active terminal or `False` for otherwise.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        payload = {
            "terminalId": terminal_id,
            "merchantId": merchant_id,
            "kudaAccountNumber": kuda_account_number,
            "serialNumber": serial_number,
            "isReceivingPayment": is_receiving_payment,
            "isActive": is_active,
        }
        return await self._api_call(
            service_type=ServiceType.NO_OP,
            data=payload,
            endpoint_path="/api/terminal/api/terminal/createterminal",
        )

    async def update_terminal(
        self,
        kuda_merchant_id: str,
        terminal_id: str,
        kuda_account_number: int,
        kuda_account_name: str,
        serial_number: str,
        is_active: bool,
        is_receiving_payment: bool,
        fee_percentage: float,
        date_created: str,
    ) -> APIResponse:
        """Allows a partner to swap the location and user of a POS device.

        Args:
            kuda_merchant_id: The client's Kuda merchant identifier
            terminal_id: The  terminal unique identifier
            kuda_account_number: The client's Kuda account number
            kuda_account_name: The client's account name
            serial_number: The terminal's serial number
            is_active: Set to `True` for an active terminal or otherwise.
            is_receiving_payment: Set to `True` if the terminal is receiving payment else otherwise.
            fee_percentage: Fee percentage
            date_created: The date the terminal was created

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        payload = {
            "id": id,
            "kudaMerchantId": kuda_merchant_id,
            "terminalId": terminal_id,
            "kudaAccountNumber": kuda_account_number,
            "kudaAccountName": kuda_account_name,
            "serialNumber": serial_number,
            "isActive": is_active,
            "isReceivingPayment": is_receiving_payment,
            "feePercentage": fee_percentage,
            "dateCreated": date_created,
        }
        return await self._api_call(
            service_type=ServiceType.NO_OP,
            data=payload,
            endpoint_path="/api/terminal/EditTerminal",
        )

    async def all(self, page_size: int, page_number: int) -> APIResponse:
        """Allows a user to get all merchants and the terminals assigned to them.

        Args:
            page_size: This specifies the maximum number of terminals to be retrieved.
            page_number: This specifies the index of the paginated results retrieved.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        payload = {"pageSize": page_size, "pageNumber": page_number}
        return await self._api_call(
            service_type=ServiceType.NO_OP,
            data=payload,
            endpoint_path="/RetrieveMerchantTerminals",
        )

    async def get_settlement_status(self, transaction_id: str) -> APIResponse:
        """Retrieves insight on the status of a particular/all settlements for a terminal.

        Args:
            transaction_id: The transaction reference number or unique identifier.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        payload = {"transactionId": transaction_id}
        return await self._api_call(
            service_type=ServiceType.NO_OP,
            data=payload,
            endpoint_path="/api/terminal/settlementstatus",
        )

    async def log_transaction(self, amount: int, transaction_id: str, terminal_id: str) -> APIResponse:
        """Logs a complete transaction.

        For complete transaction fulfilment, a user will call this method with the transaction amount
        that needs to be fulfilled. This way, the terminal management system is updated with the transaction
        status in real-time and completes settlement to the specified user's account.

        Logging a transaction sends a notification to Kuda which triggers instant settlement.

        Args:
            amount: The transaction amount.
            transaction_id: The transaction reference number or unique identifier.
            terminal_id: The terminal unique identifier.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        payload = {
            "amount": amount,
            "transactionId": transaction_id,
            "terminalId": terminal_id,
        }
        return await self._api_call(
            service_type=ServiceType.NO_OP,
            data=payload,
            endpoint_path="/api/terminal/logtransaction",
        )

    async def transactions(
        self, terminal_id: str, from_: str, to: str, page_size: int, page_number: int
    ) -> APIResponse:
        """Retrieves transactions.

        This method allows a user to do back office operations while searching for transactions disputes.

        Args:
            terminal_id: The terminal unique identifier
            from_: The start date
            to: The end date
            page_size: This specifies the maximum number of transactions to be retrieved.
            page_number: This specifies the index of the paginated results retrieved.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        payload = {
            "terminalId": terminal_id,
            "dateFrom": from_,
            "dateTo": to,
            "pageSize": page_size,
            "pageNumber": page_number,
        }
        return await self._api_call(
            service_type=ServiceType.NO_OP,
            data=payload,
            endpoint_path="/api/terminal/searchtransaction",
        )
