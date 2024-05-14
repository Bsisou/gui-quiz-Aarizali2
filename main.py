from tkinter import*
from typing import Self
from PIL import Image, ImageTk

class Quizstarter:
  def __init__(self, parent):
    
    background_color = "OldLace"
      #frame set up
    self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
    self.quiz_frame.grid()
  

      
    #label widget for our heading
    self.heading_label = Label(self.quiz_frame, text = "Welcome to my quiz!", font=("Tw Cen MT", "18", "bold"))
   
    self.heading_label.place(x=100, y=100)
    
    self.user_label  = Label(self.quiz_frame, text="Please enter your name: ", font=("Tw Cen MT", "16"))
    self.user_label.grid(row=1)                


 #user input is taken by an entry widget
    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=2)

                    
    self.continue_button = Button(self.quiz_frame, text="Continue", bg="blue")
    self.continue_button.grid(row=3, pady=20)




if __name__ == "__main__":
 root =Tk()
 root.title("Guess the footballer")
 Quizstarter_object = Quizstarter(root)
 image_path =("startingpage.png")
 image_path = Image.open(image_path)
 image_path = image_path.resize((450, 350), Image.LANCZOS) 
 image_path = ImageTk.PhotoImage(image_path)
 photoLabel = Label(root, image=image_path)
 photoLabel.place(x=0,y=0, relheight= 1, relwidth= 1)
 root.mainloop()#window doesn't dissapear