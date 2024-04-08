# テストのスキップ
import pytest
import os

@pytest.mark.skip(reason="このテストは現在利用できません")
def test_feature_x():
    # 未実装のテスト
    pass
