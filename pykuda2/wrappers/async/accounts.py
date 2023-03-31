from pykuda2.base import AsyncAPIWrapper
from pykuda2.utils import ServiceType


class AsyncAccount(AsyncAPIWrapper):
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
