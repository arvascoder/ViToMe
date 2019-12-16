import tkinter
import tkinter.ttk
import random

class Application(tkinter.ttk.Frame):
    def __init__(self, master = None):
    super().__init__(master)
    self.pack()
    self.create_widgets()
    self.check_verb_list_en = []
    self.check_adj_list_en = []
    self.check_noun_list_en = []
    self.random_int_verb = random.randrange(0, len(verb_list_en)-1)
    self.random_int_adj = random.randrange(0, len(adj_list_en)-1)
    self.random_int_noun = random.randrange(0, len(noun_list_en)-1)

    def create_widgets(self):
        self.MainText = tkinter.Frame(self.master, height = 70, width = 70)
        self.MainText.pack()
        self.Verb = tkinter.Label(self.MainText,text = 'Start' , height=5, width=15, bg='light blue', font=("Comic Sans MS", 14, "bold"))
        self.Verb.pack(side='left')
        self.Verb.bind('<Enter>', self.mouse_in_Verb)
        self.Adj = tkinter.Label(self.MainText,text = 'Start', height=5, width=15, bg='salmon1', font=("Comic Sans MS", 14, "bold"))
        self.Adj.pack(side ='left')
        self.Noun = tkinter.Label(self.MainText, text = 'Start', height=5, width=15, bg='light goldenrod', font=("Comic Sans MS", 14, "bold"))
        self.Noun.pack()
        self.Button = tkinter.Button(self.master, width = 7, text = 'Next', command = self.click_button)
        self.Button.pack()
    def mouse_in_Verb(self,into):
        self.Verb.configure(text = verb_list_ru[random_int_verb])
    def click_button(self):

if len(verb_list_en)==0:
self.random_verb = 'Out of list'
elif len(verb_list_en)==1:
self.random_verb = verb_list_en[0]
else:
random_int_verb = random.randrange(0, len(verb_list_en)-1)
self.random_verb = verb_list_en[random_int_verb]
if len(adj_list_en)==0:
self.random_adj = 'Out of list'
elif len(adj_list_en)==1:
self.random_adj = adj_list_en[0]
else:
random_int_adj = random.randrange(0, len(adj_list_en)-1)
self.random_adj = adj_list_en[random_int_adj]
if len(noun_list_en)==0:
self.random_noun = 'Out of list'
elif len(noun_list_en)==1:
self.random_noun = noun_list_en[0]
else:
random_int_noun = random.randrange(0, len(noun_list_en)-1)
self.random_noun = noun_list_en[random_int_noun]

if self.random_verb in self.check_verb_list_en and self.random_verb != "Out of list": #Тут ошибка, одно совпадение не означает три совпадения
if self.check_verb_list_en.count(self.random_verb) > 1:
verb_list_en.remove('{0}'.format(self.random_verb))
del verb_list_ru[self.random_int_verb]
if self.random_adj in self.check_adj_list_en and self.random_adj != "Out of list":
if self.check_adj_list_en.count(self.random_adj) > 1:
adj_list_en.remove('{0}'.format(self.random_adj))
del adj_list_ru[self.random_int_adj]
if self.random_noun in self.check_noun_list_en and self.random_noun != "Out of list":
if self.check_noun_list_en.count(self.random_noun) > 1:
noun_list_en.remove('{0}'.format(self.random_noun))
del noun_list_ru[self.random_int_noun]

self.check_verb_list_en.append(self.random_verb)
self.check_adj_list_en.append(self.random_adj)
self.check_noun_list_en.append(self.random_noun)

self.Verb.configure(text = self.random_verb)
self.Adj.configure(text = self.random_adj)
self.Noun.configure(text = self.random_noun)
print(self.check_verb_list_en)
print(self.check_adj_list_en)
print(self.check_noun_list_en)


root = tkinter.Tk()
root.resizable(True,True)
root.title('Visualize To Memorize')

file_verb = open(r".verbs.txt")
onstring = file_verb.read().split('\n')[☺
verb_list_en = list()
verb_list_ru = list()
for item in onstring:
key = item.split(' ')[0]
value = item.split(' ')[2☺
verb_list_en.append(key)
verb_list_ru.append(value)
print(verb_list_en, verb_list_ru)
file_verb.close()
file_adj = open(r".adjectives.txt")
onstring = file_adj.read().split('\n')[☺
adj_list_en = list()
adj_list_ru = list()
for item in onstring:
key = item.split(' ')[0]
value = item.split(' ')[2☺
adj_list_en.append(key)
adj_list_ru.append(value)
print(adj_list_en, adj_list_ru)
file_adj.close()
file_noun = open(r".nouns.txt")
onstring = file_noun.read().split('\n')[☺
noun_list_en = list()
noun_list_ru = list()
for item in onstring:
key = item.split(' ')[0]
value = item.split(' ')[2☺
self.click - Domain Name for sale
self.click
noun_list_en.append(key)
noun_list_ru.append(value)
print(noun_list_en, noun_list_ru)
file_noun.close()


app = Application ( master = root )
root.mainloop()