from tkinter import *
from tkinter import filedialog
from Acquisition import *

tkinter = Tk()
strvar = StringVar()
file = Entry(tkinter,width=50)
file.place(x=14,y=150)

def file_browse():
    path= filedialog.askopenfilename()
    file.delete(0,END)
    file.insert(0,path)
    global strvar
    strvar = path

def process():
    global strvar
    print(strvar)
    Acquisition_Lesion(strvar)

def ui():
    tkinter.title("Acquisition of Brain Matters and Lesion")
    tkinter.geometry("500x200")
    tkinter.resizable(0,0)
    Label(tkinter, text='Please upload your image',font = "Helvetica 16 bold",fg="green").place(x=110,y=50)
   
    Button(tkinter,text = "Browse",command=file_browse).place(x=330,y=150)
    Button(tkinter,text="Submit",command=process).place(x=400,y=150)
    tkinter.mainloop()
    
   
if __name__ == "__main__":
    try:
        ui()
    except Exception as error:
        print(error)
