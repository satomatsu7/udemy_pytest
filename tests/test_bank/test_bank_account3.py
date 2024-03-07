# mockの使い方
from unittest.mock import patch
import pytest
from bank_account import BankAccount

def test_get_balance_in_currency():
    account = BankAccount(1000)
    with patch('requests.get') as mock_get:
        # APIからの偽のレスポンスを設定
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rate': 0.75  # 仮定する為替レート
        }

        # USDからEURへの変換をテスト
        balance_in_eur = account.get_balance_in_currency('EUR')
        assert balance_in_eur == 750, "変換後の残高が正しく計算されていません"

def test_get_balance_in_currency_with_api_failure():
    account = BankAccount(1000)
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404  # API呼び出し失敗を模擬

        with pytest.raises(Exception, match="通貨変換サービスにアクセスできませんでした"):
            account.get_balance_in_currency('EUR')

