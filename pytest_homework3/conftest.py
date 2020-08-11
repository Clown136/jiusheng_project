# 导入要使用模块
from typing import List

import pytest
import yaml
import os

filepath = os.path.dirname(__file__) + "/calc3.yml"
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



def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """
    Called after collection has been performed. May filter or re-order
    the items in-place.
    :param _pytest.main.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[_pytest.nodes.Item] items: List of item objects.
    """
    print("items")
    print(items)

    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
# 1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
# 2、env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group将下面所有的option都展示在这个group下
    mygroup.addoption("--env",
                      default='test',  # 默认值
                      dest='env',  # 存储的变量
                      help='测试环境'  # 参数说明
                      )
    mygroup.addoption("--dev",
                      default='demo',  # 默认值
                      dest='dev',  # 存储的变量
                      help='模块'  # 参数说明
                      )
    mygroup.addoption("--st",
                      default='str',  # 默认值
                      dest='st',  # 存储的变量
                      help='字符串'  # 参数说明
                      )


# 获取参数
@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')


@pytest.fixture(scope='session')
def cmdoption1(request):
    return request.config.getoption("--dev", default='demo')


@pytest.fixture(scope='session')
def cmdoption2(request):
    return request.config.getoption("--st", default='str')





