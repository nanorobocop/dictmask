# dictmask - Simple library to mask fields in dict/json

Mask applied on top of your data.
Everything that is not whitelisted - will be removed from dict.
Works with nested dicts and lists.

Usage:

1. Prepare your data

   ```python
   data = {
       "a": "A",
       "b": "B"
   }
   ```

1. Copy your data and prepare mask: True to keep field, False/None to remove

   ```python
   mask = {
       "a": True,
       "b": False
   }
   ```

1. Apply dictmask and check result

    ```python
    dictmask(data, mask)
    {
        "a": "A"
    }
    ```
