import pytest
from redact import redact


words = ['a', 'b', 'c', 'c', 'd', 'e']
banned = ['d']


def test_redact():
    red = redact(words, banned)
    assert redact(words, banned) == ['a', 'b', 'c', 'c', 'e']
    assert len(redact(words, banned))== 5
    assert red[0] == 'a'
