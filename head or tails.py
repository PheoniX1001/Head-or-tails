import tkinter as tk
import random as rand
k=0
i=0
root=tk.Tk()
lab2=tk.Label(root,text="",font=("Sans"))
lab3=tk.Label(root,text="",font=("Sans"))
result_label=tk.Label(root,text='',font=('sans'))
coin=50
counter=0
counl=tk.Label(root,text=f"\nNo. of rolls={counter}\n",font=("Sans"))
coin_ammount=tk.Label(root,text=f"Coins:{coin}",font=('sans')) 
 
def rolls():
    global counter
    counter=counter+1
    counl.configure(text=f"\nNo. of rolls={counter}\n")  
def check_game_over(): 
    if coin == 0: 
        ch.config(state=tk.DISABLED) 
        ch2.config(state=tk.DISABLED) 
        result_label.config(text="Game Over! No more coins.") 
        return True

    elif coin==100:
        ch.config(state=tk.DISABLED) 
        ch2.config(state=tk.DISABLED) 
        result_label.config(text="Game Won! Congratulations. You won 100 coins") 
        return True        
    return False

def head():
    global coin
    global k
    a=1
    if a==(rand.randint(1,2)):
        lab2.configure(text='\nYOU WON!')
        lab2.pack()
        if k==1:
           coin=coin+20
           check_game_over()
        else:
           coin=coin+10
    else:   
        lab2.configure(text='\nYOU LOST!')
        lab2.pack()
        coin=coin-10
    coin_ammount.configure(text=f"Coins: {coin}")
    check_game_over()
    rolls()

def tail():
    global coin
    global k
    a=2
    if a==(rand.randint(1,2)):
        lab2.configure(text='\nYOU WON!')
        lab2.pack()
        if k==1:
           coin=coin+20
           check_game_over()
        else:
           coin=coin+10
    else:
        lab2.configure(text='\nYOU LOST!')
        lab2.pack()
        coin=coin-10
    coin_ammount.configure(text=f"Coins: {coin}")
    check_game_over()
    rolls()

def dub_apply():
    global k
    global coin
    app=tk.Label(sop,text='',font=("sans"))
    app.configure(text='Doubler booster applied')
    coin=coin-60
    coin_ammount.configure(text=f"Coins: {coin}")
    app.pack()
    k=1


def shop():
    global sop
    sop=tk.Tk()
    sop.geometry('500x400')
    txt1=tk.Label(sop,text="",font=("Sans"))
    txt1.configure(text='Welcome to the shop! Buy any items')
    txt1.pack()
    dub=tk.Button(sop,text="Doubler (60 coins)",command=dub_apply,pady=10,padx=10)
    if(coin>=70):
        dub.pack()
         
    
    else:
        dub.pack()
        dub.config(state=tk.DISABLED)

def rpl():
    global coin, counter, k,booster_rolls
    coin = 50
    counter = 0
    k = 0
    booster_rolls = 0
    coin_ammount.configure(text=f"Coins: {coin}")
    counl.configure(text=f"\nNo. of rolls={counter}\n")
    lab2.configure(text="")
    result_label.config(text="")
    ch.config(state=tk.NORMAL)
    ch2.config(state=tk.NORMAL)
    shp.config(state=tk.NORMAL)
     


        
lab1=tk.Label(root,text="",font=("Sans"))
lab1.configure(text='\n\tHeads  or  Tails?')
lab1.pack()
coin_ammount.pack()
counl.pack()
ch=tk.Button(root,text='Heads ',command=head,pady=10,padx=10)
ch2=tk.Button(root,text=" Tails ",command=tail,pady=10,padx=10)
shp=tk.Button(root,text=" Shop ",command=shop,pady=10,padx=10)
replay=tk.Button(root,text="Play again?",command=rpl,pady=10,padx=10)
quit=tk.Button(root,text='Exit',command=root.quit,pady=10,padx=10)
result_label.pack()
ch.pack()
ch2.pack() 
shp.pack()
quit.pack()
replay.pack()
root.geometry('500x400')
root.mainloop()
