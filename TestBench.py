import random
import time
a=random.randint(8,10)
i=0

def powerwash(num1,num2,sent1,sent2):
    Invalid_Input=False
    while Invalid_Input==False:
        illusion=input(sent1)
        try:
            illusion=int(illusion)
            if illusion>num1 and illusion<num2:
                Invalid_Input=True
                return illusion
            else:
                print(sent2)
        except:
            pass
    

class character:
    def __init__(self,health,shield,damage,name,money,Type,maxhealth):
        self.health=health
        self.shield=shield
        self.damage=damage
        self.name=name
        self.money=money
        self.Type=Type
        self.maxhealth=maxhealth

    def damageTaken1(self,decreaseHealth):
        if self.shield>0:
            self.shield-=decreaseHealth
            if self.shield<=0:
                 self.shield=0
        elif self.shield<=0:
            self.shield=0
            self.health-=decreaseHealth
            if self.health<=0:
                self.health=0

#Elliott
class enemy1:
    def __init__(self,health,shield,damage,name):
         self.health=health
         self.shield=shield
         self.damage=damage
         self.name=name

    def damageTaken2(self,decreaseHealth):
        if self.shield>0:
             self.shield-=decreaseHealth
             if self.shield<=0:
                 self.shield=0
        elif self.shield<=0:
            self.shield=0
            self.health-=decreaseHealth
            if self.health<=0:
                self.health=0

# Gilbert
class enemy2:
     def __init__(self,health,shield,damage,name):
         self.health=health
         self.shield=shield
         self.damage=damage
         self.name=name

     def damageTaken3(self,decreaseHealth):
         if self.shield>0:
             self.shield-=decreaseHealth
             if self.shield<=0:
                 self.shield=0
         elif self.shield<=0:
             self.shield=0
             self.health-=decreaseHealth
             if self.health<=0:
                 self.health=0
# #Alex
class enemy3:
    def __init__(self,health,shield,damage,name):
        self.health=health
        self.shield=shield
        self.damage=damage
        self.name=name

    def damageTaken4(self,decreaseHealth):
         if self.shield>0:
             self.shield-=decreaseHealth
             if self.shield<=0:
                 self.shield=0
         elif self.shield<=0:
             self.shield=0
             self.health-=decreaseHealth
             if self.health<=0:
                self.health=0

# #Glibert
class enemy4:
     def __init__(self,health,shield,damage,name):
         self.health=health
         self.shield=shield
         self.damage=damage
         self.name=name

     def damageTaken5(self,decreaseHealth):
         if self.shield>0:
             self.shield-=decreaseHealth
             if self.shield<=0:
                 self.shield=0
         elif self.shield<=0:
             self.shield=0
             self.health-=decreaseHealth
             if self.health<=0:
                 self.health=0
#Alex
class enemy5:
    def __init__(self,health,shield,damage,name):
        self.health=health
        self.shield=shield
        self.damage=damage
        self.name=name

    def damageTaken6(self,decreaseHealth):
        if self.shield>0:
            self.shield-=decreaseHealth
            if self.shield<=0:
                 self.shield=0
        elif self.shield<=0:
            self.shield=0
            self.health-=decreaseHealth
            if self.health<=0:
                self.health=0


#Elliott
class enemy6:
     def __init__(self,health,shield,damage,name):
         self.health=health
         self.shield=shield
         self.damage=damage
         self.name=name


     def damageTaken7(self,decreaseHealth):
        if self.shield>0:
            self.shield-=decreaseHealth
            if self.shielf<=0:
                 self.shield=0
        elif self.shield<=0:
            self.shield=0
            self.health-=decreaseHealth
            if self.health<=0:
                self.health=0


class boss1:
     def __init__(self,health,shield,damage,name):
         self.health=health
         self.shield=shield
         self.damage=damage
         self.name=name


     def damageTaken8(self,decreaseHealth):
        if self.shield>0:
            self.shield-=decreaseHealth
            if self.shield<=0:
                 self.shield=0
        elif self.shield<=0:
            self.shield=0
            self.health-=decreaseHealth
            if self.health<=0:
                self.health=0


logo1='''
    ███        ▄████████   ▄▄▄▄███▄▄▄▄      ▄███████▄  ▄█          ▄████████                              
▀█████████▄   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███         ███    ███                              
   ▀███▀▀██   ███    █▀  ███   ███   ███   ███    ███ ███         ███    █▀                               
    ███   ▀  ▄███▄▄▄     ███   ███   ███   ███    ███ ███        ▄███▄▄▄                                  
    ███     ▀▀███▀▀▀     ███   ███   ███ ▀█████████▀  ███       ▀▀███▀▀▀                                  
    ███       ███    █▄  ███   ███   ███   ███        ███         ███    █▄                               
    ███       ███    ███ ███   ███   ███   ███        ███▌    ▄   ███    ███                              
   ▄████▀     ██████████  ▀█   ███   █▀   ▄████▀      █████▄▄██   ██████████                              
                                                      ▀                                                   
'''
logo2='''

   ▄████████ ████████▄   ▄█    █▄     ▄████████ ███▄▄▄▄       ███     ███    █▄     ▄████████    ▄████████
  ███    ███ ███   ▀███ ███    ███   ███    ███ ███▀▀▀██▄ ▀█████████▄ ███    ███   ███    ███   ███    ███
  ███    ███ ███    ███ ███    ███   ███    █▀  ███   ███    ▀███▀▀██ ███    ███   ███    ███   ███    █▀ 
  ███    ███ ███    ███ ███    ███  ▄███▄▄▄     ███   ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄    
▀███████████ ███    ███ ███    ███ ▀▀███▀▀▀     ███   ███     ███     ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀    
  ███    ███ ███    ███ ███    ███   ███    █▄  ███   ███     ███     ███    ███ ▀███████████   ███    █▄ 
  ███    ███ ███   ▄███ ███    ███   ███    ███ ███   ███     ███     ███    ███   ███    ███   ███    ███
  ███    █▀  ████████▀   ▀██████▀    ██████████  ▀█   █▀     ▄████▀   ████████▀    ███    ███   ██████████
                                                                                   ███    ███             
'''
print('\nSatisfy Your Soul With A')
time.sleep(2)
print(logo1)
time.sleep(1)
print(logo2)
time.sleep(1)
input("Press Enter to Start")

skillPoints=75
maxhealth=powerwash(0,75,'\nyou have 75 skillpoints\nhow many do you want to spent on health?\nremaining skillpoints will go to damage\n','you cannot do that')
health=maxhealth
damage=skillPoints-maxhealth

if health<=5:
    skill=powerwash(0,4,'\nwould you like the class "glass cannon"?\n1 -> Yes\n2 -> No','choose Yes or No')
    if skill==1:
        Type='glass cannon'
        damage=200
        health=5
elif damage<=5:
    skill=powerwash(0,4,'\nwould you like the class "tank"?\n1 -> Yes\n2 -> No','choose Yes or No')
    if skill==1:
        Type='tank'
        health=300
        damage=5

name=input("\nwhat is your name?")
if name=='dev':
    Type='dev'
    health=1000000000000
    damage=1000000000000
elif name=='devboss':
    Type='dev'
    health=1000000000000
    damage=1000000000000
    i+=50

player=character(health,100,damage,name,75,Type,maxhealth)
print(f'Your name is {name}\nYour health is {health}\nYour damage is {damage}')
if Type=='tank':
    print('secret Type: tank')
elif Type=='glass cannon':
    print('secret Type: glass cannon')
elif Type=='':
    pass

while i<a:
    try:
        for k in range(0,2):
            print('YOU FIND A THREE WAY FORK IN YOUR PATH WHICH DIRECTION DO YOU WANT TO GO?')
            illusion=powerwash(0,5,'\n1 -> LEFT\n2 -> RIGHT\n3 -> FORWARD \n4 -> CHECK STATS\n >> ','\nyou just stand still\n')
            if illusion==1 or illusion==2 or illusion==3:
                chance=random.randint(k,2)
                if chance==2:
                    encounter=random.randint(0,5)
                    if encounter==0:
                        A_F_K=enemy1(1,50,5,'A Fallen Knight') #change
                        print(f'\nYou encounter {A_F_K.name}\n') #change
                        while player.health>0 and A_F_K.health>0: #change
                            hit=random.randint(1,10)
                            if hit>=1 and hit<4:
                                print(f'{A_F_K.name} attacks\n*weak slash*') #change
                                print(f'-{A_F_K.damage} player health')
                                player.damageTaken1(A_F_K.damage) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')    
                                wait=input('\npress enter to continue\n ----------')
                            elif hit>4 and hit<10:
                                print(f'{A_F_K.name} attacks\n*normal slash*') #change
                                print(f'-{A_F_K.damage*2} player health')
                                player.damageTaken1(A_F_K.damage*2) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            elif hit==10:
                                print(f'{A_F_K.name} attacks\n*strong slash*') #change
                                print(f'-{A_F_K.damage*4} player health')
                                player.damageTaken1(A_F_K.damage*4) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            attack=powerwash(0,4,'1 -> use weapon\n2 -> heal\n3 -> pass\n ----------','\nYou did nothing\n')
                            if attack==1:
                                print(f'{player.name} attacks\n*clank*')
                                print(f'-{player.damage} Fallen Knight health')
                                A_F_K.damageTaken2(player.damage) #change   
                                print(f'health {A_F_K.health}/1\nshield {A_F_K.shield}/50')         
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==2:
                                print(f'healing {player.name}')
                                player.health+=10
                                if player.health>player.maxhealth:
                                    player.health=player.maxhealth
                                    print(f'health maxed')
                                elif player.health<=player.maxhealth:
                                    print(f'+10 health')
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==3:
                                print('you did nothing')
                                wait=input('\npress enter to continue\n ----------')
                        if player.health<=0:
                            print('battle finished\n')
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{A_F_K.name}'s Stats:\n  Health: {A_F_K.health}\n shield: {A_F_K.shield}\n Damage: {A_F_K.damage}") #change
                            wait=input('\npress enter to continue\n ----------')
                            print('You lost\nGAME OVER')
                            i+=100
                            break
                        else:
                            print('battle finished\n')
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{A_F_K.name}'s Stats:\n  Health: {A_F_K.health}\n shield: {A_F_K.shield}\n Damage: {A_F_K.damage}") #change
                            wait=input('\npress enter to continue\n ----------')
                            print(f'You slayed {A_F_K.name}\n') #change
                            wait=input('\npress enter to continue\n ----------')
                            print('You absorb their power and strenghthen your soul')
                            if player.shield==0:
                                print('+25 shields')
                                player.shield+=25
                            elif player.shield>=90:
                                print('shields maxed')
                                player.shield=100
                            elif player.shield>0 and player.shield<90:
                                print('+10 shields')
                                player.shield+=10
                            wait=input('\npress enter to continue\n ----------')


                    elif encounter==1:
                        S=enemy2(150,0,5,'A Skeleton')
                        print(f'\nYou encounter {S.name}\n')
                        print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                        wait=input('Press enter to continue\n ----------')
                        print(f"{S.name}'s Stats:\n  Health: {S.health}\n shield: {S.shield}\n Damage: {S.damage}")
                        wait=input('press enter to continue\n ----------')
                        while player.health>0 and S.health>0:
                            hit=random.randint(1,10)
                            if hit>=1 and hit<4:
                                print(f'{S.name} attacks\n*Rattle*') #change
                                print(f'-{S.damage} player health') #change
                                player.damageTaken1(S.damage) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')    
                                wait=input('\npress enter to continue\n ----------')
                            elif hit>4 and hit<10:
                                print(f'{S.name} attacks\n*Rattle Rattle*') #change
                                print(f'-{S.damage*2} player health') #change
                                player.damageTaken1(S.damage*2) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            elif hit==10:
                                print(f'{S.name} attacks\n*Rattle Rattle Rattle*') #change
                                print(f'-{S.damage*4} player health') #change
                                player.damageTaken1(S.damage*4) #change damage and S
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            attack=powerwash(0,4,'1 -> use weapon\n2 -> heal\n3 -> pass\n ----------','\nYou did nothing\n')
                            if attack==1:
                                print(f'{player.name} attacks\n*thwack*')
                                print(f'-{player.damage} Skeleton')
                                S.damageTaken3(player.damage) #change   
                                print(f'health {S.health}/150\nshield {S.shield}/0')         
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==2:
                                print(f'healing {player.name}')
                                player.health+=10
                                if player.health>player.maxhealth:
                                    player.health=player.maxhealth
                                    print(f'health maxed')
                                elif player.health<=player.maxhealth:
                                    print(f'+10 health')
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==3:
                                print('you did nothing')
                                wait=input('\npress enter to continue\n ----------')
                        if player.health<=0:
                            print('You lost\nGAME OVER')
                            i+=100
                            break
                        else:
                            print('battle finished\n')
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{S.name}'s Stats:\n  Health: {S.health}\n shield: {S.shield}\n Damage: {S.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f'You slayed {S.name}')
                            wait=input('\npress enter to continue\n ----------')
                            print('You absorb their power and strenghthen your soul')
                            if player.health>0:
                                print('+5 damage')
                                player.damage+=5
                            wait=input('\npress enter to continue\n ----------')


                    elif encounter==2:
                        A_S_G=enemy3(10,10,10,'A Stone Golem')
                        print(f'\nYou encounter {A_S_G.name}\n')
                        print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                        wait=input('\nPress enter to continue\n ----------')
                        print(f"{A_S_G.name}'s Stats:\n  Health: {A_S_G.health}\n shield: {A_S_G.shield}\n Damage: {A_S_G.damage}")
                        wait=input('\npress enter to continue\n ----------')
                        while player.health>0 and A_S_G.health>0:
                            hit=random.randint(1,10)
                            if hit>=1 and hit<7:
                                print(f'{A_S_G.name} attacks\n*punch*') #change
                                print(f'-{A_S_G.damage} player health') #change
                                player.damageTaken1(A_S_G.damage) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')    
                                wait=input('\npress enter to continue\n ----------')
                            elif hit>7 and hit<10:
                                print(f'{A_S_G.name} attacks\n*CRASH*') #change
                                print(f'-{A_S_G.damage*2} player health') #change
                                player.damageTaken1(A_S_G.damage*2) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            elif hit==10:
                                print(f'{A_S_G.name} attacks\n*WHAM*') #change
                                print(f'-{A_S_G.damage*4} player health') #change
                                player.damageTaken1(A_S_G.damage*4) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            attack=powerwash(0,4,'1 -> use weapon\n2 -> heal\n3 -> pass\n ----------','\nYou did nothing\n')
                            if attack==1:
                                print(f'{player.name} attacks\n*Scrape*') #change
                                print(f'-{player.damage} Stone Golem') #change
                                A_S_G.damageTaken4(player.damage) #change damage
                                print(f'health {A_S_G.health}/10\nshield {A_S_G.shield}/10')  #change     
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==2:
                                print(f'healing {player.name}')
                                player.health+=10
                                if player.health>player.maxhealth:
                                    player.health=player.maxhealth
                                    print(f'health maxed')
                                elif player.health<=player.maxhealth:
                                    print(f'+10 health')
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==3:
                                print('you did nothing')
                                wait=input('\npress enter to continue\n ----------')
                        if player.health<=0:
                            print('You lost\nGAME OVER')
                            i+=100
                            break
                        else:
                            print('battle finished\n')
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{A_S_G.name}'s Stats:\n  Health: {A_S_G.health}\n shield: {A_S_G.shield}\n Damage: {A_S_G.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f'You slayed {A_S_G.name}')
                            wait=input('\npress enter to continue\n ----------')
                            print('You absorb their power and strenghthen your soul')
                            if player.health>0:
                                print('+10 maxhealth')
                                player.maxhealth+=10
                            wait=input('\npress enter to continue\n ----------')


                    elif encounter==3:
                        M_T=enemy4(10,0,1,'Mini Thoomas')
                        print(f'\nYou encounter {M_T.name}\n') #change
                        print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                        wait=input('\nPress enter to continue\n ----------')
                        print(f"{M_T.name}'s Stats:\n  Health: {M_T.health}\n shield: {M_T.shield}\n Damage: {M_T.damage}") #change
                        wait=input('\npress enter to continue\n ----------')
                        while player.health>0 and M_T.health>0: #change
                            hit=random.randint(1,10)
                            if hit>=1 and hit<7:
                                print(f'{M_T.name} attacks\n*bite*') #change
                                print(f'-{M_T.damage} player health') #change
                                player.damageTaken1(M_T.damage) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')    
                                wait=input('\npress enter to continue\n ----------')
                            elif hit>7 and hit<10:
                                print(f'{M_T.name} attacks\n*punch*') #change
                                print(f'-{M_T.damage*2} player health') #change
                                player.damageTaken1(M_T.damage*2) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            elif hit==10:
                                print(f'{M_T.name} attacks\n*stab*') #change
                                print(f'-{M_T.damage*4} player health') #change
                                player.damageTaken1(M_T.damage*4) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            attack=powerwash(0,4,'1 -> use weapon\n2 -> heal\n3 -> pass\n ----------','\nYou did nothing\n')
                            if attack==1:
                                print(f'{player.name} attacks\n*kick*') #change
                                print(f'-{player.damage} Mini Thoomas') #change
                                M_T.damageTaken5(player.damage) #change damage
                                print(f'health {M_T.health}/10\nshield {M_T.shield}/0')  #change     
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==2:
                                print(f'healing {player.name}')
                                player.health+=10
                                if player.health>player.maxhealth:
                                    player.health=player.maxhealth
                                    print(f'health maxed')
                                elif player.health<=player.maxhealth:
                                    print(f'+10 health')
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==3:
                                print('you did nothing')
                                wait=input('\npress enter to continue\n ----------')
                        if player.health<=0:
                            print('You lost\nGAME OVER')
                            i+=100
                            break
                        else:
                            print('battle finished\n')
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{M_T.name}'s Stats:\n  Health: {M_T.health}\n shield: {M_T.shield}\n Damage: {M_T.damage}") #change
                            wait=input('\npress enter to continue\n ----------')
                            print(f'You warded off the {M_T.name} for now') #change
                            wait=input('\npress enter to continue\n ----------')
                            print('You absorb their power and strenghthen your soul')
                            if player.health>0:
                                print('+1 maxhealth\n+1 health\n+1 shield\n+1 damage')
                                player.maxhealth+=1
                                player.health+=1
                                player.shield+=1
                                player.damage+=1
                            wait=input('\npress enter to continue\n ----------')


                    elif encounter==4: #TOM MESSED WITH THIS ONE
                        A_G=enemy5(25,25,10,"Anchient Gardian")
                        print(f'\nYou encounterd an {A_G.name}\n')
                        print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                        wait=input('\npress enter to continue\n ----------')
                        print(f"{A_G.name}'s Stats:\n  Health: {A_G.health}\n shield: {A_G.shield}\n Damage: {A_G.damage}")
                        wait=input('\npress enter to continue\n ----------')
                        while player.health>0 and A_G.health>0:
                            hit=random.randint(1,10)
                            if hit>=1 and hit<7:
                                print(f'{A_G.name} attacks\n*SLAM*') #change
                                print(f'-{A_G.damage} player health') #change
                                player.damageTaken1(A_G.damage) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')    
                                wait=input('\npress enter to continue\n ----------')
                            elif hit>7 and hit<10:
                                print(f'{A_G.name} attacks\n*PUNCH*') #change
                                print(f'-{A_G.damage*2} player health') #change
                                player.damageTaken1(A_G.damage*2) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            elif hit==10:
                                print(f'{A_G.name} attacks\n*BOOOOM*') #change
                                print(f'-{A_G.damage*4} player health') #change
                                player.damageTaken1(A_G.damage*4) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            attack=powerwash(0,4,'1 -> use weapon\n2 -> heal\n3 -> pass\n ----------','\nYou did nothing\n')
                            if attack==1:
                                print(f'{player.name} attacks\n*Crack*') #change
                                print(f'-{player.damage} Anchient Gardian') #change
                                A_G.damageTaken6(player.damage) #change damage
                                print(f'health {A_G.health}/25\nshield {A_G.shield}/25')  #change     
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==2:
                                print(f'healing {player.name}')
                                player.health+=10
                                if player.health>player.maxhealth:
                                    player.health=player.maxhealth
                                    print(f'health maxed')
                                elif player.health<=player.maxhealth:
                                    print(f'+10 health')
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==3:
                                print('you did nothing')
                                wait=input('\npress enter to continue\n ----------')
                        if player.health<=0:
                            print('You lost\nGAME OVER')
                            i+=100
                            break
                        else:
                            print('battle finished\n')
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{A_G.name}'s Stats:\n  Health: {A_G.health}\n shield: {A_G.shield}\n Damage: {A_G.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f'You defeated an {A_G.name}')
                            wait=input('\npress enter to continue\n ----------')
                            print('You absorb their power and strenghthen your soul')
                            if player.health>0:
                                print('+5 health')
                                player.health+=5
                                if player.shield==0:
                                    print('+15 shields')
                                    player.shield+=15
                                elif player.shield>=95:
                                    print('shields maxed')
                                    player.shield=100
                                elif player.shield>0 and player.shield<95:
                                    print('+5 shields')
                                    player.shield+=5
                                wait=input('\npress enter to continue\n ----------')



                                # Encounter Here #


                    elif encounter==5:
                        V=enemy6(1,0,50,'Void')
                        print(f'\nYou encounter {V.name}\n') #change
                        print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                        wait=input('\nPress enter to continue\n ----------')
                        print(f"{V.name}'s Stats:\n  Health: {V.health}\n shield: {V.shield}\n Damage: {V.damage}") #change
                        wait=input('\npress enter to continue\n ----------')
                        while player.health>0 and V.health>0: #change
                            hit=random.randint(1,10)
                            if hit>=1 and hit<7:
                                print(f'{V.name} attacks\n*hooon*') #change
                                print(f'-{V.damage} player health') #change
                                player.damageTaken1(V.damage) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')    
                                wait=input('\npress enter to continue\n ----------')
                            elif hit>7 and hit<10:
                                print(f'{V.name} attacks\n*warble*') #change
                                print(f'-{V.damage} player health') #change
                                player.damageTaken1(V.damage) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            elif hit==10:
                                print(f'{V.name} attacks\n*wisper*') #change
                                print(f'-{V.damage} player health') #change
                                player.damageTaken1(V.damage) #change
                                print(f'health {player.health}/{player.maxhealth}\nshield {player.shield}/100')   
                                wait=input('\npress enter to continue\n ----------')
                            attack=powerwash(0,4,'1 -> use weapon\n2 -> heal\n3 -> pass\n ----------','\nYou did nothing\n')
                            if attack==1:
                                print(f'{player.name} attacks\n*woosh*') #change
                                print(f'-{player.damage} Void') #change
                                V.damageTaken7(player.damage) #change damage
                                print(f'health {V.health}/???\nshield {V.shield}/???')  #change     
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==2:
                                print(f'healing {player.name}')
                                player.health+=10
                                if player.health>player.maxhealth:
                                    player.health=player.maxhealth
                                    print(f'health maxed')
                                elif player.health<=player.maxhealth:
                                    print(f'+10 health')
                                wait=input('\npress enter to continue\n ----------')
                            elif attack==3:
                                print('you did nothing')
                                wait=input('\npress enter to continue\n ----------')
                        if player.health<=0:
                            print('You lost\nGAME OVER')
                            i+=100
                            break
                        else:
                            print('battle finished\n')
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                            wait=input('\npress enter to continue\n ----------')
                            print(f"{V.name}'s Stats:\n  Health: {V.health}\n shield: {V.shield}\n Damage: {V.damage}") #change
                            wait=input('\npress enter to continue\n ----------')
                            print(f'You survived the {V.name}') #change
                            wait=input('\npress enter to continue\n ----------')
                            print('You absorb their power and strenghthen your soul')
                            if player.health>0:
                                print('+15 shields')
                                player.damage+=15
                                print('+15 maxhealth')
                                player.maxhealth+=15
                                wait=input('\npress enter to continue\n ----------')
                    else:
                        pass


                    i+=1
                    pass
                else:
                    i+=1
            elif illusion==4:
                print('\n----------')
                print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
                wait=input('press enter to continue\n----------\n')

            elif illusion>4:
                print('you just stand still\n')
    except:
        print('you just stand still\n')
if i<100:
    TOM=boss1(100,50,25,"Tho'mas Destroyer Of Worlds, The Undying Hunger")
    print(f'\nYou encounter {TOM.name}\n') #change
    print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
    wait=input('Press enter to continue\n ----------')
    print(f"{TOM.name}'s Stats:\n  Health: {TOM.health}\n shield: {TOM.shield}\n Damage: {TOM.damage}") #change
    wait=input('press enter to continue\n ----------')
    while player.health>0 and TOM.health>0: #change
        print(f'{TOM.name} attacks\n*BOOM*\n*BANG*\n*POW*') #change
        print(f'-{TOM.damage} player health\n')
        player.damageTaken1(TOM.damage) #change
        wait=input('press enter to continue\n ----------')
        attack=powerwash(0,4,'1 -> use weapon\n2 -> heal\n3 -> pass\n ----------','\nYou did nothing\n')
        if attack==1:
            print(f'{player.name} attacks\n*Slash*') #change
            print(f"-{player.damage} Tho'mas Destroyer Of Worlds, The Undying Hunger") #change
            TOM.damageTaken8(player.damage) #change damage
            print(f'health {TOM.health}/100\nshield {TOM.shield}/50')  #change     
            wait=input('\npress enter to continue\n ----------')
        elif attack==2:
            print(f'healing {player.name}')
            player.health+=10
            if player.health>player.maxhealth:
                player.health=player.maxhealth
                print(f'health maxed')
            elif player.health<=player.maxhealth:
                print(f'+10 health')
            wait=input('\npress enter to continue\n ----------')
        elif attack==3:
            print('you did nothing')
            wait=input('\npress enter to continue\n ----------')
    if player.health<=0:
        print('You lost\nGAME OVER')
    else:
        print('battle finished\n')
        wait=input('press enter to continue\n ----------')
        print(f"{player.name}'s Stats:\n Health: {player.health}\n shield: {player.shield}\n Damage: {player.damage}")
        wait=input('press enter to continue\n ----------')
        print(f"{TOM.name}'s Stats:\n  Health: {TOM.health}\n shield: {TOM.shield}\n Damage: {TOM.damage}") #change
        wait=input('press enter to continue\n ----------')
        print(f'By surviving {TOM.name} you are able to absorb some of their power') #change
        if player.health>0:
            print('+1000000 shields')
            player.shield+=1000000
            print('+1000000 health')
            player.health+=1000000
            print('+1000000 maxhealth')
            player.maxhealth+=1000000
            print('+1000000 damage')
            player.damage+=1000000
        wait=input('press enter to continue\n ----------')
        print('You have found the power within the temple and claimed it for yourself')
        wait=input('press enter to continue\n ----------')
        print('By satisfying your soul you have beaten the game!')