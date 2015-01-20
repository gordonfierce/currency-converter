import currency as cur


rates = [("USD", "EUR", 0.86), ("BTC", "USD", 212.86)]


def test_convert_to_same():
    assert cur.convert(rates, 1, "USD", "USD") == 1
    assert cur.convert(rates, 10, "USD", "USD") == 10


def test_convert_from_one_to_another():
    assert cur.convert(rates, 1, "USD", "EUR") == 0.86


def test_convert_with_different_values():
    assert cur.convert(rates, 10, "USD", "EUR") == 8.6


def test_convert_both_ways():
    assert cur.convert(rates, 1, "EUR", "USD") == 1.16

    
