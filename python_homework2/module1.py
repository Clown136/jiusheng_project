# 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个

class Dog:      # 定义类，定义一个动物狗：
    #  属性
        color = "yellow"    # 颜色，黄色
        leg = 4         # 有四条腿
        character = "lively"    # 性格，活泼
    #  方法，使用def关键字定义方法
        def eat(self):      # 吃
            print("狗在吃")    # 打印输出
        def talk(self):     # 叫
            print("狗在叫")    # 打印输出
        def sleep(self):    # 睡
            print("狗在睡")    # 打印输出
#  类的实例化
dog = Dog()
print("狗的颜色",Dog.color)        # 打印输出颜色
print("狗的腿数",dog.leg)          # 打印输出腿的数量
print("狗的性格",Dog.character)    # 打印输出性格
dog.eat()           # 打印输出吃
dog.talk()          # 打印输出叫
dog.sleep()         # 打印输出睡


class Bird:         #  定义类，定义一个动物鸟：
    #  属性
    color = "black"         # 颜色，黑色
    wings = 2               # 翅膀2支
    leg = 2                 # 有2条腿
    #  方法，使用def关键字定义方法
    def talk(self):         # 叫
        print("鸟在叫")            # 打印输出
    def run(self):          # 跑
        print("鸟在跑")            # 打印输出
    def sleep(self):        # 睡
        print("鸟在睡")            # 打印输出
#  类的实例化
bird = Bird ()
print("鸟的颜色",bird.color)        # 打印输出颜色
print("鸟的翅膀",bird.wings)        # 打印输出翅膀的数量
print("鸟的腿数",bird.leg)          # 打印输出腿的数量
bird.talk()         # 打印输出叫
bird.run()          # 打印输出跑
bird.sleep()        # 打印输出睡


class DuanYu:      # 定义类，定义人物段誉：
    #  属性
    height = 178            # 身高，178
    weight = 150            # 体重，150
    appearance = "handsome"         # 容貌，帅气
    #  方法，使用def关键字定义方法
    def six_pulse_excalibur(self):      # 六脉神剑
        print("在练六脉神剑")           # 打印输出
    def the_ghost_alkaloids(self):      # 北冥神功
        print("在练北冥神功")           # 打印输出
    def rap_with_edison(self):          # 凌波微步
        print("在练凌波微步")           # 打印输出
#  类的实例化
duanyu = DuanYu()
print("身高",duanyu.height)           # 打印输出身高
print("体重",duanyu.weight)           # 打印输出体重
print("容貌",duanyu.appearance)       # 打印输出容貌
duanyu.six_pulse_excalibur()            # 打印输出在练六脉神剑
duanyu.the_ghost_alkaloids()            # 打印输出在练北冥神功
duanyu.rap_with_edison()                # 打印输出在练凌波微步


class XiaoHong:         # 定义类，定义人物小红：
    #  属性
    skin = "white"          # 皮肤，白
    appearance = "beautiful"        # 容貌，漂亮
    figure = "good"         # 身材，很好
    #  方法，使用def关键字定义方法
    def swimming(self):     # 游泳
        print("在游泳")         # 打印输出
    def tourism(self):      # 旅游
        print("在旅游")         # 打印输出
    def shopping(self):     # 购物
        print("在购物")         # 打印输出
#  类的实例化
hong = XiaoHong()
print("皮肤",hong.skin)           # 打印输出皮肤
print("容貌",hong.appearance)        # 打印输出容貌
print("身材",hong.figure)         # 打印输出身材
hong.swimming()         # 打印输出在游泳
hong.tourism()          # 打印输出在旅游
hong.shopping()         # 打印输出在购物



class Boss:         # 定义类，定义一个怪物Boss
    #  属性
    volume = "large"        # 体积，庞大
    damage = 10000          # 攻击力，10000
    defense = 10000         # 防御力，10000
    #  方法，使用def关键字定义方法
    def hammer(self):           # 锤击
        print("Boss会锤击")        # 打印输出
    def tear(self):             # 撕裂
        print("Boss会撕裂")        # 打印输出
    def block(self):            # 格挡
        print("Boss会格挡")        # 打印输出
#  类的实例化
boss = Boss()
print("体积",boss.volume)         # 打印输出体积
print("攻击力",boss.damage)        # 打印输出攻击力
print("防御力",boss.defense)       # 打印输出防御力
boss.hammer()           # 打印输出Boss会锤击
boss.tear()             # 打印输出Boss会撕裂
boss.block()            # 打印输出Boss会格挡