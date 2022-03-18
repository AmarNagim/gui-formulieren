from ast import Break
from tkinter import *
from tkinter.messagebox import askyesno
import random
import time
import threading
from turtle import width

window = Tk()
window.title('FPS Trainer V1')
window.geometry("450x300")
window.resizable(width=False, height=False)
window.configure(background="light grey")
points=0

topBar = Frame(window, height = 35,width = 450,bg = 'black')
topBar.pack()
topBar.pack_propagate(0)

windowFrame = Frame(window, height=265, width= 450, bg='light grey')
windowFrame.pack()
windowFrame.pack_propagate(0)

def main():
    global points
        
    def pointsFunction():
        pointsLabel['text'] = f"{points} Points"
        

    def gamesFunction(event):
        global gamesBtnDestroy
        global gamesBtn
        pointsFunction()  
        games = ['Press: w', 'Press: a','Press: s', 'Press: d', 'Double click', 'Triple click', 'Single click', 'Press space']
        random.shuffle(games)
        gamesBtn = Label(windowFrame, text=f"{games[0]}",  font=("Arial", 20))
        
        def gamesBtnDestroy():
            gamesBtn.destroy() 
            # gamesFunction(event)   
            
        def keyboardFunction(event):
            global points
            window.unbind(event.keysym)
            window.unbind('<space>')
            gamesBtn.destroy()
            gamesFunction(event)
            points+=1
            pointsFunction()                 


        def mouseFunction(event):
            global points
            gamesBtn.unbind(event.keysym)
            window.unbind(event.keysym)
            gamesBtn.destroy()
            gamesFunction(event)
            points+=2    
            pointsFunction()                 
            
        def buttonBind():
            if games[0] == 'Press: w':
                window.bind('w', keyboardFunction)
            if games[0] == 'Press: a':
                window.bind('a', keyboardFunction) 
            if games[0] == 'Press: s':   
                window.bind('s', keyboardFunction) 
            if games[0] == 'Press: d':   
                window.bind('d', keyboardFunction) 
            if games[0] == 'Press space':   
                window.bind('<space>', keyboardFunction)             
            if games[0] == 'Double click':   
                gamesBtn.bind('<Double-1>', mouseFunction)
            if games[0] == 'Triple click':   
                gamesBtn.bind('<Triple-1>', mouseFunction)
            if games[0] == 'Single click':   
                gamesBtn.bind("<Button-1>", mouseFunction)   
            else:
                pass
            xValue = random.randint(0, 292)
            yValue = random.randint(0, 227)    
            # minimum y value is 0
            # maximum y value is 227
            # minimum x value is 0
            # maximum x value is 292
            gamesBtn.place(x=xValue, y=yValue)
            
        buttonBind() 
                
    def countDown():
        global points
        global startBtn
        global gamesBtn
        lengthSecondsVar = int(lengthSeconds.get())
        startBtn.destroy()
        lengthLabel.destroy()
        lengthSeconds.destroy()
        count = lengthSecondsVar
        while count > -1:
            timeLabel['text'] = f'Time Remaining: {count}'
            count-=1
            time.sleep(1)
            if count == -1:
                gamesBtn.destroy()     
                pointsLabel['text'] = f"0 Points"
                endOfGame = askyesno(title="FPS Trainer V1", message=f"Congratulations you have {points} points, do you want to play again?")
                if endOfGame:   
                    points-=points
                    pointsLabel['text'] = f"0 Points"
                    timeLabel['text'] = f'Time Remaining: '              
                    gamesBtn.destroy()
                    timeLabel.destroy()
                    pointsLabel.destroy()
                    main()
                else:
                    window.destroy()
                    


    def startCd(event):
        cdTh = threading.Thread(target=countDown)
        cdTh.start()        
        gamesFunction(event)

    timeLabel = Label(topBar, text="Time Remaining:".format(''), fg="white", bg="black", font=("Arial", 14))
    timeLabel.pack(side='left')

    pointsLabel = Label(topBar, text="0 Points".format(''), fg="white", bg="black", font=("Arial", 14))
    pointsLabel.pack(side='right')


    def startButton():
        global startBtn
        startBtn = Button(windowFrame, text="Press here to start", highlightthickness = 0, bd = 0, font=("Arial", 15))
        startBtn.bind('<Button-1>', startCd)
        startBtn.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        lengthLabel = Label(windowFrame, text="Enter timer length (seconds)", font=("Arial", 13), bg='light grey')
        lengthLabel.place(relx=0.27, rely=0.27, anchor=W)
        
        lengthSeconds = Entry(windowFrame, width=10, font=('Arial Italic', 12), justify=CENTER, highlightthickness = 0, bd = 0)
        lengthSeconds.insert(0, "20")
        lengthSeconds.pack(side = TOP, pady=87, padx=10)
        return lengthLabel, lengthSeconds
    
    lengthLabel, lengthSeconds = startButton()
    
main()    
window.mainloop()
