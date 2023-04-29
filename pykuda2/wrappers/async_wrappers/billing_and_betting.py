from typing import Optional

from pykuda2.base import BaseAsyncAPIWrapper
from pykuda2.utils import BillType, ServiceType, APIResponse


class AsyncBillingAndBetting(BaseAsyncAPIWrapper):
    async def get_bill_type_options(
        self, bill_type: BillType, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieves all the options of a bill type that are available from Kuda.

        Args:
            bill_type: The bill type we want to get the options available for e.g.
                BillType.INTERNET_DATA, BillType.CABLE_TV
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {"BillTypeName": bill_type}
        return await self._api_call(
            service_type=ServiceType.GET_BILLERS_BY_TYPE,
            data=data,
            request_reference=request_reference,
        )

    async def verify_customer_before_purchase(
        self,
        tracking_reference: str,
        kuda_bill_item_identifier: str,
        customer_identification: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Verifies the identity of  the beneficiary.

        Just like an account or bank transfer, You need to verify a customer's identity before
        successfully initiating a bill purchase instance. This way you reduce the issue of theft
        or erroneous bill payments which are hard to retrieve.
        You don't need to verify the customer if the bill type is airtime


        Args:
            tracking_reference: Customer's wallet identifier.
            kuda_bill_item_identifier: The Kuda bill unique identifier.
            customer_identification: The customer's unique identifier.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "TrackingRef": tracking_reference,
            "KudaBillItemIdentifier": kuda_bill_item_identifier,
            "CustomerIdentification": customer_identification,
        }
        return await self._api_call(
            service_type=ServiceType.VERIFY_BILL_CUSTOMER,
            data=data,
            request_reference=request_reference,
        )

    async def purchase_bill(
        self,
        amount: int,
        bill_item_identifier: str,
        customer_identifier: str,
        phone_number: Optional[str] = None,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Purchase a bill from your main account.

        Args:
            amount: Bill amount.
            bill_item_identifier: The Kuda bill unique identifier
            customer_identifier: The customer's unique identifier
            phone_number: The customer's phone number It is not required
                if you're purchasing airtime.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "Amount": amount,
            "BillItemIdentifier": bill_item_identifier,
            "PhoneNumber": phone_number,
            "CustomerIdentifier": customer_identifier,
        }
        return await self._api_call(
            service_type=ServiceType.ADMIN_PURCHASE_BILL,
            data=data,
            request_reference=request_reference,
        )

    async def purchase_bill_from_virtual_account(
        self,
        tracking_reference: str,
        amount: int,
        bill_item_identifier: str,
        phone_number: str,
        customer_identifier: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Purchase a bill from your virtual account.

        Args:
            tracking_reference: The customer virtual account Identifier.
            amount: Bill amount.
            bill_item_identifier: The Kuda bill unique identifier
            customer_identifier: The customer's unique identifier
            phone_number: The customer's phone number It is not required
                if you're purchasing airtime.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "Amount": amount,
            "BillItemIdentifier": bill_item_identifier,
            "PhoneNumber": phone_number,
            "CustomerIdentifier": customer_identifier,
            "TrackingReference": tracking_reference,
        }
        return await self._api_call(
            service_type=ServiceType.PURCHASE_BILL,
            data=data,
            request_reference=request_reference,
        )

    async def get_bill_purchase_status(
        self,
        bill_request_ref: Optional[str],
        bill_response_reference: Optional[str],
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieve the status of a bill purchase.

        Args:
            bill_response_reference: The bill reference gotten from purchasing the bill.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        if bill_response_reference and bill_request_ref:
            raise ValueError(
                "Both `bill_response_reference` and `bill_request_ref` should"
                " not be provided. Please provide any but not both"
            )
        data = {
            "BillResponseReference": bill_response_reference,
            "BillRequestRef": bill_request_ref,
        }
        return await self._api_call(
            service_type=ServiceType.BILL_TSQ,
            data=data,
            request_reference=request_reference,
        )

    async def get_purchased_bills(
        self, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieve bills purchased from the main account.

        Args:
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        return await self._api_call(
            service_type=ServiceType.ADMIN_GET_PURCHASED_BILLS,
            request_reference=request_reference,
        )

    async def get_purchased_bill_from_virtual_account(
        self, tracking_reference: str, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieve bills purchased from a virtual account.

        Args:
            tracking_reference: The unique identifier of the virtual account.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {"TrackingReference": tracking_reference}
        return await self._api_call(
            service_type=ServiceType.GET_PURCHASED_BILLS,
            data=data,
            request_reference=request_reference,
        )
