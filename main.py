import random

computer_n = random.randrange(1,10)

# print(computer_n)

player_life = 3

play = True

start_menu = ['###############################################',
              '# you have three attempt for guess the number #',
              '###############################################']

large_than = ['########################',
              '#  number larger than  #',
              "# you have: " + str(player_life) + " attempts #",
              '########################']

lower_than = ['########################',
              '#  number lower than   #',
              "# you have: " + str(player_life) + " attempts #",
              '########################']

win = ["##############",
       "# YOU WIN!!! #",
       "##############"]

lose = ["###############",
        "# YOU LOSE((( #",
        "# NUMBER IS " + str(computer_n)+ " #",
        "###############"]

for i in range(len(start_menu)):
    print(start_menu[i])

# print("# you have three attempt for guess the number #")

while play:

    player_n = int(input())
    
    if player_n == computer_n:
        
        # print("You win!!!")
        
        for i in range(len(win)):
            
            print(win[i])
            
        break
    
    if player_n < computer_n:
        
        player_life -= 1
        
        # print("number larger than")
        # print("you have: " + str(player_life) + " attempts")
        
        large_than[2] = "# you have: " + str(player_life) + " attempts #"
        
        for i in range(len(large_than)):
            
            print(large_than[i])
        
    else:
        
        player_life -= 1
        
        # print("number lower than")
        # print("you have: " + str(player_life) + " attempts")
        
        lower_than[2] = "# you have: " + str(player_life) + " attempts #"
        
        for i in range(len(lower_than)):
            
            print(lower_than[i])
    
    if player_life == 0:
        play = False
    
    print(player_life)


for i in range(len(lose)):
    print(lose[i])
