import random

def make_state():
    return("tictactoe",())

def check_rep(s):
    if s[0]=="tictactoe":
        return True
    else:
        return False

def get_square(s,coords):
    moves=s[1]
#   coords=(x,y)
    for i in moves:
        if i[1]==coords:
            return i[0]
    return False

def check_win(s):
    moves=s[1]
    down1=((0,0),(0,1),(0,2))
    down2=((1,0),(1,1),(1,2))
    down3=((2,0),(2,1),(2,2))
    right1=((0,0),(1,0),(2,0))
    right2=((0,1),(1,1),(2,1))
    right3=((0,2),(1,2),(2,2))
    diag1=((0,0),(1,1),(2,2))
    diag2=((0,2),(1,1),(2,0))
    win_combos=(down1,down2,down3,right1,right2,right3,diag1,diag2)
    x_coords=()
    o_coords=()
    for i in moves:
        if i[0]=="X":
            x_coords+=(i[1],)
        elif i[0]=="O":
            o_coords+=(i[1],)
    for i in win_combos:
        x_score=0
        o_score=0
        for coord in i:
            if coord in x_coords:
                x_score+=1
            elif coord in o_coords:
                o_score+=1
        if x_score==3:
            return "\nX wins!"
        elif o_score==3:
            return "\nO wins!"
    return "\n"

def move(s,x,y,player):
    moves=s[1]
    move_coords=(x,y)
    moves+=((player,move_coords),)
    new_s=("tictactoe",moves)
    return new_s

def play_game():
    ai_var=input("Type S for singleplayer and M for multiplayer: ")
    if ai_var=="M":
        s=make_state()
        show_board(s)
        turn=1
        won=False
        while turn<=9:
            x=int(input("Enter x-coordinate: "))
            y=int(input("Enter y-coordinate: "))
            if x<0 or x>2 or y<0 or y>2:
                print("Invalid Move!")
                continue
            moves=s[1]
            move_coords=(x,y)
            completed_move_coords=()
            for i in moves:
                completed_move_coords+=(i[1],)
            if move_coords in completed_move_coords:
                print("Invalid Move!")
                continue
            elif turn%2==1:
                player="X"
            else:
                player="O"
            s=move(s,x,y,player)
            show_board(s)
            won=check_win(s)
            print(won)
            if won=="\nX wins!" or won=="\nO wins!":
                break
            elif turn==9:
                rematch_var=input("\nIt's a tie. For rematch, type Y. To end game, type anything else. ")
                if rematch_var=="Y":
                    play_game()
                else:
                    print("Thanks for playing!")
            turn+=1
    else:
        play_ai_game()

def play_ai_game():
    s=make_state()
    show_board(s)
    turn=1
    won=False
    while turn<=9:
        if turn%2==0:
            s=ai_move(s,turn)
            show_board(s)
            won=check_win(s)
            print(won)
            if won=="\nX wins!" or won=="\nO wins!":
                break
            turn+=1
        else:
            x=int(input("Enter x-coordinate: "))
            y=int(input("Enter y-coordinate: "))
            if x<0 or x>2 or y<0 or y>2:
                print("Invalid Move!")
                continue
            moves=s[1]
            move_coords=(x,y)
            completed_move_coords=()
            for i in moves:
                completed_move_coords+=(i[1],)
            if move_coords in completed_move_coords:
                print("Invalid Move!")
                continue
            elif turn%2==1:
                player="X"
            else:
                player="O"
            s=move(s,x,y,player)
            show_board(s)
            won=check_win(s)
            print(won)
            if won=="\nX wins!" or won=="\nO wins!":
                break
            elif turn==9:
                rematch_var=input("It's a tie. For rematch, type Y. To end game, type anything else. ")
                if rematch_var=="Y":
                    play_game()
                else:
                    print("Thanks for playing!")
            turn+=1

            

def show_board(s):
    moves=s[1]
    all_coords=((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2))
    c00=" "
    c01=" "
    c02=" "
    c10=" "
    c11=" "
    c12=" "
    c20=" "
    c21=" "
    c22=" "
    all_coord_strings=(c00,c01,c02,c10,c11,c12,c20,c21,c22)
    completed_move_coords=()
    for i in moves:
        completed_move_coords+=(i[1],)
        coord=i[1]
        sym=i[0]
        if coord==(0,0):
            c00=sym
        elif coord==(0,1):
            c01=sym
        elif coord==(0,2):
            c02=sym
        elif coord==(1,0):
            c10=sym
        elif coord==(1,1):
            c11=sym
        elif coord==(1,2):
            c12=sym
        elif coord==(2,0):
            c20=sym
        elif coord==(2,1):
            c21=sym
        elif coord==(2,2):
            c22=sym
    print("\n"+c00+"|"+c10+"|"+c20+"\n"+"- - -\n"+c01+"|"+c11+"|"+c21+"\n"+"- - -\n"+c02+"|"+c12+"|"+c22)
        

def ai_move(s,turn):
    moves=s[1]
    down1=((0,0),(0,1),(0,2))
    down2=((1,0),(1,1),(1,2))
    down3=((2,0),(2,1),(2,2))
    right1=((0,0),(1,0),(2,0))
    right2=((0,1),(1,1),(2,1))
    right3=((0,2),(1,2),(2,2))
    diag1=((0,0),(1,1),(2,2))
    diag2=((0,2),(1,1),(2,0))
    win_combos=(down1,down2,down3,right1,right2,right3,diag1,diag2)
    x_coords=()
    o_coords=()
    for i in moves:
        if i[0]=="X":
            x_coords+=(i[1],)
        elif i[0]=="O":
            o_coords+=(i[1],)
    for i in win_combos:
        x_score=0
        o_score=0
        for coord in i:
            if coord in x_coords:
                x_score+=1
            elif coord in o_coords:
                o_score+=1
        if o_score==2:
            for coord in i:
                if get_square(s,coord)==False:
                    moves+=(("O",coord),)
                    new_s=("tictactoe",moves)
                    return new_s
    for i in win_combos:
        x_score=0
        o_score=0
        for coord in i:
            if coord in x_coords:
                x_score+=1
            elif coord in o_coords:
                o_score+=1
        if x_score==2:
            for coord in i:
                if get_square(s,coord)==False:
                    moves+=(("O",coord),)
                    new_s=("tictactoe",moves)
                    return new_s

    all_coords=((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2))
    corner_coords=((0,0),(2,0),(0,2),(2,2))
    side_coords=((1,0),(0,1),(1,2),(2,1))
    empty_move_coords=()
    empty_corner_coords=()
    empty_side_coords=()
    for coord in all_coords:
        if get_square(s,coord)==False:
            empty_move_coords+=(coord,)
    for coord in corner_coords:
        if get_square(s,coord)==False:
            empty_corner_coords+=(coord,)
    for coord in side_coords:
        if get_square(s,coord)==False:
            empty_side_coords+=(coord,)
    if turn==2:
        if len(empty_corner_coords)==3:
            moves+=(("O",(1,1)),)
            new_s=("tictactoe",moves)
            return new_s
        elif (1,1) not in empty_move_coords:
            move_coord=random.choice(empty_corner_coords)
            moves+=(("O",move_coord),)
            new_s=("tictactoe",moves)
            return new_s
    elif turn==4:
        if len(empty_corner_coords)==2:
            move_coord=random.choice(empty_side_coords)
            moves+=(("O",move_coord),)
            new_s=("tictactoe",moves)
            return new_s
    elif turn==4 or turn==6:
        if empty_corner_coords!=():
            move_coord=random.choice(empty_corner_coords)
            moves+=(("O",move_coord),)
            new_s=("tictactoe",moves)
            return new_s
    move_coord=random.choice(empty_move_coords)
    moves+=(("O",move_coord),)
    new_s=("tictactoe",moves)
    return new_s

        
play_game()


