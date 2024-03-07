import pytest
from bank_account import BankAccount

def test_bank_account_initial_balance():
    account = BankAccount(1000)
    assert account.get_balance() == 1000, "初期残高が正しく設定されていません"

def test_deposit_positive_amount():
    account = BankAccount()
    account.deposit(500)
    assert account.get_balance() == 500, "預金後の残高が正しくありません"

def test_withdraw_sufficient_balance():
    account = BankAccount(1000)
    account.withdraw(500)
    assert account.get_balance() == 500, "引き出し後の残高が正しくありません"

def test_withdraw_insufficient_balance():
    account = BankAccount(500)
    with pytest.raises(ValueError, match="残高不足です"):
        account.withdraw(1000)

def test_deposit_negative_amount():
    account = BankAccount()
    with pytest.raises(ValueError, match="預金額は正の値でなければなりません"):
        account.deposit(-500)

def test_withdraw_negative_amount():
    account = BankAccount(1000)
    with pytest.raises(ValueError, match="引き出し額は正の値でなければなりません"):
        account.withdraw(-500)
