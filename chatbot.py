


# import necessary libs
import nltk
import time
from nltk.chat.util import Chat, reflections
from tkinter import *
from nltk.corpus import treebank


root = Tk()
root.title("Chatbot")


# Inputs and corresponding outputs
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

# Rules input/output

set_pairs = [
        [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello|wsup|sup|helo|greetings|greet|supp|Hello|ello",
        ["Hello", "Hey there", "Hello there, how are you doing?", "Hey, how are you feeling today?", "Hey, tell me what is bothering you today?", "Hello, what do you want to talk about?"]
    ],
    [
        r"what is your name?",
        ["You can call me Freud, I will be your assistant today :)"]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you!", "I am feeling well, thanks!", "I am doing fantastic, thank you!"]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?", "great to hear, what else would you want to talk about?"]
    ],
    [
        r"how can i help you?|what do you do?| what are you doing right now?|what is your purpose?|who even need you?|What is your purpose here?|what you do?|what are you working on right now?|you do what?|when and what do you do?",
        ["i am here to help you and others creating any emotional or mental disorder",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)", "That's good to hear, tell me more about that", "That's really good, tell me more about it"]
    ],
    [
        r"i need a doctor|can you recommend me any good doctor?|what doctors are near me?|please recommend me a doctor|i need a help from doctor|i think i am going to visit a doctor|i'll visit a doctor|i think i should go to doctor|i should go to doctor",
        ["You should contact your local doctor or psychiatrist for further help", "Please contact your local doctor for further help"]
    ],
    [
        r"(.*) thank you so much, that was helpful|thanks for the suggestion.|thanks for suggesting that|yes thanks for suggestion|great suggestion thanks|thanks for that suggestion",
        ["You are more than welcome. Is there anything else i can help you with?", "You are welcome, I'm glad i was able to help. Do you need me for anything else?"]
    ],
    [
        r"quit|Quit|exit|Exit|leave|Leave|Bye|bye|bye bye|Bye Bye|byee|goodbye|see you|see ya|see you later",
        ["Bye, take care :)", "It was nice talking to you, take care :)", "Bye, take care :)"]

],
]



set_pairs2 = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you feeling today?",]
    ],
    [
        r"????",
        ["Hello %1, How are you feeling today?",]
    ],
    [
        r"hi|Hi|Hey|hey|hello|Hello|wsup|Wsup|sup|Sup|good morning|heyy|Heyy|hii|Hii|HEY|HELLO|HII|HI",
        ["Hello, I am Sophia, I will be your assistant today. Please write what is your name or what should i call you: "]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Analytics Vidhya. you can call me crazy!",]
    ],
    [
        r"What are you?|what are you?|Who are you?|who are you?|Who is you?|who is you?",
        ["I'm Sophia, your assistant :)",]
    ],
    [
        r"how are you ?",
        ["I'm doing goodnHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Raghav created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]



# Sigmund Freud - was an Austrian neurologist and the founder of psychoanalysis
bot = "Freud"

# Logical structure
def send():
    send = "You -> "+e.get()
    txt.insert(END, "\n"+send)
    user = e.get().lower()
    if(user == "hello"):
        time.sleep(0.5)
        txt.insert(END, "\n" + bot+" -> Hi")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        time.sleep(0.5)
        txt.insert(END, "\n" + bot+" -> Hello")
    elif(user == "how are you" or user == "how are you?" or user == "how r u?"):
        time.sleep(0.5)
        txt.insert(END, "\n" + bot+" -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        time.sleep(0.5)
        txt.insert(END, "\n" + bot+" -> Great! how can I help you.")
    elif(user == "bad" or user == "sad" or user == "painful" or user == "not great"):
        time.sleep(0.5)
        txt.insert(END, "\n" + bot+" -> Tell me what is bothering you")
    else:
        time.sleep(0.5)
        txt.insert(END, "\n" + bot+" -> Sorry! I dind't got you")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
time.sleep(1)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)


'''
# include paris and reflections rules
def chat():
    chat = Chat(pairs, reflections)
    chat.converse()
# initiate the conversation
if __name__ == "__main__":
    chat()
'''

root.mainloop()








