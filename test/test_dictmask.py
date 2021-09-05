#!/usr/bin/env python3

import pytest

from ..dictmask import dictmask


@pytest.mark.parametrize(
    "data,mask,masked",
    [
        (
            {"a": "A"},
            {"a": True},
            {"a": "A"},
        ),
        (
            {"a": "A"},
            {"a": False},
            {},
        ),
        (
            {"a": "A"},
            {"a": None},
            {},
        ),
        (
            {"a": {"b": "B"}},
            {"a": {"b": True}},
            {"a": {"b": "B"}},
        ),
        (
            {"a": {"b": "B"}},
            {"a": {"b": False}},
            {"a": {}},
        ),
        (
            {"a": [{"b": "B"}]},
            {"a": [{"b": True}]},
            {"a": [{"b": "B"}]},
        ),
        (
            {"a": [{"b": "B"}]},
            {"a": [{"b": False}]},
            {"a": [{}]},
        ),
        (
            {"a": None},
            {"a": [{"b": False}]},
            {"a": None},
        ),
    ],
)
def test_dictmask(data, mask, masked):
    assert dictmask(data, mask) == masked
