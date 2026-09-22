# this shit is so dead cause i dont know how openutau works adsfdsaydguk

import re
import tkinter as tk

root=tk.Tk()

# setting the windows size
root.geometry("600x400")
 
# declaring string variable

sentence_var=tk.StringVar()

 
# i dont understand shit

def hell(text):
    processing_text = text

    processing_text = processing_text.replace("Java", "Python")

    fixes = {
        "im": "I'm",
        "arent": "aren't",
        "cant": "can't",
        "couldnt": "couldn't",
        "didnt": "didn't",
        "doesnt": "doesn't",
        "dont": "don't",
        "hadnt": "hadn't",
        "hasnt": "hasn't",
        "havent": "haven't",
        "isnt": "isn't",
        "mustnt": "mustn't",
        "neednt": "needn't", 
        "oughtnt": "oughtn't", # who says this
        "shant": "shan't",
        "shouldnt": "shouldn't",
        "wasnt": "wasn't",
        "werent": "weren't",
        "wont": "won't",
        "wouldnt": "wouldn't",
            
            # this is mandatory trust.
        "french bread": "baguette", 
    }

    for old, new in fixes.items():
        processing_text = re.sub(
            r"\b" + old + r"\b",
            new,
            processing_text,
            flags=re.IGNORECASE
        )

    return processing_text

def submit():
    print("inputted: " + sentence_var.get())
    print("post processing input: " + hell(sentence_var.get()))
    sentence_var.set("")   
    
    
sentence_lable = tk.Label(root, text = 'sentence', font = ('calibre',10,'bold'))
 
# creating a entry for sentence
sentence_entry=tk.Entry(root, textvariable = sentence_var, font = ('calibre',10,'normal'))
 
# creating a button using the widget 
# button that will call the submit function 
sub_btn=tk.Button(root,text = 'Submit', command = submit)
 
# placing the label and entry in
# the required position using grid
# method
sentence_lable.grid(row=0,column=0)
sentence_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)

# honestly dont understands shit but this apparently
# makes it work with the enter key so im happy
root.bind("<Return>", lambda event: submit())

# performing an infinite loop 
# for the window to display
root.mainloop()
