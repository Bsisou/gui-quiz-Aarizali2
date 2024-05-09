import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()

image_path =("startingpage.png")
image_path = Image.open(image_path)
image_path = image_path.resize((450, 350), Image.LANCZOS) 
image_path = ImageTk.PhotoImage(image_path)

label = tk.Label(root, image=image_path)
label.pack()



root.mainloop()