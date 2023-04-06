import random


def read_temperature():
    '''
        Simulates a temprature sensor by returning random temperature value
    '''
    return random.randint(-10, 110)


def convert_to(value, unit):
    '''
    Performs a conversion from Celsius to Fahrenheit to Celsius
    :param value:
    :param unit:
    :return:
    '''
    if unit == 'Celsius':
        value_in_celsius = (value - 32) * 5 / 9
        return value_in_celsius
    value_in_fahrenheit = value * 9 / 5 + 32
    return value_in_fahrenheit
