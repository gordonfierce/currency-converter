import currency as cur


rates = [("USD", "EUR", 0.86), ("BTC", "USD", 212.86)]

def test_convert_to_same():
    assert cur.convert(rates, 1, "USD", "USD") == 1
