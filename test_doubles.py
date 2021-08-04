import pytest
from pytest import raises
from unittest.mock import MagicMock
import os


def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("Bad file")

    inline = open(filename, "r")
    line = inline.readline()
    return line


@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


def test_returnsCorrectString(mock_open, monkeypatch):
    mock_exist = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exist)
    result = readFromFile("some")
    mock_open.assert_called_once_with("some", "r")
    assert result == "test line"


def test_throwExceptionWithBadFile(mock_open, monkeypatch):
    mock_exist = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exist)
    with raises(Exception):
        result = readFromFile("some")
