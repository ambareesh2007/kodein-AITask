import random
board = [" "]*9
def printboard():
    print(board[0] +"|"+board[1]+"|"+board[2])
    print("")
    print(board[3] +"|"+board[4]+"|"+board[5])
    print("")
    print(board[6] +"|"+board[7]+"|"+board[8])

def playermove():
    print("Give a number between 0 and 8")
    n=int(input())
    c=0
    while c==0:
        if (n<0 or n>8) or board[n]!=" " :
            print("Invalid!, Enter Again")
            n=int(input())
        else:
            board[n]="X"
            c+=1


def compmove():
    flag=False
    while flag==False:
        n=random.randrange(0,9)
        if (n<0 or n>8) or board[n]!=" " :
            continue
        else:
            flag=True
            board[n]="O"


def wincheck():
    if(((board[0]==board[1]==board[2]) and board[0]!=" ")or
       ((board[3]==board[4]==board[5]and board[3]!=" "))or
       ((board[6]==board[7]==board[8]and board[6]!=" "))or
       ((board[0]==board[3]==board[6]and board[0]!=" "))or
       ((board[1]==board[4]==board[7]and board[1]!=" "))or
       ((board[2]==board[5]==board[8]and board[2]!=" "))or
       ((board[0]==board[4]==board[8]and board[0]!=" "))or
       ((board[2]==board[4]==board[6]and board[2]!=" "))):
        return True
    else:
        return False
        

f=0
printboard()
while f==0:
    print("")
    playermove()
    printboard()
    print('')
    if(board[0]!=" " and
       board[1]!=" " and 
       board[2]!=" " and
       board[3]!=" " and
       board[4]!=" " and
       board[5]!=" " and 
       board[6]!=" " and
       board[7]!=" " and
       board[8]!=" "):
            print("Draw")
            break
    if wincheck():
        print("You won!")
        break
    compmove()
    printboard()
    print("")
    if(board[0]!=" " and
       board[1]!=" " and 
       board[2]!=" " and 
       board[3]!=" " and 
       board[4]!=" " and
       board[5]!=" " and
       board[6]!=" " and
       board[7]!=" " and
       board[8]!=" "):
            print("Draw")
            break
    if wincheck():
        print("You lost!, Better luck next time")
        break
