# 导入要使用模块
import pytest
import yaml
import os
filepath = os.path.dirname(__file__) +"/calc.yml"
from calculator_homework.calc_demo import Calculator
# 提取文件数据
with open(filepath,encoding='utf-8') as f:
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

# 定义测试计算机的类
class TestCalc:
    # 定义setup_class()方法
    def setup_class(self):
        # 实例化计算器
        self.calc = Calculator()
        print("开始计算")
    # 定义teardown_class()
    def teardown_class(self):
        print("结束计算")

    def setup(self):
        print("测试用例开始")

    def teardown(self):
        print("测试用例结束")
    # 定义测试加法的参数以及方法
    @pytest.mark.parametrize('a,b,expect',add_datas,ids=add_ids)
    # 定义一个test_add()方法
    def test_add(self,a,b,expect):
        try:
            # 调用它的相加add()方法
            result = calc = self.calc.add(a,b)
            # 判断result为小数的时候使用round取小数点后两位
            if isinstance(result,float):
                result = round(result,2)
        except:
            if isinstance(a,str):
                raise ValueError("计算不能有特殊字符")
            elif isinstance(b,str):
                raise ValueError("计算不能有特殊字符")
        else:
            # 断言
            assert expect == result

    # 定义测试除法的参数以及方法
    @pytest.mark.parametrize('a,b,expect',div_datas,ids=div_ids)
    def test_div(self,a,b,expect):
        try:
            # 调用它的除法的方法
            result = self.calc.div(a,b)
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if b == 0:
                raise ValueError("被除数不能为0")
            elif  isinstance(a,str):
                raise ValueError("计算不能有特殊字符")
            elif isinstance(b,str):
                raise ValueError("计算不能有特殊字符")
        else:
            # 断言
            assert expect == result






