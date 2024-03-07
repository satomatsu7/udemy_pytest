# テストのスキップ
import pytest
import os

@pytest.mark.skip(reason="このテストは現在利用できません")
def test_feature_x():
    # 未実装のテスト
    pass

# @pytest.mark.skipif(os.getenv("MY_ENV_VAR") == "true", reason="MY_ENV_VARがtrueの場合はスキップ")
# def test_feature_y():
#     # MY_ENV_VARがtrueのときにスキップされるテスト
#     pass
