# 导入要使用模块
import pytest
import yaml
import os

filepath = os.path.dirname(__file__) + "/calc2.yml"
from pytest_homework2.calc import Calculator

# 提取文件数据
with open(filepath, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    # 获取测试用例加法的参数
    add_datas = datas['add']['add_demo']
    print(add_datas)
    # 获取加法测试用例的标题
    add_ids = datas['add']['add_ids']
    print(add_ids)
    # 获取除法的参数
    div_datas = datas['div']['div_demo']
    print(div_datas)
    # 获取除法测试用例的标题
    div_ids = datas['div']['div_ids']
    print(div_ids)
    # 获取测试用例减法的参数
    sub_datas = datas['sub']['sub_demo']
    print(sub_datas)
    # 获取减法测试用例的标题
    sub_ids = datas['sub']['sub_ids']
    print(sub_datas)
    # 获取测试用例乘法的参数
    mul_datas = datas['mul']['mul_demo']
    print(mul_datas)
    # 获取乘法测试用例的标题
    mul_ids = datas['mul']['mul_ids']
    print(mul_ids)


@pytest.fixture(scope='function')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")


@pytest.fixture(params=add_datas, ids=add_ids)
def get_adddatas(request):
    data = request.param
    print(f"加法的测试数据是：{data}")
    return data


@pytest.fixture(params=sub_datas, ids=sub_ids)
def get_subdatas(request):
    data = request.param
    print(f"减法的测试数据是：{data}")
    return data


@pytest.fixture(params= mul_datas, ids=mul_ids)
def get_muldatas(request):
    data = request.param
    print(f"乘法的测试数据是：{data}")
    return data


@pytest.fixture(params=div_datas, ids=div_ids)
def get_divdatas(request):
    data = request.param
    print(f"除法法的测试数据是：{data}")
    return data
