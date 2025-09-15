import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("bedroom", "Bedroom"),
    ("don't worry", "Don't worry"),
    ("rug", "Rug"),
    ("room", "Room"),
    ("living room", "Living room"),
    ("hello Mark", "Hello mark")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    (",but", ",but"),
    ("@ru", "@ru"),
    (":)", ":)")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" London", "London"),
    (" I agree", "I agree"),
    (" Forbidden", "Forbidden"),
    (" Nadezhda", "Nadezhda"),
    (" Thank you", "Thank you"),
    (" You are welcome!", "You are welcome!")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("/   ", "/   "),
    (",but", ",but"),
    ("@ru  ", "@ru  "),
    (": ) ", ": ) ")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    (" London", "L"),
    (" I agree", "a"),
    (" Forbidden", "n"),
    (" Nadezhda", "z"),
    (" Thank you", " "),
    (" You are welcome!", "w")
])
def test_contains(string, symbol):
    assert string_utils.contains(string, symbol) == True

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("123abc", "5"),
    ("", "1"),
    ("/54545   ", "-"),
    (",but", ":"),
    ("@ru  ", "!"),
    (": 8) ", "*")
])
def test_contains(string, symbol):
    assert string_utils.contains(string, symbol) == False

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("London", "L", "ondon"),
    ("I agree", "a", "I gree"),
    ("Forbidden", "n", "Forbidde"),
    ("Nadezhda", "z", "Nadehda"),
    ("Thank you", " ", "Thankyou"),
    ("You are welcome!", "w", "You are elcome!")
])
def test_delete_symbol(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("123abc", "5", "123abc"),
    ("", "1", ""),
    ("/54545   ", "-", "/54545   "),
    (",but", ":", ",but"),
    ("@ru  ", "!", "@ru  "),
    (": 8) ", "*", ": 8) ")
])
def test_delete_symbol(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected