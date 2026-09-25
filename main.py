import re
import tkinter as tk

root=tk.Tk()

# self explanatory

root.geometry("600x400")
sentence_var=tk.StringVar()

 
# i dont understand shit
def text_correction_function_because_people_are_really_fucking_lazy(text):
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
            
            # this is mandatory trust me.
        "french bread": "baguette", 
    }


    for old, new in fixes.items():
        processing_text = re.sub(
            r"\b" + old + r"\b",
            new,
            processing_text,
            flags = re.IGNORECASE
        )

    return processing_text

def submit():
    print("inputted: " + sentence_var.get())
    print("post processing input: " + text_correction_function_because_people_are_really_fucking_lazy(sentence_var.get()))
    sentence_var.set("")   
    
    
sentence_label = tk.Label(root, text = 'sentence, acronyms unsupported due to the nature of the auto correct', font = ('calibre',10,'bold'))
sentence_entry=tk.Entry(root, textvariable = sentence_var, font = ('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit)
sentence_label.grid(row=0,column=0)
sentence_entry.grid(row=1,column=0)
sub_btn.grid(row=2,column=0)

# honestly dont understands shit but this apparently
# makes it work with the enter key so im happy
root.bind("<Return>", lambda event: submit())
root.mainloop() # dont know what this means but without it the thing just dies
