# tests/conftest.py
import pytest
from bank_account import BankAccount

@pytest.fixture
def bank_account():
    """テスト用のBankAccountインスタンスをセットアップするフィクスチャ"""
    return BankAccount(initial_balance=1000)

