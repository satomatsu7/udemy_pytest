# 例外のテスト/マーカーのテスト
import pytest
from bank_account import BankAccount

@pytest.mark.raises
def test_deposit_negative_amount_raises_exception():
    account = BankAccount()
    with pytest.raises(ValueError, match="預金額は正の値でなければなりません"):
        account.deposit(-100)
