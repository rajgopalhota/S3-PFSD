import pytest


def raja(x):
    return x + 1


def test_sample():
    assert raja(7) == 49
    assert raja(8) == 9