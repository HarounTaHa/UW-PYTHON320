from unittest.mock import patch, Mock
import queue

import pytest

import patch_tutorial2 as PT2


@patch('patch_tutorial.temperature_sensor.read_temperature', Mock(side_effect=(75, 10, -1)))
def get_current_temperature():
    expected_queue = queue.Queue()
    expected_queue.put('Nice temperature 75F!')
    expected_queue.put("Tough weather, 10F")

    assert PT2.get_current_temperature() == expected_queue.get()
    assert PT2.get_current_temperature() == expected_queue.get()

    with pytest.raises(SystemError):
        PT2.get_current_temperature()


@patch('patch_tutorial2.temperature_sensor.convert_to')
def test_perform_conversion_C_to_F(mocked_function):
    mocked_function.return_value = 32
    result = PT2.perform_conversion(0, 'Fahrenheit')
    assert result == 'A reading of 0 degrees Celsius is equivalent to 32 degrees Fahrenheit'
