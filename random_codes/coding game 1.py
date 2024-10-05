# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:42:42 2023

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:40:10 2022

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 07:37:07 2022

@author: Admin
"""
print('''


                                          /\
       !__!          O   _    __         /LL\         __    _    O
   /\__('')__/\     /L\  \'._(oo)  _    /LLLL\    _  (OO)_.'/   /L\
  / _        _ \   /LLL\  `.   (_.'/   /LLLLLL\   \'._)   .'   /LLL\
  \/ \/\  /\/ \/  /LLLLL_.' _.'-..'     |.--.|     '..-'._ `'._LLLLL\
        mm         |.-.'__.'____________||__||____________'. __'.-.|
     \_  '\/` \_   ||_||\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\||_||
,__/  /`  ,\_ /'  [_____]\_\_\/\_\_\_\_\_\/\_\_\_\_\_\/\_\_\_\[_____]
   \\/---./  \\   /LLLLL\\_\_//\\\_\_\_\_//\\\_\_\_\_//\\_\_\_/LLLLL\
  .'\\, // '. \\ /LLLLLLL\==//__\\======//oo\\======//__\\===/LLLLLLL\
 /   \\//    \ \/LLLLLLLLL\__|__|________|__|________|__|__ /LLLLLLLLL\
:     \#\   _ :[___________]_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_[___________]
'   _//\ (_// '\|    _   |_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|   _    |
 \  \ ( \ \/ / )|  .'|'.[__].=============================.[__].'|'.  |
  '. \ \) ).' / |  |-OO| || |          _________          | || |-+-|  |
    `-\/#(`  / /|  |_|_| || |    _    [_________]    _    | || |_|_|  |
     __\ ,\ / / |        || |  .'_'.   |__    _|   .'_'.  | ||        |
    (OO.-----.% |    _   || |  | | |_  (oo)_.'/|   | | |  | ||   _    |
     %%|R.I.P|%%|  .'|'. || |  |-+-|\'._)   .' |   |-+-|  | || .'|'.  |
    %%%|_____|%%|  |-+-| || |  |_|_| '..-'._ `'._  |_|_|  | || |OO-|  |
~^"^~[_________]|  |_|_| || | [_____]  |    '.__.'[_____] | || |_|_|  |
    ''"^"^"~~^"`|        || |          |       |          | ||        |
                | /\     || lc_________|_______|__________| ||        | _
                |_) )_   ||/                               \||      _ | ))
  .-~^"^-__    .' """ '._||_________________________________||______)\.'""'.
              / /\   /\ \__]XXXXXXXXXX[_________]XXXXXXXXXX[__]~"^.'""'.__.'
             |    /_\    |~"^~"^~"^~[_____________]~^"~_________  '.__.'~^"^
             |  _______  |                            /Keep Out/   -"~"-
              \ \W W W/ /                  _-        /________/
               '.\M M/.'               __--             / /
              '~"^"~"^~'.                              / /
   _-"^~"^"-                    __--              _-^~"^"~^-_ ''')
print("Welcome to escape the house game!!")
print("Your mission is to escape the hounted house.")
print("So lets start!!")
choise1=input("you are in a hounted house on the tarris.There are two ways infront of you.Which will you choose? 'downstairs' or 'wait to sunrise' :")
if(choise1=="downstairs"):
    print("The ghosts killd you.GAME OVER.")
    print("One ghosts gave you a puzzel.If you sloved the puzzel you will be safe on tarris.")
    print("You have to understand and write the code !#%&@$^")
    print("HINT:The code is in number.")
    a=int(input("Enter the code:"))
    if(a==1357246):
        print("VERY GOOD!! YOU CAN CONTINUE!!")
        choise1=input("Type wait to sunrise. ")
    else:
        print("WRONG ANSWER.GAME OVER!!!")
if(choise1=="wait to sunrise"):
   choise2=input("Now you entered the bunglow.There are two ways infront of you.What will you choose? 'right' or 'left' :")
   if(choise2=="right"):
       print("You found a ghost.You became scared and jumped fromed balcanoy and died. ")
   else:
       print("You found 3 doors.In door 1 thers are many cactus which will make your body channi.In door 2 there are many poisanus snakes which will kill you and in door 3 there is poisanus gas till 4meters.")
       a=input("Choose 'door1','door2' or 'door3'")
if(a=="door3"):
    print("You controled your breath and crossed the room")
    choise4=input("Now there is a big monster in front of you.You have a sword,a bow and arrow and a bom in that room.Click '1' for sword.Click '2' for bow and arrow.Click '3' for bom.What will you choose? :")
else:
    print("YOU DIED!!GAME OVER!!")
if(choise4=="1"):
    print("You choose right wepon.You killed the MONSTER!!")
    if(choise4=="2"):
        print("You hit yourself from the arrow and died.GAME OVER!!")
        if(choise4=="3"):
            print("You blasted yourself.GAME OVER!!")
abc=input("Now you are taleported magically to a dark park out side the bunglow filled with ghost.What will you choose?'climb a tree' or 'hide underground' ")
if(abc=="hide underground"):
    print("You choose right choise.The ghosts cant see you")
else:
    print("There were ghosts on tree and they killd you.GAME OVER!!!")
choise6=input("You found a way underground.You follwed the way.You got 3 theasure boxes.Which will you choose?'box made of gold' or 'box made of copper' or 'box made of iron'  ")    
if(choise6=="box made of gold"):
    print("It was box filled with snakes.You died.GAME OVER!!!")
    if(choise6=="box made of copper"):
        print("You chossed a right box.But it has a code as a puzzel.If yoi sloved the puzzle you will win the treasure.")
        print("The puzzel is:Write the letters in numbers:'MANANAGRAWAL '")    
        b=int(input("Write the numbers here :"))
        if(b=="131141141718123112"):
            print("CONGRASILATIONS YOU WON THE TREASURE!!!")
            print('''
                                ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))

 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.  ''')
            if(choise6=="box made of iron"):
                print("It was box filled with ghosts.You died.GAME OVER!!!")
   
            
            

            
        
        
    
       
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   