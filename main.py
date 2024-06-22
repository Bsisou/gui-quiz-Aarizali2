from tkinter import *
from typing import Self
from PIL import Image, ImageTk




class Quizstarter:

  def __init__(self, parent):

      self.parent = parent
      self.selected_option = IntVar()#selection option stored in an integer variable
      self.all_page_bg_image = "allpage.png"
    #self.quiz_page_bg_image = 
      self.options_questions = [
      {
        "question_image":
        "ronaldinho.png",
        "options": ["Ronaldo", "Ronaldino", "Ronaldinho", "Pogba"],
        "answer":
        3
    },
      {
          "question_image":
          "mbappe.png",
          "options": ["Ronaldo", "Ronaldino", "Mbappe", "Pogba"],
          "answer":
          3
      }
                             ]


      self.current_question_index = 0
      self.photoLabel = None
      self.photoLabel2 = None
      self.entry_box = None
      self.next_button = None    
      self.question_image_label = None  
      self.options_buttons = []
      self.submit_button = None
      self.score_label = None  
      self.feedback_label = None

    #Button
      self.next_button = Button(parent, text="Next",  bg="#b8b4b4",command=self.show_questions)
    
                              
                             
      self.next_button.place(x=720, y=535, anchor="se")

    #name entry box
      self.entry_box = Entry(parent)
      self.entry_box.place(x=370, y=444, anchor="center")

  #hide first page``
  def show_questions(self):
      photoLabel.destroy()
      self.entry_box.destroy()
      self.next_button.destroy()
      self.show_background()

  #show backgrond for all pages
  def show_background(self):
    
      all_page_image_path = "imgs/" + self.all_page_bg_image
      all_page_image = Image.open(all_page_image_path)
      all_page_image = all_page_image.resize((700, 450), Image.LANCZOS)
      self.all_page_image = ImageTk.PhotoImage(all_page_image)
      self.photoLabel2 = Label(self.parent, image=self.all_page_image)
      self.photoLabel2.place(x=0, y=0, relheight=1, relwidth=1)

    
      self.show_next_questions()
    
  def show_next_questions(self):
      if self.current_question_index < len(self.options_questions):
        question_data = self.options_questions[self.current_question_index]
 
    

   #show question image 

      self.question_image_path = Image.open("imgs/" + question_data["question_image"])
      self.question_image = ImageTk.PhotoImage(self.question_image_path.resize((100, 100), Image.LANCZOS))
      self.question_image_label = Label(self.parent, image=self.question_image)
      self.question_image_label.place(relx=0.4, rely=0.3)
   
  

      options = question_data["options"]
      self.options_buttons = []
      for i in range(len(options)):
          option = Radiobutton(self.parent, text=options[i],
          variable=self.selected_option, value =i+1)
          option.place(x=140 +(i% 2) * 400, y=400 + (i // 2) *40)
          self.options_buttons.append(option)


      #  submit answer button
      submit_button = Button(self.parent,text="Submit", bg="white",command=self.check_answer)
      submit_button.place(x=340, y=460)
   

      self.score_label = Label(self.parent, text="Score: 0", font=("Arial", 14))
      self.score_label.place(x=100, y=80)
  
      self.feedback_label = Label(self.parent, fg="green", font=("Arial", 12))
      self.feedback_label.place(x=340, y=425)
   # else:
     # self.show_final_score()
    #getting submit button to work


  def check_answer(self):
    #the value 3 is for the correct answer
      question_data = self.options_questions[self.current_question_index]
      correct_answer_value = question_data["answer"]
      user_answer = self.selected_option.get()

      if user_answer == correct_answer_value:
        self.feedback_label.config(text="Correct! You guessed right", fg="green")
      #add 1 score every correct answer
        self.score = 1
        self.score_label.config(text=f"Score: {self.score}")
      else:
        self.feedback_label.config(text="Incorrect! You guessed wrong", fg="red")

      #this means it takes around 2 seconds to go to the next question page
      self.parent.after(2000, self.options_questions)

 
    #question_number = question_number + 1
    #destroy the first question page and make new one
    


if __name__ == "__main__":
  quiz = Tk()
  quiz.title("Guess the footballer")
  quiz.geometry("750x550")
  #window cann't be resized
  quiz.resizable(False, False)
  #load and place background image
  image_path = ("imgs/startingpage.png")
  image_path = Image.open(image_path)
  image_path = image_path.resize((760, 540), Image.LANCZOS)
  image_path = ImageTk.PhotoImage(image_path)
  photoLabel = Label(quiz, image=image_path)
  photoLabel.place(x=0, y=0, relheight=1, relwidth=1)

  #create the quiz starter object
  Quizstarter_object = Quizstarter(quiz)
  Quizstarter_object.photoLabel2 = photoLabel
  quiz.mainloop()  #window doesn't dissapear
