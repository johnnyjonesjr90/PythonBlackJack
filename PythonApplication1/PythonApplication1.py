
import PythonModule

playerCard1=""
playerCard2=""
playerCard3=""
dealerCard1=""
dealerCard2=""
dealerCard3=""
choice =0
total= 0
Dtotal=0

exit00=0
while(exit00==0):
    dealerCard1 = PythonModule.Convert(dealerCard1, 0)
    dealerCard2 = PythonModule.Convert(dealerCard2, 0)
    playerCard1 = PythonModule.Convert(playerCard1, 0)
    playerCard2 = PythonModule.Convert(playerCard2, 0)
    Dtotal= dealerCard1+dealerCard2
    total= playerCard1 +playerCard2
    if(total>21):total=2
    if(Dtotal>21):Dtotal=2
    d= 'Dealer Cards:' + str(PythonModule.Suitchoice())+' '+str(dealerCard1)+ ' / ' +str(PythonModule.Suitchoice())+'  ' +str(dealerCard2)+ '  Total: ' + str(Dtotal)
    print(d)
    p= 'Player Cards:' + str(PythonModule.Suitchoice())+' '+str(playerCard1)+ ' / ' +str(PythonModule.Suitchoice())+'  ' +str(playerCard2)+ '  Total: ' + str(total)
    print(p)
    input()
    exit=0
    while(exit==0):
        exit2=0
        while(exit2==0):
            print('Dealer Total:'+str(Dtotal))
            print('Player Total:'+str(total))
            print(PythonModule.HitStay())
            choice=int(input())
            if(choice!=1 and choice !=2): print('Incorrect entry')
            if(choice ==1 or choice==2):exit2=1
        if(choice==1):
            playerCard3 = PythonModule.Convert(PythonModule.Deal(), total)
            total += playerCard3
            p2= "Card:" +str(PythonModule.Suitchoice()) + str(playerCard3) + "Total: " + str(total)+  "Press Enter"
            print(p2)
            if(total>21):
                print(PythonModule.Bust())
                input()
                exit2 = 1
                exit00=1
                exit=1
  
            if(total==21):
                print(PythonModule.Hit21())
                input()
                exit2 = 1
                exit00=1
                exit=1
            
        if(choice==2):
            exit3=0
            while(exit3==0):
                print(Dtotal)
                if(Dtotal<16):
                    dealerCard3= PythonModule.Convert(PythonModule.Deal(), Dtotal)
                    Dtotal+= dealerCard3
                    d2= "Card:" +str(PythonModule.Suitchoice()) + str(dealerCard3) + "Total: " + str(total)
                    print(d2)
                
                if(Dtotal>=16):
                    d3= "Dealer Total: " + str(total)
                    print(d3)
                    exit3 = 1
                    exit2 = 1
                    exit=1
                

    if(total>Dtotal and total<=22):
        print('Congrats you win   Press Enter')
        input()
    if(Dtotal>total and Dtotal<22):
        print('Dealer wins  Press Enter')
        input()
    if(Dtotal==total):
        print('Dealer Draw  Press Enter')
        input()
    print('Play again? (1)- Yes  (2)  No')
    choice2 = int(input())
    if(choice2 ==2):
        print('Thanks for playing. Press Enter')
        input()
        exit00=1

                