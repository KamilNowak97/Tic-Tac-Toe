#! /usr/bin/python3
from random import randint

#Stan planszy
plansza = ['-','-','-',
           '-','-','-',
           '-','-','-']
#Metoda do wyświetlenia planszy
def print_board(board):
    print(board[0]+ "|" +board[1] + "|" + board[2])
    print(board[3]+ "|" +board[4] + "|" + board[5])
    print(board[6]+ "|" +board[7] + "|" + board[8])
    
#Metoda sprawdzająca który gracz aktualnie wygrywa
def does_player_win(board):
    count_x = 0
    count_y= 0
    for value in board:
        if value == 'x':
            count_x += 1
        elif value == 'o':
            count_y +=1
       
    
    if count_x > count_y: 
        print("--------------------------------")   
        print("Aktualnie wygrywa gracz: krzyżyk")
        print("--------------------------------") 
    else:
        print("--------------------------------")   
        print("Aktualnie wygrywa gracz:  kółko")
        print("--------------------------------")

#AI komputera
def ai_move(board):
    pos = randint(0,8)
    while board[pos] != '-':
        pos = randint(0,8)

    board[pos] = 'o'
    return board

#Metoda do pobrania ruchu użytkownika
def get_user_move(board):
    print("Gdzie chcesz postawić krzyżyk?")
    choice = input()

    while board[int(choice)] != '-':
        choice = input()
        print("Spróbuj jeszcze raz")

    board[int(choice)] = 'x'
    return board

#16 - najpierw musi być sprawdzona wygrana
def draw_game(board):
    not_blank = 0

    
    for val in board:
        if val != '-':
            not_blank += 1
    if not_blank == 9:
        if(win_game(board)==False):
            return True
        else:
            return False
  
#Sprawdzenie czy ktoś wygrał
def win_game(board):
    
    if board[0] == board[1] and board[0] == board[2]:
        if(board[0]=='o'):
            print ("Wygrało kółko")
            return True
        elif(board[0]=='x'):
             print("Wygrał krzyżyk")
             return True

    elif board[3] == board[4] and board[3] == board[5]:
        if(board[3]=='o'):
            print ("Wygrało kółko")
            return True
        elif(board[3]=='x'):
             print("Wygrał krzyżyk")
             return True
    elif board[6] == board[7] and board[6] == board[8]:
        if(board[6]=='o'):
            print ("Wygrało kółko")
            return True
        elif(board[6]=='x'):
            print("Wygrał krzyżyk")
            return True

    elif board[0] == board[3] and board[0] == board[6]:
        if(board[0]=='o'):
            print ("Wygrało kółko")
            return True
        elif(board[0]=='x'):
             print("Wygrał krzyżyk")
             return True
    elif board[1] == board[4] and board[1] == board[7]:
        if(board[1]=='o'):
            print ("Wygrało kółko")
            return True
        elif(board[1]=='x'):
             print("Wygrał krzyżyk")
             return True
    elif board[2] == board[5] and board[2] == board[8]:
        if(board[2]=='o'):
            print ("Wygrało kółko")
            return True
        elif(board[2]=='x'):
             print("Wygrał krzyżyk")
             return True
    
    elif board[0] == board[4] and board[0] == board[8]:
        if(board[0]=='o'):
            print ("Wygrało kółko")
            return True
        elif(board[0]=='x'):
             print("Wygrał krzyżyk")
             return True
    elif board[2] == board[4] and board[2] == board[6]:
        if(board[2]=='o'):
            print ("Wygrało kółko")
            return True
        elif(board[2]=='x'):
             print("Wygrał krzyżyk")
             return True
    else:
        return False
    
def final(board):
    if draw_game(plansza) == True: 
        print_board(plansza)
        print("--------------------------------")
        print("Nastąpił remis. Nikt nie wygrał.")
        print("--------------------------------")
        return True
    if win_game(plansza) == True: 
        print_board(plansza)
        return True
  
        
#Główna pętla    
while True:
    print_board(plansza)
    get_user_move(plansza)
    if final(plansza) == True:
        break
    ai_move(plansza)
    if final(plansza) == True:
        break
    

   
        


    


