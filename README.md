"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，进行PK，
打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

# 定义一个fight方法：
def fight():
    # 定义四个变量，分别是每个角色的血量hp和攻击力power的值:
    my_hp = 3000
    my_power = 300
    teacher_hp = 5000
    teacher_power = 100
    # while 循环，若不退出循环，将一直执行:
    while True:
        # 定义打斗多个回合后，角色的剩余的血量：
        my_hp = my_hp - teacher_power
        teacher_hp = teacher_hp - my_power
        # if ...elif ...else 语句判断,当某角色剩余血量<=0时，输出判断结果:
        if my_hp <= 0:
            # 输出打印判断结果:
            print("老师的剩余血量：",teacher_hp)  # 打印输出结果:
            print("我的剩余血量：",my_hp)         # 打印输出结果:
            print("我输了，惜败")                 # 打印输出结果:
            break
            # 结束循环:
        elif teacher_hp <= 0:   ## if ...elif ...else 语句判断,当某角色剩余血量<=0时，输出判断结果:
            print("老师的剩余血量：",teacher_hp)
            print("我的剩余血量：",my_hp)
            print("老师输了，被打的毫无还手之力")
            print("温馨提示：“充钱可以使你变得更加强大“")
            break
            # 结束循环:
    print("第三天又进行了一次PK")
    my_hp = 8000
    my_power = 800
    teacher_hp = 5000
    teacher_power = 500
    boyfriend_hp = 8000
    boyfriend_power = 600
    while True:
        my_hp = my_hp - teacher_power
        teacher_hp = teacher_hp - my_power
        if my_hp <= 0:
            print("老师的剩余血量：",teacher_hp)
            print("我的剩余血量：",my_hp)
            print("我输了，惜败")
            break
        elif teacher_hp <= 0:
            print("老师的剩余血量：",teacher_hp)
            print("我的剩余血量：",my_hp)
            print("老师输了，再次被打的毫无还手之力")
            print("温馨提示：“充钱不到位，充钱可以使你变得更加强大“")
            print("老师生气的叫来了男朋友")
            if boyfriend_hp >= 8000 and boyfriend_power >= 1000:
                print("我输了不冤，下次继续")
            else: print("结果他也输了")
            break

# 调用fight()方法
fight()
