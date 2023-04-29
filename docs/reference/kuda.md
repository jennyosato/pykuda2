::: pykuda2.kuda

## Attributes on the `Kuda` and  `AsyncKuda` classes
The wrapper classes `Kuda` and `AsyncKuda` classes have methods bounded to them that provides methods that lets you
interact with Kuda. Here's a comprehensive list of those attributes.


| Attribute             | Description                                                                                                                                                                       | Example                                          |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| `accounts`            | Provides methods that let's you interact with [Kuda's Account API](https://kuda.notion.site/Accounts-c5069c45cb414ddfa4be40fdbce3977c)                                            | `kuda.accounts.get_admin_account_balance()`      |
| `transactions`        | Provides methods that let's you interact with [Kuda's Account Transactions API](https://kuda.notion.site/Account-Transactions-80fb16f4aca843a1a63bba835123f3a6)                   | `kuda.transactions.get_banks()`                  |
| `billing_and_betting` | Provided methods that let's you interact with [Kuda's Bill Payments & Betting Services](https://kuda.notion.site/Bill-Payments-Betting-Services-cd1008366ab2477bb8fa36350a1e2945) | `kuda.billing_and_betting.get_purchased_bills()` |
| `gift_cards`          | Provides methods that let's you interact with [Kuda's Gift Cards API](https://kuda.notion.site/Gift-Cards-9eaeccd55bbf41d1bb309b97123e7af9)                                       | `kuda.gift_cards.get_gift_cards()`                                   |
| `savings`             | Provides methods that let's you interact with [Kuda's Savings API](https://kuda.notion.site/Kuda-Savings-881f221fa3ba4fef998278e8cf2c56f9)                                        | `kuda.savings.get_fixed_savings_account(tracking_reference="12343443435")` |
| `cards`               | Provides methods that let's you interact with [Kuda's Cards API](https://kuda.notion.site/Kuda-Cards-9c17c1ab4ae14d1bb2aaee40f56e3d56)                                            | `kuda.cards.get_cards(tracking_reference="24232244")`                             |

```py title="Using a class attribute on the Kuda class to interact with Kuda"
import os
from pykuda2 import Kuda

KUDA_EMAIL_ADDRESS = os.getenv("KUDA_EMAIL_ADDRESS")
KUDA_API_KEY = os.getenv("KUDA_API_KEY")

# You instantiate the wrapper classes
kuda = Kuda(email=KUDA_EMAIL_ADDRESS, api_key=KUDA_API_KEY)

# calling a method by accessing the attributes on `kuda`
response = kuda.accounts.get_admin_account_balance()
print(response)
```

```py title="What the async equivalent might look like"
import asyncio
import os
from pykuda2 import AsyncKuda

KUDA_EMAIL_ADDRESS = os.getenv("KUDA_EMAIL_ADDRESS")
KUDA_API_KEY = os.getenv("KUDA_API_KEY")

# You instantiate the wrapper classes
async_kuda = AsyncKuda(email=KUDA_EMAIL_ADDRESS, api_key=KUDA_API_KEY)

# The bounded attributes have the same name for the async equivalent of the `Kuda` wrapper
async def print_admin_balance():
    print(await async_kuda.accounts.get_admin_account_balance())

coroutines = asyncio.gather(print_admin_balance())
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutines)
```