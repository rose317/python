import random
import sys
import time

class Card:
    """
      定义扑克牌类，每个对象代表一张扑克牌
      """
    def __init__(self,card_type,card_text,card_value):
        self.card_type = card_type
        self.card_text = card_text
        self.card_value = card_value

class Role:
    def __init__(self):
        #定义角色类，用来表示电脑（庄家）和我们用户（玩家）

        #定义列表，用来保存当前校色手中的牌，初始牌为空
        self.cards = []

    def show_card(self):
        #向控制台打印手中所有的牌

        for card in self.cards:
            print(card.card_type,card.card_text,sep="",end="")
            #打印当前角色手中所有牌之后，在进行一个换行
    
        print()

    def get_value(self,min_or_max):
        #定义一个总的点数
        sum2 = 0
        #牌面中A的数量
        A = 0
        for card in self.cards:
            #累计相加的所有点数
            sum2 += card.card_value
            #累计A的数量
            if card.card_text == "A":
                A += 1
        if min_or_max == "max":
            #逐渐减少A的数量
            for i in range(A):
                value = sum2 - i*10
                if value <= 21:
                    return value
        return sum2-A*10

    def burst(self):
        #判断是否爆牌，是返回true,否则返回false

        return self.get_value("min")>21


class CardManager:
    #扑克牌管理类，管理一整副扑克牌，并且能够进行发牌

    def __init__(self):

        self.cards = []

        #定义所有牌的类型
        all_card_type = "♥♦♣♠"

        all_card_text = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

        all_card_value = [11,10,10,10,10,9,8,7,6,5,4,3,2]

        #对牌面类型与牌面文本进行嵌套循环
        for card_type in all_card_type:
            for index,card_text in enumerate(all_card_text):
                #创建Card类型的对象。（一张扑克牌）
                card = Card(card_type, card_text,all_card_value[index])
                self.cards.append(card)

        #洗牌操作
        random.shuffle(self.cards)
        
    def send_card(self,role,num =1):
        for i in range(num):
            card = self.cards.pop()
            role.cards.append(card)

    #创建扑克牌管理者
cards = CardManager()
    #创建电脑角色对象
computer = Role()
    #创建玩家角色
player = Role()
    #给庄家发一张牌给玩家发一张牌
cards.send_card(computer)
cards.send_card(player,2)
    #显示庄家玩家手中的牌
computer.show_card()
player.show_card()
    #询问玩家是否要牌，要则继续发牌，不要给庄家发牌
while True:
    choice = input("是否再要一张牌？【y/n】")
    if choice == 'y':
        #向玩家发牌
        cards.send_card(player)
        computer.show_card()
        player.show_card()
        #判断每次玩家要牌后，是否爆牌，如果爆牌，则玩家负
        #如果没有爆牌，则继续向玩家询问是否要牌
        if player.burst():
            print("爆牌，你输了")
            sys.exit()
            #没有要牌则停止循环
    else:
        break
#庄家发牌，小于17，必须一直要牌，17与21点之间停止要牌
while True:
    print("庄家发牌中。。。")
    time.sleep(1)
    cards.send_card(computer)
    computer.show_card()
    player.show_card()
    if computer.burst():
        print("庄家爆牌，您赢了")
        sys.exit()
    elif computer.get_value("max")>=17:
        break
#都没有爆牌，互相比较大小
player_value = player.get_value("max")
computer_value = computer.get_value("max")

if player_value > computer_value:
    print("你赢了")
elif player_value == computer_value:
    print("平局")
else:
    print("你输了")
    
    

                
                
            
        
     



    
                
            
         
         

        
            
            
        
