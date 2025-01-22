#-------------------------QR Code Genertor----------------------------------
#-------------------------BY Smriti Sinha-----------------------------------
# ------------------------Importing Modules---------------------------------

import qrcode, PIL
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


# -------------------------Defining Command Functions----------------------

def createQR(*args):
    data = text.get()

    if data:
        img = qrcode.make(data)  # QR code
        resized_image = img.resize((280, 250))
        tkimage = ImageTk.PhotoImage(resized_image)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        canvas.image = tkimage
    else:
        messagebox.showinfo("Error!, Enter valid data")


def saveQR(*args):
    data = text.get()

    if data:
        img = qrcode.make(data)  # QR code
        resized_image = img.resize((280, 250))

        pth = filedialog.asksaveasfilename(defaultextension=".png")

        if pth:
            resized_image.save(pth)
            messagebox.showinfo("QR code saved successfully")
    else:
        messagebox.showinfo("Error!, Enter valid data")


# -------------------------Code For GUI--------------------------------------

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x380")
root.config(bg="#8bbed6")
root.resizable(0, 0)

F1 = tk.Frame(root, bd=2, relief="raised")
F1.place(x=10, y=10, width=280, height=250)

F2 = tk.Frame(root, bd=2, relief="sunken")
F2.place(x=10, y=270, width=280, height=100)

image = tk.PhotoImage(file="C:\\Users\\DELL\\OneDrive\\Desktop\\projects\\QR_code_generator\\WELCOME (2) (1).png")

canvas = tk.Canvas(F1)
canvas.create_image(0, 0, anchor=tk.NW, image=image)
canvas.image = image
canvas.bind("<Double-1>", saveQR)

canvas.pack(fill=tk.BOTH)

text = ttk.Entry(F2, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
text.bind("<Return>", createQR)
text.place(x=5, y=5)

button1 = ttk.Button(F2, text="Create", width=10, command=createQR)
button1.place(x=25, y=50)

button2 = ttk.Button(F2, text="Save", width=10, command=saveQR)
button2.place(x=100, y=50)

button3 = ttk.Button(F2, text="Exit", width=10, command=root.quit)
button3.place(x=175, y=50)

root.mainloop()
