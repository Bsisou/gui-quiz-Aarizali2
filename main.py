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


      option2 = Radiobutton(parent, text="Ronaldino", variable=self.selected_option, value=2)
    
      option2.place(x=140, y=440)


      option3 = Radiobutton(parent, text="Ronaldinho", variable=self.selected_option, value=3)

      option3.place(x=540, y=440)

      option4 = Radiobutton(parent, text="Pogba", variable=self.selected_option, value=4)

      option4.place(x=540, y=400)

    
     #submit answer button
      submit_button = Button(parent, text="Submit", bg="white", command=self.check_answer)
      submit_button.place(x=340, y=460)


      self.feedback_label = Label(parent, fg="green", font=("Arial", 12))
      self.feedback_label.place(x=340,y=425)


  
      #getting submit button to work
  def check_answer(self):
         correct_answer_value=3
         user_answer = self.selected_option.get()
    
         if user_answer == correct_answer_value:
            self.feedback_label.config(text="Correct!",fg="green")
         else:
            self.feedback_label.config(text="Incorrect!",fg="red"


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


