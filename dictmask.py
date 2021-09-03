#!/usr/bin/env python3

"""
dictmask masks dictionary data based on mask
"""


def dictmask(data, mask, missing_keep=False):
    """dictmask masks dictionary data based on mask"""

    if not isinstance(data, dict):
        raise ValueError("First argument with data should be dictionary")
    if not isinstance(mask, dict):
        raise ValueError("Second argument with mask should be dictionary")
    if not isinstance(missing_keep, bool):
        raise ValueError("Argument missing_keep should be bool type")

    res = {}
    for k, v in data.items():
        if k not in mask:
            if missing_keep is True:
                res[k] = v
            continue

        if mask[k] is True:
            res[k] = v
            continue

        if mask[k] is None or mask[k] is False:
            continue

        if isinstance(data[k], dict) and isinstance(mask[k], dict):
            res[k] = dictmask(data[k], mask[k])
            continue

        if isinstance(data[k], list) and isinstance(mask[k], list):
            if len(mask[k]) != 1:
                ValueError("Mask inside list should have only one item")
            res2 = []
            for i in range(len(data[k])):
                res2.append(dictmask(data[k][i], mask[k][0], missing_keep))
            res[k] = res2
        else:
            raise ValueError(
                "Cannot proceed values with different types",
                type(data),
                type(mask),
            )
    return res
