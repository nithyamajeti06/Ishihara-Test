import tkinter
from tkinter import*
import random
import speech_recognition as sr


#List of plates
plates = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]

normal_answers = ["12", "8" ,"6", "29", "57", "5" , "3", "15", "74", "2", "6", "97", "45", "5", "7", "16", "73", "nothing", "nothing", "nothing", "nothing",
                  "26", "42", "35", "96"]

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < len(plates)):  
        x = random.randint(0,len(plates)-1)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(indexes)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 10:
        #img = PhotoImage(file="great.png")    #Need to change this image
        #labelimage.configure(image=img) 
        #labelimage.image = img
        labelresulttext.configure(text="You Have Normal Vision")

    else:
        #img = PhotoImage(file="bad.png")    #Need to change this image
        #labelimage.configure(image=img)
        #labelimage.image = img
        labelresulttext.configure(text="You Have Red-Green Blindness")

def calc():
    global indexes,user_answer,normal_answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == normal_answers[i]:
            score = score+1
        x += 1
    print(score)
    showresult(score)
    
ques = 1
def selected():
    global lblQuestion,r1, user_answer, x
    global ques
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_text = r.listen(source)
        try:
            x = r.recognize_google(audio_text)
            user_answer.append(x)
        
        except:
           user_answer.append("")

    if ques < len(plates): 
        plate_change = PhotoImage(file = plates[indexes[ques]]+'.png')
        lblQuestion.config(image = plate_change)
        lblQuestion.img = plate_change
        r1['text'] = "Record"
        ques += 1

    else: 
        calc()

def startquiz():
    global lblQuestion, r1
    photo = PhotoImage(file = plates[indexes[0]]+".png")
    lblQuestion = Label(
        root,
        image = photo,
        background = "#ffffff"
    )
    lblQuestion.image = photo
    lblQuestion.pack(pady=(100,30))

    r1 = Radiobutton(
        root,
        text = "Record",
        font = ("Times",12),
        value = 0,
        indicator = 0,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(fill = X, pady=5)


def startIspressed():
    labelbackground.destroy()
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title('Ishihara Test')
root.geometry('411x650')
root.config(background = "#ffffff")
root.resizable(0,0)

back_image = PhotoImage(file="Background.png")   #This is for background image
labelbackground = Label(root, image=back_image)
labelbackground.grid(row=0, column=0)


img1 = PhotoImage(file="1.png")    #This is for logo

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff"
)
labelimage.grid(row=0,column=0,sticky='N',pady=120)

labeltext = Label(
    root,
    text = "Ishihara Test",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.grid(row=0,column=0,sticky='S',pady=245)


img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.grid(row=0,column=0,sticky='S',pady=150)

lblInstruction = Label(
    root,
    text = "Press Record Button and record your responses\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",10),
)
lblInstruction.grid(row=0,column=0,sticky='S',pady=80)

lblRules= Label(
    root,
    text = "This test examines if you have color vision deficiency\nSelect teh record button to record your responses\nMake sure you are near to your microphone\nAlso, your background is silent",
    width = 100,
    font = ("Times",14),
    wraplength = 50,
    justify = "center",
    background =  "#000000",
    foreground = "#FACA2F",
)
#lblRules.grid(row=0,column=0,sticky='S',pady=20)
    
root.mainloop()
