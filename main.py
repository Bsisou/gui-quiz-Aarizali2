from tkinter import*
from PIL import Image, ImageTk

class Quizstarter:
  
  def __init__(self, parent):

    self.parent = parent
  
             #Button       
    self.next_button = Button(parent, text="Next", bg="#b8b4b4",command=self.show_questions)
 
    self.next_button.place(x=570, y=478)

    #name entry box
    self.entry_box = Entry(parent)
    self.entry_box.place(x=350, y=444)   

  #hide first page
  def show_questions(self):
    photoLabel.destroy()
    self.entry_box.destroy()
    self.next_button.destroy()
    self.show_background(self.parent)


  #show backgrond for second page
  def show_background(self, parent):
      second_page_image_path = "secondpage.png"
      second_page_image = Image.open(second_page_image_path)
      second_page_image = second_page_image.resize((500,450),Image.LANCZOS)
      self.second_page_image = ImageTk.PhotoImage(second_page_image)
      self.photoLabel2 = Label(self.parent, image=self.second_page_image)    
      self.photoLabel2.place(x=0,y=0, relheight=1, relwidth= 1)


if __name__ == "__main__":
 quiz =Tk()
 quiz.title("Guess the footballer")
 quiz.geometry("500x450")
  #load and place background image
 image_path =("startingpage.png")
 image_path = Image.open(image_path)
 image_path = image_path.resize((500, 450), Image.LANCZOS) 
 image_path = ImageTk.PhotoImage(image_path)
 photoLabel = Label(quiz, image=image_path)
 photoLabel.place(x=0,y=0, relheight= 1, relwidth= 1)

#create the quiz starter object
 Quizstarter_object = Quizstarter(quiz) 
 Quizstarter_object.photoLabel2 = photoLabel
 quiz.mainloop()#window doesn't dissapear


