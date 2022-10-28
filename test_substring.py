from substring import length_of_longest_substring


def test_substring_of_three():
    assert length_of_longest_substring("abcabcbb") == 3


def test_substring_of_one():
    assert length_of_longest_substring("bbbbb") == 1


def test_substring_of_zero():
    assert length_of_longest_substring("") == 0
