current_player = "X"
stop = False
board = [
    "-","-","-",
    "-","-","-",
    "-","-","-",
]
count=0

def changePlayer(current):
    global current_player
    if current == "X":
        current_player= "0"
    if current == "0":
        current_player="X"


def play(position):
    global current_player
    global count 
    if board[int(position)] != "-":
        print("This position is not available")
    else:
        board[int(position)] = current_player
        count +=1
        check_for_winner ()
        changePlayer(current_player)

def check_for_winner():
    global stop
    global count
    if count <9:
        if board[6] == current_player and board[7] ==current_player and board[8] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True
        if board[3] == current_player and board[4] ==current_player and board[5] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True
        if board[0] == current_player and board[1] ==current_player and board[2] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True
        if board[0] == current_player and board[3] ==current_player and board[6] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True       
        if board[1] == current_player and board[4] ==current_player and board[7] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True   
        if board[2] == current_player and board[5] ==current_player and board[8] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True 
        if board[0] == current_player and board[4] ==current_player and board[8] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True 
        if board[2] == current_player and board[4] ==current_player and board[6] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True 
        if board[4] == current_player and board[5] ==current_player and board[6] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True 
        if board[1] == current_player and board[2] ==current_player and board[3] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True 
        if board[1] == current_player and board[4] ==current_player and board[7] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True 
        if board[2] == current_player and board[5] ==current_player and board[8] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True 
        if board[3] == current_player and board[6] ==current_player and board[9] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True
        if board[1] == current_player and board[5] ==current_player and board[9] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True
        if board[7] == current_player and board[5] ==current_player and board[3] == current_player: 
            print("\nGame Over.\n")                
            print(" " +current_player + " won. ")
            stop = True
    elif count == 9:
        print("It's a tie")
        stop = True
    


def print_board():
    print(f"""
    Current board ({current_player} turn):

    [{board[0]}] [{board[1]}] [{board[2]}]
    [{board[3]}] [{board[4]}] [{board[5]}]
    [{board[6]}] [{board[7]}] [{board[8]}]
    """)

while stop == False:
    command = input("Which key do you want?: ")

    if command == "stop":
        stop = True
    else:
        play(command)

    print_board()