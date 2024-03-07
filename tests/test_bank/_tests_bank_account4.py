# 結合テストのスクリプト（まだ完成していないという設定）

import pytest
from bank_account import BankAccount

@pytest.mark.currency
def test_get_balance_in_currency():
    account = BankAccount(1000)
    # このテストは通貨変換機能をテストし、実行が遅い可能性があるため、slowとcurrencyマーカーが付けられています。
    # 通貨変換のロジック（外部APIのモックなど）をここに実装します。

@pytest.mark.integration
def test_bank_account_with_real_database():
    # このテストは実際のデータベースとの統合テストであるため、integrationマーカーが付けられています。
    # 統合テストのロジックをここに実装します。
