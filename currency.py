def convert(rates, value, from_string, to_string):
    """Given a list of conversion rates, calculate the value of one
    currency (specified in from_string) denominated in another (to_string)"""
    rate = conversion_control_structure(rates, from_string, to_string)
    if rate is None:
        pass
    else:
        return round((rate * value), 2)


def conversion_control_structure(rates, from_string, to_string):
    """Determines which sort of currency conversion is needed based on input"""
    if from_string == to_string:
        return 1
    elif is_in_rates_forward_or_backward(rates, from_string, to_string):
        return convert_forward_or_backward(rates, from_string, to_string)
    else:
        pass


def is_in_rates_forward_or_backward(rates, from_string, to_string):
    """Determines if a conversion can be made in one step"""
    return is_in_rates_forward(rates, from_string, to_string) or is_in_rates_backward(
        rates, from_string, to_string
    )


def convert_forward_or_backward(rates, from_string, to_string):
    """Gets a conversion rate between two currencies"""
    if is_in_rates_forward(rates, from_string, to_string):
        return basic_convert(rates, from_string, to_string)
    else:
        return 1 / basic_convert(rates, to_string, from_string)


def is_in_rates_forward(rates, from_string, to_string):
    """Checks to see if there is a conversion rate directly from
    from_string to to_string"""
    from_rates = [rate for rate in rates if rate[0] == from_string]
    for rate in from_rates:
        if rate[1] == to_string:
            return True
    return False


def is_in_rates_backward(rates, from_string, to_string):
    """Checks to see if there is a conversion rate from the to_string to
    the for_string."""
    return is_in_rates_forward(rates, to_string, from_string)


def basic_convert(rates, from_string, to_string):
    """Looks up a conversion rate between two strings we know are in rates"""
    rate = [rate for rate in rates if rate[0] == from_string and rate[1] == to_string][
        0
    ]
    return rate[2]
