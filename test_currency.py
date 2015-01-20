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


def test_is_in_rates_forward():
    assert cur.is_in_rates_forward(rates, "USD", "EUR")
    assert cur.is_in_rates_forward(rates, "BTC", "USD")
    assert not cur.is_in_rates_forward(rates, "USD", "BTC")
    assert not cur.is_in_rates_forward(rates, "EUR", "USD")


def test_is_in_rates_backward():
    assert cur.is_in_rates_backward(rates, "EUR", "USD")
    assert cur.is_in_rates_backward(rates, "USD", "BTC")
    assert not cur.is_in_rates_backward(rates, "USD", "EUR")


def test_many_tuples_both_ways():
    rates = [("USD", "EUR", 0.86), ("BTC", "USD", 212.86),
             ("EUR", "GBP", 0.76)]
    assert cur.convert(rates, 2, "USD", "BTC") == 0.01
    assert cur.convert(rates, 4, "GBP", "EUR") == 5.26
    assert cur.convert(rates, 4, "EUR", "GBP") == 3.04
    assert cur.convert(rates, 5, "BTC", "USD") == 1064.3
