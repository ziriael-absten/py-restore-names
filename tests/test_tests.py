from typing import List

import pytest

from app import restore_names


def test_restore_only_missing_names(monkeypatch):
    def restore_only_missing_names(users: List[dict]) -> None:
        for user in users:
            if "first_name" not in user:
                user["first_name"] = user["full_name"].split()[0]

    monkeypatch.setattr(restore_names, "restore_names", restore_only_missing_names)

    test_result = pytest.main(["app/test_restore_names.py"])
    assert (
        test_result.value == 1
    ), "Function 'restore_only_missing_names' shouldn't pass all tests"


def test_restore_only_none_names(monkeypatch):
    def restore_only_none_names(users: List[dict]) -> None:
        for user in users:
            if user["first_name"] is None:
                user["first_name"] = user["full_name"].split()[0]

    monkeypatch.setattr(restore_names, "restore_names", restore_only_none_names)

    test_result = pytest.main(["app/test_restore_names.py"])
    assert (
        test_result.value == 1
    ), "Function 'restore_only_none_names' shouldn't pass all tests"
