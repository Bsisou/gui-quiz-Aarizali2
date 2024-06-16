from tkinter import*
from typing import Self
from PIL import Image, ImageTk

class Quizstarter:
  
  def __init__(self, parent):

    self.parent = parent
    self.selected_option = IntVar() #selection option stored in an integer variable
   

    #self.options_questions = [
       # {"allpage.png": "ronaldinho.png", "options": ["Ronaldo", "Ronaldino", "Ronaldinho", "Pogba"], "answer":3}
    #]

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

  #show backgrond for all pages
  def show_background(self, parent):
      all_page_image_path = "allpage.png"
      all_page_image = Image.open(all_page_image_path)
      all_page_image = all_page_image.resize((700,450),Image.LANCZOS)
      self.all_page_image = ImageTk.PhotoImage(all_page_image)
      self.photoLabel2 = Label(self.parent, image=self.all_page_image)    
      self.photoLabel2.place(x=0,y=0, relheight=1, relwidth= 1)
    
     
      #self.options_question()

  #def options_question(self):
      #question = self.options_questions

  #update player image
      #player_image_path = ["allpage.png"]
      #player_image = Image.open(player_image_path)
      #player_image = player_image.resize((200,200),Image.LANCZOS)
      #self.player_image = ImageTk.PhotoImage(player_image)
      #self.photoLabel2 = Label(self.parent, image=self.player_image)  
      #self.photoLabel2.place(x=275,y=50)
  

    #creating radio buttons for users to answer the question
      option1 = Radiobutton(parent, text="ronaldo", variable=self.selected_option, value=3)

 #place radiobuttons
      option1.place(x=140, y=400)

      option2 = Radiobutton(parent, text="pogba", variable=self.selected_option, value=2)
    
      option2.place(x=140, y=440)

      option3 = Radiobutton(parent, text="Ronaldinho", variable=self.selected_option, value=3)

      option3.place(x=540, y=440)

      option4 = Radiobutton(parent, text="messi", variable=self.selected_option, value=4)

      option4.place(x=540, y=400)

    
     #submit answer button
      submit_button = Button(parent, text="Submit", bg="white", command=self.check_answer)
      submit_button.place(x=340, y=460)

      self.score_label = Label(parent, text="Score: 0", font=("Arial", 14))
      self.score_label.place(x=100, y=80)

      self.feedback_label = Label(parent, fg="green", font=("Arial", 12))
      self.feedback_label.place(x=340,y=425)


  
      #getting submit button to work
  def check_answer(self):
        #the value 3 is for the correct answer 
         correct_answer_value=3
         user_answer = self.selected_option.get()
    
         if user_answer == correct_answer_value:
            self.feedback_label.config(text="Correct! You guessed right",fg="green")
            #add 1 score every correct answer
            self.score =1
            self.score_label.config(text=f"Score: {self.score}")
         else:
            self.feedback_label.config(text="Incorrect! You guessed wrong",fg="red")

            #this means it takes around 2 seconds to go to the next question page
        # self.parent.after(2000, self.show_next_question)
  def show_next_question(self):       
              #destroy the first question page and make new one
      self.parent.destroy()
      quiz=Tk()
      quiz.title("second question page")
      quiz.geometry("750x550")
                            


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


