import pytest


# # 多参数，多次循环，数组[]的形式
# @pytest.mark.parametrize("name,word", [["安琪拉", "火烧屁屁喽"], ["黄忠", "周日被我射熄火了"], ["鲁班", "哒哒哒哒哒"]])
# def test_parametrize_02(name, word):
#     print(f'{name}的台词是:{word}')

# 多参数，多次循环，元组()的形式
@pytest.mark.parametrize("name,word", [("安琪拉", "火烧屁屁喽"), ("黄忠", "周日被我射熄火了"), ("鲁班", "哒哒哒哒哒")])
def test_parametrize_02(name, word):
    print(f'{name}的台词是:{word}')
