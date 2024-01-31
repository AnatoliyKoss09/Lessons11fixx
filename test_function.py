import pytest
import function as f


# 1
def test_print_text():
    expected_result = ("“Don't let the noise of others\n"
                       "       opinions drown out your\n"
                       "                own inner voice.”\n"
                       "                        Steve Jobs")
    assert f.print_text() == expected_result


# 2
def test_check_number_valid_input():
    assert f.check_number2(12, 20) == 'Programm completed' != [
        '12 Paired number!', '13 Not Paired number!', '14 Paired number!',
        '15 Not Paired number!', '16 Paired number!', '17 Not Paired number!',
        '18 Paired number!', '19 Not Paired number!', '20 Paired number!'
    ]


def test_check_number_invalid_input():
    assert f.check_number2('12', 20) == ['Invalid Data']


def test_check_number_program_completed():
    assert f.check_number2(1, 5) == "Programm completed"


# 3

def test_lines_symbol_valid():
    assert f.lines_symbol(3, "vertical", "*") == "*\n*\n*\n"

    assert f.lines_symbol(3, "horizontal", "@") == "@@@"


def test_lines_symbol_invalid():
    assert f.lines_symbol(3, "vertical", "*") == "**"


# 4
def test_max_number_valid():
    assert f.max_number(3, 2, 5, 2) == 5


def test_max_number_invalid():
    assert f.max_number(3, 2, 5, 2) == 2


def test_max_number_zero():
    assert f.max_number(0, 0, 0, 0) == 0


# 5
def test_sum_number_valid():
    assert f.sum_number(2, 4) == 9


def test_sum_number_invalid():
    assert f.sum_number(2, 10) == 9


def test_sum_number_zero():
    assert f.sum_number(0, 0) == 0


# 6
def test_simple_number_valid():
    assert f.simple_number(2) == True

    assert f.simple_number(1) == True

    assert f.simple_number(10) == False


def test_simple_number_invalid():
    assert f.simple_number(3) == False

    assert f.simple_number(4) == True


# 7
def test_happy_number_valid():
    assert f.happy_number(123420) == True

    assert f.happy_number(123428) == False


def test_happy_number_invalid():
    assert f.happy_number(00000) == True

    assert f.happy_number(9999999) == True

    assert f.happy_number(123420) == False
