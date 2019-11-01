import random

l=1
while l>0 :
    def player():
        pc=input("choose rock ,paper or scissor: ")
        if pc in ['Rock','rock','ROCK','r']:
            pc='r'
        elif pc in ['Paper','paper','PAPER','p']:
            pc='p'
        elif pc in ['Scissor','scissor','SCISSOR','s']:
            pc='s'
        else:
            print('enter valid option!')
        return pc


    def computer():
        cc=random.randint(0,2)
        if cc==1:
            cc='r'
        elif cc==0:
            cc='p'
        else:
            cc='s'
        return cc
    pc=player()    
    cc=computer()
    if pc=='r':
        if cc=='r':
            print('computer chose rock')
            print("draw")
        elif cc=='p':
            print('computer chose paper')
            print("computer won")
        else:
            print('computer chose scissor')
            print("you won")
    elif pc=='p':
        if cc=='p':
            print('computer chose paper')
            print("draw")
        elif cc=='s':
            print('computer chose scissor')
            print("computer won")
        else:
            print('computer chose rock')
            print("you won")
    else :
        if cc=='s':
            print('computer chose scissor')
            print("draw")
        elif cc=='r':
            print('computer chose rock')
            print("computer won")
        else:
            print('computer chose paper')
            print("you won")
    ans=input('if you want to continue,press y: ')
    if ans=='y':
        pass
    else:
        break



