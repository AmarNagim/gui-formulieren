from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.messagebox import askyesno
import string
import random

window = Tk()
window.geometry('400x300')
points = 0
def main():
    
    def gameFunction(amountSpinBoxes, word):
        global points
        points = amountSpinBoxes*amountSpinBoxes
        centerFrame = Frame(window)
        window.title('Guessword - Player 2')
        centerFrame.pack()
        spinboxList = []

        titleLabel = Label(centerFrame, text="Raad het woord", font=("Arial", 20, font.BOLD), fg="black").pack(pady=30)
        alphabet = list(string.ascii_uppercase)
        print(alphabet)

        for spinboxContent in range(amountSpinBoxes):
            listAmount = f'list{spinboxContent}'
            listAmount = []
            listAmount.append(word[spinboxContent].upper())
            for randomLetter in range(4):
                random.shuffle(alphabet)
                if alphabet[0] in listAmount:
                    listAmount.append(alphabet[1])
                else:    
                    listAmount.append(alphabet[0])
                random.shuffle(listAmount)
            print(f'listamount: {listAmount}')                
            spinboxAmount = Spinbox(centerFrame, state='readonly', values=listAmount, width=2, font=("Arial", 20))
            spinboxAmount.pack(side=LEFT, pady=13)
            print(f'current letter {spinboxContent}')
            spinboxList.append(spinboxAmount)



        def answerMatchFunction():
            global points
            wrongAnswer = 0
            userWordList = []
            userWord = ''
            for userWordItteration in range(len(spinboxList)): 
                letter = spinboxList[userWordItteration].get()
                userWordList.append(letter)
            userWord = ''.join(userWordList).lower()
            print(userWordList)
            if userWord == word:
                print('pass')
                endOfGame = askyesno(title="Guess the word", message=f"Congratulations you guessed the word! You ended up with {points} score! Do you want to play again?")
                if endOfGame:
                    for widget in window.winfo_children():
                        widget.destroy()
                    main()                        
                else:
                    window.destroy()    
            else:
                for letterMatch in range(amountSpinBoxes):
                    letterMatchCheck = word[letterMatch] == userWord[letterMatch]
                    if letterMatchCheck == False:
                        wrongAnswer+=1
                        print(points)
                        points-=2
                        print(points)
                        if points == 0:
                            endOfGame = askyesno(title="Guess the word", message=f"You lost. Do you want to play again?")
                            if endOfGame:
                                for widget in window.winfo_children():
                                    widget.destroy()
                                main()
                            else:
                                window.destroy()                                
                if points > 0:            
                    messagebox.showinfo(title=None, message=f'Helaas er zijn {wrongAnswer} letters fout. Nog {points} punten over')               
           
        centerFrame = Frame(window)
        centerFrame.pack()
        doeEenGok = Button(centerFrame, text="Doe een gok", borderwidth=1, highlightthickness=1, highlightbackground='black', font=("Arial", 13), command=answerMatchFunction)
        doeEenGok.pack(pady=27)

    def clearWindow(wordEntryValue):
        for widget in window.winfo_children():
            widget.destroy()
        wordEntryValueLenght = len(wordEntryValue)               
        gameFunction(wordEntryValueLenght, wordEntryValue)            

    def startScreen(): 
        centerFrame = Frame(window)
        window.title('Guessword - Player 1')
        centerFrame.pack()
        titleLabel = Label(centerFrame, text="Vul een woord in", font=("Arial", 20, font.BOLD), fg="black").pack(pady=30)

        wordEntry = Entry(centerFrame)
        wordEntry.config(width=20, font=("Arial", 15), borderwidth=0, highlightthickness=0.5, highlightbackground='black')
        wordEntry.pack(pady=5)
        def getEntryValue():
            entryValue = wordEntry.get().lower()
            if len(entryValue) < 4 or len(entryValue) > 7:
                startScreen()
                messagebox.showerror(title='ERROR', message='Het opgegeven woord is niet tussen de 4 en 7 letters!')
            else:    
                clearWindow(entryValue)

        entryText = Label(centerFrame, text="(4 tot 7 letters)", font=("Arial", 10, font.ITALIC), fg="black").pack()

        entryButton = Button(centerFrame, text="Stel woord in", command=getEntryValue)
        entryButton.configure(borderwidth=1, highlightthickness=1, highlightbackground='black', font=("Arial", 13))
        entryButton.pack(pady=30)       
    wordEntry = startScreen()
main()


window.mainloop()