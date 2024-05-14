from tkinter import*
from PIL import Image, ImageTk

class Quizstarter:
  def __init__(self, root):
    
     

             #Button       
    self.continue_button = Button(root, text="Next", bg="#b8b4b4")
    self.continue_button.place(x=414, y=378)

    
 
if __name__ == "__main__":
 root =Tk()
 root.title("Guess the footballer")
 root.geometry("500x450")
  #load and place background image
 image_path =("startingpage.png")
 image_path = Image.open(image_path)
 image_path = image_path.resize((500, 450), Image.LANCZOS) 
 image_path = ImageTk.PhotoImage(image_path)
 photoLabel = Label(root, image=image_path)
 photoLabel.place(x=0,y=0, relheight= 1, relwidth= 1)

#create the quiz starter object
 Quizstarter_object = Quizstarter(root) 
  
 root.mainloop()#window doesn't dissapear