# parametrizeの使い方

import pytest
from bank_account import BankAccount

# depositメソッドのパラメータ化テスト
@pytest.mark.parametrize("initial_balance, deposit_amount, expected_balance", [
    (1000, 500, 1500),
    (0, 100, 100),
])
def test_deposit(initial_balance, deposit_amount, expected_balance):
    account = BankAccount(initial_balance)
    assert account.deposit(deposit_amount) == expected_balance

# withdrawメソッドのパラメータ化テスト
@pytest.mark.parametrize("initial_balance, withdraw_amount, expected_balance", [
    (1000, 500, 500),
    (100, 100, 0),
])
def test_withdraw(initial_balance, withdraw_amount, expected_balance):
    account = BankAccount(initial_balance)
    assert account.withdraw(withdraw_amount) == expected_balance

# withdrawメソッドで残高不足のケースのパラメータ化テスト
@pytest.mark.parametrize("initial_balance, withdraw_amount", [
    (100, 200),
    (0, 1),
])
def test_withdraw_insufficient_balance(initial_balance, withdraw_amount):
    account = BankAccount(initial_balance)
    with pytest.raises(ValueError, match="残高不足です"):
        account.withdraw(withdraw_amount)
