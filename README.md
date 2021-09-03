# dictmask - Simple library to mask fields in dict/json

Mask applied on top of your data.
Everything that is not whitelisted - will be removed from dict.
Works for nested dicts and lists.

Usage:

1. Prepare your data

   ```python
   data = {
       "a": "A",
       "b": "B"
   }
   ```

1. Copy your data and mask: True for keep, False/None to remove

   ```python
   data = {
       "a": True,
       "b": False
   }
   ```

1. Apply dictmask and check result

    ```python
    dictmask(data, mask)
    data = {
        "a": "A"
    }
    ```
