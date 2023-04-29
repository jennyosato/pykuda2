This tries to be a comprehensive explanation of how `pykuda2` works internally. 
Most of the classes, functions or variables in `pykuda2` that you'll ever need in your
project has been exposed in the package level, so you'll rarely need to transverse the project structure to get
what you need.

Here's the structure of the project.
```bash
$ tree pykuda2
├── base.py
├── exceptions.py
├── __init__.py
├── kuda.py
├── utils.py
└── wrappers
    ├── async_wrappers
    │   ├── accounts.py
    │   ├── billing_and_betting.py
    │   ├── card.py
    │   ├── gift_card.py
    │   ├── __init__.py
    │   ├── instant_settlement_service.py
    │   ├── savings.py
    │   └── transaction.py
    ├── __init__.py
    └── sync_wrappers
        ├── accounts.py
        ├── billing_and_betting.py
        ├── card.py
        ├── gift_card.py
        ├── __init__.py
        ├── instant_settlement_service.py
        ├── savings.py
        └── transaction.py

```
So for example even though `TransferInstruction` or `CardChannel` classes live in the `pykuda2.utils.py`
you can import them link this
```python
from pykuda2 import TransferInstruction, CardChannel
```
instead of this
```python
from pykuda2.utils import TransferInstruction, CardChannel
```