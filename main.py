print("May take a bit to load.")
print("")
print("Please make sure you have the following installed:")
print(" - g2p_en | pip install g2p-en | https://pypi.org/project/g2p-en/")
print(" - pyUtau | pip install pyutau | https://pypi.org/project/pyutau/")

import re
import tkinter as tk
import pyutau 
from g2p_en import G2p

# stuff im not bothered to fuck with

root=tk.Tk()

conversion = G2p()

root.geometry("600x400")

sentence_var = tk.StringVar()

# camelCase my beloved

fixes = {
        "i": "I",
        # i dont even think this mattters 
        #at all but added it anyway

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
            
        # this is mandatory trust me.
        "french bread": "baguette", 

        # troll
        "Java": "Python"
    }

def text_correction_function_because_people_are_really_fucking_lazy(text):

    processing_text = text

    for old, new in fixes.items():
        processing_text = re.sub(
            r"\b" + re.escape(old) + r"\b",
            new,
            processing_text,
            flags = re.IGNORECASE
        )

    return processing_text
    
def ARPAbetConversion(text):
    postConversion = conversion(text)

    return postConversion

def fileCreator():
    print("the person who made pyUtau is the reason i created test.py")
    pyutau.create_note(lyric="s")


def submit():

    correctedText = text_correction_function_because_people_are_really_fucking_lazy(sentence_var.get())

    print("inputted: " + sentence_var.get())
    print("post processing input: " + correctedText)
    print("ARPAbet output: ", ARPAbetConversion(correctedText))
    sentence_var.set("")   


    
sentence_label = tk.Label(root, text = 'sentence, acronyms unsupported due to the nature of the auto correct', font = ('calibre',10,'bold'))
 
sentence_entry=tk.Entry(root, textvariable = sentence_var, font = ('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit)

sentence_label.grid(row=0,column=1)
sentence_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

# honestly dont understands shit but this apparently
# makes it work with the enter key so im happy
root.bind("<Return>", lambda event: submit())

root.mainloop()
