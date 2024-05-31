import customtkinter

def guess_the_number(computer_number, player_number, lives, win, lower, larger, play, text: customtkinter.CTkLabel):

    player_number = int(player_number)

    if lives == 0:
        
        text.configure(text="YOU LOSE!!!")
        
        play = False
        
        return play
    
    if player_number == computer_number:
        
        text.configure(text="YOU WIN!!!")
        
        win = True
        
        return win
    
    if player_number < computer_number:
        
        lives -= 1
        
        text.configure(text="Number is larger!")
        
        larger = True
        
        return larger
        
    else:
        
        lives -= 1
        
        text.configure(text="Number is lower!")
        
        lower = False
        
        return lower



def check_all(play, lower, larger, win, ):
    
    # text.configure(text="new")
    
    if not play:
        
        
        
    elif lower:
        
        
        
    elif larger:
        
        
        
    elif win:
        
        
        
    lower = False
    larger = False
    
    return lower, larger