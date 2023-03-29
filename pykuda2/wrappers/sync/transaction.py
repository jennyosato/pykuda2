from pykuda2.base import APIWrapper, ServiceType


class Transaction(APIWrapper):
    def get_banks(self):
        """ Gets all the bank list from NIPS
         Note: 
              In production, the list of banks and bank codes may change based on the responses gotten from NIBSS.
            """
        return self.api_call(service_type=ServiceType.BANK_LIST)
    
    def confirm_transfer_recipient(self, beneficiary_account_number:str, beneficiary_bank_code: str, sender_tracking_reference: str, is_request_from_virtual_account:str ):
        """ 
        Retrieve the name linked to a bank account
        """
        data = {
            "beneficiaryAccountNumber": beneficiary_account_number,
            "beneficiaryBankCode": beneficiary_bank_code,
            "SenderTrackingReference": sender_tracking_reference,
            "isRequestFromVirtualAccount": is_request_from_virtual_account
        }
        return self.api_call(service_type=ServiceType.NAME_ENQUIRY, data=data)
    def fund_transfer(self, tracking_reference:str, beneficiary_account:str, beneficiary_bank_code: str, beneficiary_name: str, amount: int, narration: str, name_enquiry_session_id:str, sender_name:str, client_fee_charge:int):
        """ 
        Transfer money from your main account
        ---Please, do not use sensitive data while doing test transactions so as not to save it in your sandbox environment.
          """
        data = {
    #   "ClientAccountNumber": client_account_number,
      "beneficiarybankCode": beneficiary_bank_code,
      "beneficiaryAccount": beneficiary_account,
      "beneficiaryName": beneficiary_name,
      "amount": amount,
      "narration": narration,
      "nameEnquirySessionID": name_enquiry_session_id,
      "trackingReference": tracking_reference,
      "senderName": sender_name,
      "clientFeeCharge": client_fee_charge
		}
        return self.api_call(service_type=ServiceType.SINGLE_FUND_TRANSFER, data=data)
    
    def virtual_fund_transfer(self, tracking_reference: str, beneficiary_account: str, amount: int, beneficiary_name:str, narration: str, beneficiary_bank_code: str, sender_name:str, name_enquiry_id: str, client_fee_charge: int):
        """ Transfer money from a virtual account """
        data =  {
      "trackingReference": tracking_reference,
      "beneficiaryAccount": beneficiary_account,
      "amount": amount,
      "beneficiaryName": beneficiary_name,
      "narration": narration,
      "beneficiaryBankCode": beneficiary_bank_code,
      "senderName": sender_name,
      "nameEnquiryId": name_enquiry_id,
	  "clientFeeCharge": client_fee_charge
    }
        return self.api_call(service_type=ServiceType.VIRTUAL_ACCOUNT_FUND_TRANSFER, data=data)
    
    def transfer_instructions(self, fund_transfer_instructions: object, account_number: str, account_name: str, beneficiary_bank_code: str, amount: str, bank_code:str, narration: str, bank_name: str, long_code: str, reference: str):
        
        data = {
            "FundTransferInstructions": fund_transfer_instructions 
        }
        fund_transfer_instructions = [
					{
						"AccountNumber": account_number,
						"AccountName":account_name,
						"BeneficiaryBankCode":beneficiary_bank_code,
						"Amount":amount,                 
						"BankCode":bank_code,
						"Narration":narration,
						"BankName":bank_name,
						"LongCode":long_code,
						"Reference":reference        
					}]
        return self.api_call(service_type=ServiceType.FUND_TRANSFER_INSTRUCTION, data=data)
    
    def search_instruction(self, account_number:str, reference: str, amount: str, original_request_ref:str, status:str, page_number: str, page_size: str):
        data = {
                "AccountNumber": account_number, 
				"Reference": reference, 
				"Amount": amount, 
				"OriginalRequestRef": original_request_ref,
				"Status": status, 
				"PageNumber": page_number,
				"PageSize": page_number
        }
        return self.api_call(service_type=ServiceType.SEARCH_FUND_TRANSFER_INSTRUCTION, data=data)
    
    def transaction_logs(self, request_reference: str,response_reference: str, transaction_date: str, has_transaction_date_range_filter:str,start_date:str, end_date:str, page_size:str, page_number: str):
        data = {
             "RequestReference": request_reference,
             "ResponseReference": response_reference,
	         "TransactionDate": transaction_date,
             "HasTransactionDateRangeFilter": has_transaction_date_range_filter,
             "StartDate": start_date,
             "EndDate": end_date,
             "PageSize": page_size,
             "PageNumber": page_number
        }
        return self.api_call(service_type=ServiceType.RETRIEVE_TRANSACTION_LOGS, data=data)
    
    def transaction_history(self, page_size: str, page_number:str):
        data = {
             "pageSize": page_size,
             "pageNumber": page_number
        }
        return self.api_call(service_type=ServiceType.ADMIN_MAIN_ACCOUNT_TRANSACTIONS, data=data)
   
    def filtered_transaction_history(self, page_size:str, page_number: str, start_date:str, end_date: str):
        data = {
          "pageSize": page_size,
          "pageNumber": page_number,
		  "startDate": start_date,
          "endDate": end_date
        }
        return self.api_call(service_type=ServiceType.ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS, data=data)
    
    def virtual_transaction_history(self, page_size: str, page_number:str, tracking_reference:str):
        data = {
             "trackingReference": tracking_reference,
             "pageSize": page_size,
             "pageNumber": page_number
        }
        return self.api_call(service_type=ServiceType.ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS, data=data)
   
    def virtual_filtered_transaction_history(self, page_size:str, page_number: str, start_date:str, end_date: str, tracking_reference:str):
        data = {
          "trackingReference": tracking_reference,
          "pageSize": page_size,
          "pageNumber": page_number,
		  "startDate": start_date,
          "endDate": end_date
        }
        return self.api_call(service_type=ServiceType.ADMIN_VIRTUAL_ACCOUNT_FILTERED_TRANSACTIONS, data=data)
    def transaction_status(self, is_third_party_bank_transfer: str, transaction_request_reference:str):
        data = {
          "isThirdPartyBankTransfer": is_third_party_bank_transfer,
          "transactionRequestReference": transaction_request_reference
        }
        return self.api_call(service_type=ServiceType.TRANSACTION_STATUS_QUERY, data=data)
    def fund_virtual_account(self, tracking_reference: str, amount: str, narration:str):
        data = {
          "trackingReference": tracking_reference,
          "amount": amount,
          "narration": narration
        }
        return self.api_call(service_type=ServiceType.FUND_VIRTUAL_ACCOUNT, data=data)
    
    def withdraw_from_virtual_account(self, tracking_reference:str, amount:int, narration: str, client_fee_charge:int):
        data = {
             "trackingReference": tracking_reference,
             "amount": amount,
             "narration": narration,
             "ClientFeeCharge": client_fee_charge
        }
        return self.api_call(service_type=ServiceType.WITHDRAW_VIRTUAL_ACCOUNT, data=data)