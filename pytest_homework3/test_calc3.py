# 作业1：
# 1、编写用例顺序：加- 除-减-乘
# 2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
# 作业2【选做】：
# 1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
# 2、env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据


import pytest


# 定义测试计算机的类
class TestCalc:

    # 控制测试用例的执行顺序
    # 定义测试加法的参数以及方法
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_adddatas):
        try:
            # 调用它的加法方法
            result = get_calc.add(get_adddatas[0], get_adddatas[1])
            # 判断result为小数的时候使用round取小数点后两位
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if isinstance(get_adddatas[0], str):
                raise ValueError("计算不能有特殊字符")
            elif isinstance(get_adddatas[1], str):
                raise ValueError("计算不能有特殊字符")
        else:
            # 断言
            assert get_adddatas[2] == result

    # 控制测试用例的执行顺序
    # 定义测试除法的参数以及方法
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_divdatas):
        try:
            # 调用它的除法的方法
            result = get_calc.div(get_divdatas[0], get_divdatas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if get_divdatas[1] == 0:
                raise ValueError("被除数不能为0")
            elif isinstance(get_divdatas[0], str):
                raise ValueError("计算不能有特殊字符")
            elif isinstance(get_divdatas[1], str):
                raise ValueError("计算不能有特殊字符")
        else:
            # 断言
            assert get_divdatas[2] == result

    # 控制测试用例的执行顺序
    # 定义测试减法的参数以及方法
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_subdatas):
        try:
            # 调用它的减法方法
            result = get_calc.sub(get_subdatas[0], get_subdatas[1])
            # 判断result为小数的时候使用round取小数点后两位
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if isinstance(get_subdatas[0], str):
                raise ValueError("计算不能有特殊字符")
            elif isinstance(get_subdatas[1], str):
                raise ValueError("计算不能有特殊字符")
        else:
            # 断言
            assert get_subdatas[2] == result

    # 控制测试用例的执行顺序
    # 定义测试乘法的参数以及方法
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_muldatas):
        try:
            # 调用它的乘法方法
            result = get_calc.mul(get_muldatas[0], get_muldatas[1])
            # 判断result为小数的时候使用round取小数点后两位
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if isinstance(get_muldatas[0], str):
                raise ValueError("计算不能有特殊字符")
            elif isinstance(get_muldatas[1], str):
                raise ValueError("计算不能有特殊字符")
        else:
            # 断言
            assert get_muldatas[2] == result
