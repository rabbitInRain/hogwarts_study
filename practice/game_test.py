
#定义对战方法
import random


def fight(enemy_hp, enemy_power):
    #定义自己的出生血量和攻击力
    my_hp = 1000
    my_power = 200

    #打印敌人初始血量和初始攻击力
    print(f"敌人的初始血量为{enemy_hp},初始攻击力为{enemy_power}")

    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        if my_hp < 0:
            print(f"我的剩余血量为{my_hp},敌人的剩余血量为{enemy_hp},我输了")
            break
        elif my_hp == 0 & enemy_hp == 0:
            print(f"我的剩余血量为{my_hp},敌人的剩余血量为{enemy_hp},平局")
            break
        elif enemy_hp < 0:
            print(f"我的剩余血量为{my_hp},敌人的剩余血量为{enemy_hp},我赢了")
            break

if __name__ =="__main__":

    #列表推导式生成敌人的血量
    hp = [x for x in range(990, 1010)]
    enemy_hp = random.choice(hp)

    #randint随机生成敌人攻击力
    enemy_power = random.randint(190, 210)

    fight(enemy_hp, enemy_power)


