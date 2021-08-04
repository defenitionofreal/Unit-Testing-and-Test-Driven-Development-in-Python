import pytest

def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        value = "Fizz"
    elif isMultiple(value, 5):
        value = "Buzz"
    return str(value)


def isMultiple(value, mod):
    return (value % mod) == 0


def checkFizzBuzz(value, expected):
    retVal = fizzBuzz(value)
    assert retVal == expected


def test_returns1With1Passes():
    checkFizzBuzz(1, "1")


def test_returns2With1Passes():
    checkFizzBuzz(2, "2")


def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")


def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")


def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")


def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")


def test_returnsFizzBuzzWith15Passed():
    checkFizzBuzz(15, "FizzBuzz")

