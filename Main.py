import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.title('PNG To JPG Converter')

canv1 = tk.Canvas(root, width=301, height=251, bg='yellow', relief='raised')
canv1.pack()

label = tk.Label(root, text='File Conversion Tool', bg='green')
label.config(font=('helvetica', 20))
canv1.create_window(151, 61, window=label)


def getPNGFile():
    global img1
    global rgb
    import_file_path = filedialog.askopenfilename()
    img1 = Image.open(import_file_path)
    rgb = img1.convert('RGB')

browseButton_PNGFile = tk.Button(text=" Import PNG File ", command=getPNGFile, bg='blue', fg='white',
                                 font=('helvetica', 12, 'bold'))
canv1.create_window(151, 131, window=browseButton_PNGFile)


def convertToJPGFile():
    global img1
    global rgb
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    rgb.save(export_file_path)


saveAsButton_JPGFile = tk.Button(text='Convert PNG to JPG', command=convertToJPGFile, bg='blue', fg='white',
                                 font=('helvetica', 12, 'bold'))
canv1.create_window(151, 181, window=saveAsButton_JPGFile)

root.mainloop()
