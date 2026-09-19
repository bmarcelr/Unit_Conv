import pytest

from helpers import get_number, display_results, show_history, clear_history

# monkeypatch fakes user input when an input is needed, i.e. number or enter ("")

def test_get_number_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "12.5")

    result = get_number("Enter a number: ")

    assert result == 12.5

def test_get_number_invalid_then_valid(monkeypatch):
    inputs = iter(["abc", "12.5"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_number("Enter a number: ")

    assert result == 12.5

def test_get_number_rejects_negative(monkeypatch):
    inputs = iter(["-5", "10"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_number("Enter a number: ")

    assert result == 10

def test_get_number_accepts_negative(monkeypatch):
    inputs = iter(["-5", "10"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_number("Enter a number: ", allow_negative=True)

    assert result == -5

def test_display_result_adds_to_history():
    history = []

    display_results(10, "km", 6.21371, "miles", history)

    assert history == ["10 km = 6.21 miles"]

# capsys captures code printed to the terminal, in this case what is spat out of show_history

def test_show_history_with_items(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "")

    history = [
        "10 km = 6.21 miles",
        "5 kg = 11.02 pounds"
    ]

    show_history(history)

    captured = capsys.readouterr()

    assert "10 km = 6.21 miles" in captured.out
    assert "5 kg = 11.02 pounds" in captured.out

def test_show_history_no_items(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "")
    
    history = []

    show_history(history)

    captured = capsys.readouterr()

    assert "No conversions yet." in captured.out


def test_clear_test_history(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")

    history = ["10 km = 6.21 miles"]

    clear_history(history)

    assert history == []

print("All tests passed!")