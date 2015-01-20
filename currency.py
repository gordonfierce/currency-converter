def convert(rates, value, from_string, to_string):
    """Given a list of conversion rates, calculate the value of one
    currency (specified in from_string) denominated in another (to_string)"""
    if from_string == to_string:
        return value
    else:
        return basic_convert(rates, value, from_string, to_string)


def basic_convert(rates, value, from_string, to_string):
    rate = [rate for rate in rates if rate[0] == from_string
            and rate[1] == to_string][0]
    return rate[2] * value
