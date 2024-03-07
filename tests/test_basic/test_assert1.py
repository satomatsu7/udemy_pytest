# 実行方法:python3 test_assert1.py

# 数値の比較
sum = 1 + 1
assert sum == 2, "1 + 1は2になるはずです"
print("数値チェックOK")

# 文字列の比較
hello_world = "Hello" + " " + "World"
assert hello_world == "Hello World", "文字列の結合が期待通りでない"
print("文字列チェックOK")

# リストに対する操作
items = []
items.append("Python")
assert items == ["Python"], "リストにアイテムが正しく追加されていない"
print("リストチェックOK")

# 実行時にエラーがなければ、ここまでのすべてのassertがTrueと評価されていることになります。
print("すべてのチェックが成功しました。")

