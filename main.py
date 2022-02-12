import cv2
import pytesseract as tess
import tkinter as tk
from tkinter import filedialog
import threading
import PyPDF2

files= []
directoryPath=""

def warning():
    while(1):
        key=0
        if atDirectory.get() == 1 and directoryPath == "":
            error = tk.Label(frame, text="You have not changed the Directory yet.", bg="red")
            error.place(x=13, y=196)
            key=1
        if atDirectory.get() == 0:
            if key==1:
                error = tk.Label(frame, text="You have not changed the Directory yet.", bg="white", fg="white")
                error.place(x=13, y=196)
                # error.destroy()

def changeDirectory():
    global directoryPath
    directoryPath=filedialog.askdirectory()
    label = tk.Label(frame, text=directoryPath, bg="grey")
    label.pack()

def convertFiles():
    if directoryPath=="":
        for file in files:
            if file.endswith(".png"):
                img=cv2.imread(file)
                text=tess.image_to_string(img)
                newFile=file.rstrip(",.png")
                newFile+=".txt"
                f=open(newFile,"x")
                f.write(text)
                f.close()

            if file.endswith(".jpg"):
                img = cv2.imread(file)
                text = tess.image_to_string(img)
                newFile = file.rstrip(",.jpg")
                newFile+=".txt"
                f = open(newFile, "x")
                f.write(text)
                f.close()
                print("Here")

            if file.endswith(".pdf"):
                pdfObject=open(file,'rb')
                Reader=PyPDF2.PdfFileReader(pdfObject)
                pageObject = Reader.getPage(0)
                text=pageObject.extractText()
                newFile = file.rstrip(",.pdf")
                newFile+=".txt"
                f = open(newFile, "x")
                f.write(text)
                f.close()
                print("Here")

    else:
        for file in files:
            directoryPath1=directoryPath+"/"
            if file.endswith(".png"):
                img = cv2.imread(file)
                text = tess.image_to_string(img)
                newFile = file.rstrip(",.png")
                newFile += ".txt"
                for i in newFile:
                    if i == "/":
                        newFile = newFile[newFile.index(i) + 1:]
                newFile=directoryPath1+newFile
                f = open(newFile, "x")
                f.write(text)
                f.close()

            if file.endswith(".jpg"):
                img = cv2.imread(file)
                text = tess.image_to_string(img)
                pos=0
                newFile = file.rstrip(",.jpg")
                newFile += ".txt"
                for i in newFile:
                    if i == "/":
                        newFile = newFile[newFile.index(i) + 1:]
                newFile = directoryPath1 + newFile
                f = open(newFile, "x")
                f.write(text)
                f.close()
                print("Here")

            if file.endswith(".pdf"):
                pdfObject = open(file, 'rb')
                Reader = PyPDF2.PdfFileReader(pdfObject)
                pageObject = Reader.getPage(0)
                text = pageObject.extractText()
                newFile = file.rstrip(",.pdf")
                newFile += ".txt"
                for i in newFile:
                    if i == "/":
                        newFile = newFile[newFile.index(i) + 1:]
                newFile = directoryPath1 + newFile
                f = open(newFile, "x")
                f.write(text)
                f.close()
                print("Here")


def concatenate():
    text=""
    for file in files:
        if file.endswith(".png"):
            img=cv2.imread(file)
            text+=tess.image_to_string(img)

        if file.endswith(".jpg"):
            img = cv2.imread(file)
            text += tess.image_to_string(img)

        if file.endswith(".pdf"):
            pdfObject=open(file,'rb')
            Reader=PyPDF2.PdfFileReader(pdfObject)
            pageObject = Reader.getPage(0)
            text+=pageObject.extractText()

        text+="\n\n\n\n"

    if directoryPath== "":
        newFile="Master.txt"
        f = open(newFile, "x")
        f.write(text)
        f.close()
    else:
        newFile = directoryPath
        newFile+="\Master.txt"
        f = open(newFile, "x")
        f.write(text)
        f.close()

#Opening a File:
def addFile():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("Images", "*.jpg; *.png"), ("PDFs", "*.pdf")))
    files.append(filename)
    #print(files)

    label = tk.Label(frame, text=filename, bg="white")
    label.pack()

#GUI:
root = tk.Tk()

canvas = tk.Canvas(root, height=300, width=300, bg="#5680E9")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

atDirectory = tk.IntVar()
tick=tk.Checkbutton(root,text="Converted files at specified Directory", variable=atDirectory, onvalue=1, offvalue=0)
tick.place(x=40, y=248)

OpenFile = tk.Button(root, text="Open File", padx=5, pady=2, fg="white", bg="#8860D0", command=addFile)
OpenFile.place(x=40, y=274)

toText = tk.Button(root, text="Convert", padx=5, pady=2, fg="white", bg="#8860D0", command=convertFiles)
toText.place(x=110, y=274)

concatenate= tk.Button(root, text="Concatenate", padx=5, pady=2, fg="white", bg="#8860D0", command=concatenate)
concatenate.place(x=172, y=274)

changeDirectory=tk.Button(root, text="Change Directory", padx=5, pady=2, fg="white", bg="#8860D0", command=changeDirectory)
changeDirectory.place(x=101, y=2)

x = threading.Thread(target=warning)
x.start()

root.mainloop()
