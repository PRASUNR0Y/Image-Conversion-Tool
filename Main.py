import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.title('Image Conversion Tool')

canv1 = tk.Canvas(root, width=301, height=251, bg='yellow', relief='raised')
canv1.pack()

label = tk.Label(root, text='Image Conversion Tool', bg='green')
label.config(font=('helvetica', 20))
canv1.create_window(151, 61, window=label)


def getPNGFile():
    global img1
    import_file_path = filedialog.askopenfilename()
    img1 = Image.open(import_file_path)


browseButton_PNGFile = tk.Button(text=" Import File ", command=getPNGFile, bg='blue', fg='white',
                                 font=('helvetica', 12, 'bold'))
canv1.create_window(151, 131, window=browseButton_PNGFile)


def convertToJPGFile():
    global img1
    global rgb
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    rgb = img1.convert('RGB')
    rgb.save(export_file_path)


def convertToPNGFile():
    global img1
    global rgba
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    rgba = img1.convert('RGBA')
    rgba.save(export_file_path)


saveAsButton_JPGFile = tk.Button(text='Convert to JPG & Save', command=convertToJPGFile, bg='blue', fg='white',
                                 font=('helvetica', 12, 'bold'))
canv1.create_window(151, 181, window=saveAsButton_JPGFile)

saveAsButton_PNGFile = tk.Button(text='Convert to PNG & Save', command=convertToPNGFile, bg='blue', fg='white',
                                 font=('helvetica', 12, 'bold'))
canv1.create_window(151, 220, window=saveAsButton_PNGFile)

root.mainloop()
