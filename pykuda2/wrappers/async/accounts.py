from pykuda2.base import BaseAsyncAPIWrapper
from pykuda2.utils import ServiceType


class AsyncAccount(BaseAsyncAPIWrapper):
    async def create_virtual_account(
        self,
        email: str,
        phone_number: str,
        last_name: str,
        first_name: str,
        middle_name: str,
        business_name: str,
        tracking_reference: str,
    ):
        """Creates a new virtual account for customers

        Note:
            Ensure that you have updated your BVN on your main account.
        """
        data = {
            "email": email,
            "phoneNumber": phone_number,
            "lastName": last_name,
            "firstName": first_name,
            "middleName": middle_name,
            "businessName": business_name,
            "trackingReference": tracking_reference,
        }
        return await self.api_call(
            service_type=ServiceType.ADMIN_CREATE_VIRTUAL_ACCOUNT, data=data
        )
    async def update_virtual_account(
        self, tracking_reference: str, first_name: str, last_name: str, email: str
    ):
        """Modifies a virtual account data

        Note:
            Good to know: For context, you cannot alter the phone number of the customer.
            You may only alter either the first name/last name or email address tied to
            the account information.
            Do not update the name and the email address together on a single request.
        """
        data = {
            "trackingReference": tracking_reference,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
        return await self.api_call(
            service_type=ServiceType.ADMIN_UPDATE_VIRTUAL_ACCOUNT, data=data
        )
    async def get_virtual_accounts(self, page_size: int, page_number: int):
        """Retrieves your existing virtual accounts"""
        data = {
            "PageSize": page_size,
            "PageNumber": page_number,
        }
        return await self.api_call(service_type=ServiceType.ADMIN_VIRTUAL_ACCOUNTS, data=data)

    async def get_virtual_account(self, tracking_reference: str):
        """Retrieves an existing virtual account"""
        data = {
            "trackingReference": tracking_reference,
        }
        return await self.api_call(
            service_type=ServiceType.ADMIN_RETRIEVE_SINGLE_VIRTUAL_ACCOUNT, data=data
        )

    async def disable_virtual_account(self, tracking_reference: str):
        """Disables a user’s virtual static account.

        Note:
            We encourage Admins and account managers to review accounts and transactions
            frequently. This will avoid situations where a user has an over bloated customer
            database without real customers or helping to reduce the menace of fraudulent transactions.
        """
        data = {
            "trackingReference": tracking_reference,
        }
        return await self.api_call(
            service_type=ServiceType.ADMIN_DISABLE_VIRTUAL_ACCOUNT, data=data
        )

    async def enable_virtual_account(self, tracking_reference: str):
        """Enables a user’s virtual static account."""
        data = {
            "trackingReference": tracking_reference,
        }
        return await self.api_call(
            service_type=ServiceType.ADMIN_ENABLE_VIRTUAL_ACCOUNT, data=data
        )

    async def get_admin_account_balance(self):
        """Retrieves the account balance on your main account."""
        return await self.api_call(
            service_type=ServiceType.ADMIN_RETRIEVE_MAIN_ACCOUNT_BALANCE
        )

    async def get_virtual_account_balance(self, tracking_reference: str):
        """Retrieves the account balance on your virtual account."""
        data = {
            "trackingReference": tracking_reference,
        }
        return await self.api_call(
            service_type=ServiceType.ADMIN_ENABLE_VIRTUAL_ACCOUNT, data=data
        )
