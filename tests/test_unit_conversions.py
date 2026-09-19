from unit_converter import show_menu, main

def test_show_menu(capsys):
    show_menu()

    captured = capsys.readouterr()

    assert "UNIT CONVERTER" in captured.out
    assert "==============" in captured.out
    assert "1. Kilometres to Miles" in captured.out
    assert "2. Miles to Kilometres" in captured.out
    assert "3. Celsius to Fahrenheit" in captured.out
    assert "4. Fahrenheit to Celsius" in captured.out
    assert "5. Kilograms to Pounds" in captured.out
    assert "6. Pounds to Kilograms" in captured.out
    assert "7. Litres to Gallons" in captured.out
    assert "8. Gallons to Litres" in captured.out
    assert "9. Show History" in captured.out
    assert "10. Clear History" in captured.out
    assert "11. Quit" in captured.out

def test_main_quit(monkeypatch, capsys):
     monkeypatch.setattr("builtins.input", lambda _: "11")

     main()

     captured = capsys.readouterr()

     assert "Goodbye!" in captured.out

def test_main_invalid_option(monkeypatch, capsys):
     inputs = iter(["abc", "12", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert captured.out.count("Invalid Option") == 2
     assert "Goodbye!" in captured.out


# Next I need to test the individual functions in the menu from pressing 1 through to entering a conversion, and getting the right result, then quitting the programme.

def test_main_kilometres_to_miles(monkeypatch, capsys):
     inputs = iter(["1", "10", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert "10 km = 6.21 miles" in captured.out
     assert "Goodbye!" in captured.out

def test_main_miles_to_kilometres(monkeypatch, capsys):
     inputs = iter(["2", "10", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert "10 miles = 16.00 km" in captured.out
     assert "Goodbye!" in captured.out

def test_main_celsius_to_fahrenheit(monkeypatch, capsys):
     inputs = iter(["3", "100", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert "100 C = 212.00 F" in captured.out
     assert "Goodbye!" in captured.out

def test_main_fahrenheit_to_celsius(monkeypatch, capsys):
     inputs = iter(["4", "32", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert "32 F = 0.00 C" in captured.out
     assert "Goodbye!" in captured.out

def test_main_kilograms_to_pounds(monkeypatch, capsys):
     inputs = iter(["5", "10", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert "10 kg = 22.05 lbs" in captured.out
     assert "Goodbye!" in captured.out

def test_main_pounds_to_kilograms(monkeypatch, capsys):
     inputs = iter(["6", "10", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert "10 lbs = 4.54 kg" in captured.out
     assert "Goodbye!" in captured.out

def test_main_litres_to_gallons(monkeypatch, capsys):
     inputs = iter(["7", "10", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert "10 L = 2.20 gal" in captured.out
     assert "Goodbye!" in captured.out

def test_main_gallons_to_litres(monkeypatch, capsys):
     inputs = iter(["8", "10", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert "10 gal = 45.46 L" in captured.out
     assert "Goodbye!" in captured.out

def test_main_show_history(monkeypatch, capsys):
     inputs = iter(["1", "10", "", "9", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert captured.out.count("10 km = 6.21 miles") == 2
     assert "CONVERSION HISTORY" in captured.out
     assert "Goodbye!" in captured.out

def test_main_show_clear_history(monkeypatch, capsys):
     inputs = iter(["1", "10", "", "9", "", "10", "", "9", "", "11"])

     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     main()

     captured = capsys.readouterr()

     assert captured.out.count("10 km = 6.21 miles") == 2
     assert "CONVERSION HISTORY" in captured.out
     assert "Conversion history cleared." in captured.out
     assert "No conversions yet."
     assert "Goodbye!" in captured.out