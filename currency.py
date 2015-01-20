def convert(rates, value, from_string, to_string):
    """Given a list of conversion rates, calculate the value of one
    currency (specified in from_string) denominated in another (to_string)"""
    if from_string == to_string:
        return value
    else:
        return basic_convert(rates, value, from_string, to_string)


def conversion_control_structure(rates, value, from_string, to_string):
    if from_string == to_string:
        return value
    elif is_in_rates_forward(from_string, to_string):
        return basic_convert(rates, value, from_string, to_string)
    elif is_in_rates_backward(from_string, to_string):
        return "Well, it ain't work"

def is_in_rates_forward(from_string, to_string):
    pass


def is_in_rates_backward(from_string, to_string):
    return is_in_rates_forward(to_string, from_string)


def basic_convert(rates, value, from_string, to_string):
    rate = [rate for rate in rates if rate[0] == from_string
            and rate[1] == to_string][0]
    return rate[2] * value
