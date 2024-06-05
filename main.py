from tkinter import*
from typing import Self
from PIL import Image, ImageTk

class Quizstarter:
  
  def __init__(self, parent):

    self.parent = parent
    self.selected_option = IntVar() #selection option stored in an integer variable
  
             #Button       
    self.next_button = Button(parent, text="Next", bg="#b8b4b4",command=self.show_questions)
 
    self.next_button.place(x=720, y=535,anchor="se")

    #name entry box
    self.entry_box = Entry(parent)
    self.entry_box.place(x=370, y=444, anchor="center")   


  


  #hide first page``
  def show_questions(self):
    photoLabel.destroy()
    self.entry_box.destroy()
    self.next_button.destroy()
    self.show_background(self.parent)

  #show backgrond for second page
  def show_background(self, parent):
      second_page_image_path = "secondpage.png"
      second_page_image = Image.open(second_page_image_path)
      second_page_image = second_page_image.resize((700,450),Image.LANCZOS)
      self.second_page_image = ImageTk.PhotoImage(second_page_image)
      self.photoLabel2 = Label(self.parent, image=self.second_page_image)    
      self.photoLabel2.place(x=0,y=0, relheight=1, relwidth= 1)


    #creating radio buttons for users to answer the question
      option1 = Radiobutton(parent, text="Ronaldo", variable=self.selected_option, value=1)

 #place radiobuttons
      option1.place(x=140, y=400)
    

if __name__ == "__main__":
 quiz =Tk()
 quiz.title("Guess the footballer")
 quiz.geometry("750x550")
 #window cann't be resized
 quiz.resizable(False, False)
  #load and place background image
 image_path =("startingpage.png")
 image_path = Image.open(image_path)
 image_path = image_path.resize((760, 540), Image.LANCZOS) 
 image_path = ImageTk.PhotoImage(image_path)
 photoLabel = Label(quiz, image=image_path)
 photoLabel.place(x=0,y=0, relheight= 1, relwidth= 1)

#create the quiz starter object
 Quizstarter_object = Quizstarter(quiz) 
 Quizstarter_object.photoLabel2 = photoLabel
 quiz.mainloop()#window doesn't dissapear


