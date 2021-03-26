import pytest

from checking_account import CheckingAccount


@pytest.fixture
def conta():
    return CheckingAccount('1234-5', 'Test', 1000.00, 50000)


def test_should_debit_ten_percent_when_deposited():
    conta
    conta.deposit(1000)
    expected_balance = 1999.9
    assert conta.get_balance() == expected_balance


def test_deve_lancar_erro_quando_depositar_valor_negativo():
    conta
    with pytest.raises(TypeError):
        conta.withdraw("A")


def test_deve_dar_erro_se_saca_mais_que_saldo():
    conta
    conta.withdraw(3000)
