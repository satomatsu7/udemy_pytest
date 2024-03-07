import pytest
from bank_account import BankAccount

@pytest.fixture
def account():
    # 初期残高1000のBankAccountインスタンスを作成
    return BankAccount(1000)

def test_bank_account_initial_balance(account):
    # fixtureから取得したaccountインスタンスを使用
    assert account.get_balance() == 1000, "初期残高が正しく設定されていません"

def test_deposit_positive_amount(account):
    account.deposit(500)
    assert account.get_balance() == 1500, "預金後の残高が正しくありません"

def test_withdraw_sufficient_balance(account):
    account.withdraw(500)
    assert account.get_balance() == 500, "引き出し後の残高が正しくありません"

def test_withdraw_insufficient_balance(account):
    with pytest.raises(ValueError, match="残高不足です"):
        account.withdraw(2000)

def test_deposit_negative_amount(account):
    with pytest.raises(ValueError, match="預金額は正の値でなければなりません"):
        account.deposit(-500)

def test_withdraw_negative_amount(account):
    with pytest.raises(ValueError, match="引き出し額は正の値でなければなりません"):
        account.withdraw(-500)

