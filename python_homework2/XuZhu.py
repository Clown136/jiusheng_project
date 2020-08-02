# 模块化，导入TongLao类
from python_homework2.TongLao import TongLao

# 定义一个XuZhu类，继承于童姥。
class XuZhu(TongLao):
    # 定义虚竹血量和武力值，防具属性（通过传入的参数得到）
    def __init__(self,xu_hp,xu_power,armor):
        super().__int__(1000,200)
        self.xu_hp = xu_hp
        self.xu_power = xu_power
        self.armor = armor
      #  定义一个fight方法，双方进行生死一击，
    def fight(self,enemy_hp,enemy_power):
       # 需要传入敌人的hp，power，进行生死，打完之后，血多的一方获胜
        self.xu_hp = self.xu_hp + self.armor - enemy_power
        self.enemy_hp = enemy_hp - self.xu_power
       # 定义一个if判断语句，一击后，虚竹血量 > 敌人血量则打印”虚竹赢！报仇了“
        if self.xu_hp > enemy_hp:
            print("虚竹赢！报仇了")
        # 一击后，虚竹血量 < 敌人血量则打印”敌人赢！大仇未报“
        elif self.xu_hp < enemy_hp:
            print("敌人赢！大仇未报")
         #   一击后，虚竹血量 = 敌人血量则打印”平局！各自离去“
        else:
            print("平局！各自离去")
    # 虚竹宅心仁厚不想打架。所以虚竹有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    def read(self):
        print("罪过罪过")
    # 虚竹发怒后，会有一个发怒的方法，会与敌人生死一搏
    def angry(self):
        print("虚竹发怒了")

# 虚竹实例化，传入虚竹血量和武力值，防具属性参数
xu = XuZhu(3000,300,500)
# 打印发怒状态
xu.angry()
# 传入搏斗时敌人的血量和攻击力
xu.fight(3000,300)
