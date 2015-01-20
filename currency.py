def convert(rates, value, from_string, to_string):
    """Given a list of conversion rates, calculate the value of one
    currency (specified in from_string) denominated in another (to_string)"""
    rate = conversion_control_structure(rates, from_string, to_string)
    if rate is None:
        pass
    else:
        return round((rate * value), 2)


def conversion_control_structure(rates, from_string, to_string):
    if from_string == to_string:
        return 1
    elif is_in_rates_forward(rates, from_string, to_string):
        return basic_convert(rates, from_string, to_string)
    elif is_in_rates_backward(rates, from_string, to_string):
        return 1 / basic_convert(rates, to_string, from_string)
    else:
        pass


def is_in_rates_forward(rates, from_string, to_string):
    from_rates = [rate for rate in rates if rate[0] == from_string]
    for rate in from_rates:
        if rate[1] == to_string:
            return True
    return False


def is_in_rates_backward(rates, from_string, to_string):
    return is_in_rates_forward(rates, to_string, from_string)


def basic_convert(rates, from_string, to_string):
    rate = [rate for rate in rates if rate[0] == from_string
            and rate[1] == to_string][0]
    return rate[2]
