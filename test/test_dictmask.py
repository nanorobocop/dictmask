#!/usr/bin/env python3

"""Tests for dictmask"""

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
    """Test dictmask"""
    assert dictmask(data, mask) == masked


@pytest.mark.parametrize(
    "data,mask,exception",
    [
        (
            {"a": "A"},
            {"a": 1},
            ValueError,
        ),
        (
            {"a": "A"},
            {"a": "A"},
            ValueError,
        ),
        (
            {"a": "A"},
            {"a": [{"b": "B"}]},
            ValueError,
        ),
        (
            {"a": [{"b": "B"}]},
            {"a": [{"b": True}, {"c": True}]},
            ValueError,
        ),
    ],
)
def test_dictmask_exception(data, mask, exception):
    """Test dictmask with negative cases"""
    with pytest.raises(exception):
        assert dictmask(data, mask)
