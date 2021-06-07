import webbrowser
import tkinter
from tkinter import *
#importing the needed modules for this assignment

class ParentWindow(Frame):
    #creating a window with Tkinter that will house my custom GUI
    def __init__ (self, master):
        Frame.__init__(self)
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(1400, 400))
        self.master.title('Custom HTML Site!')
        self.master.config(bg='lightgray')
#named my window above and sized it as well as picked colors
        #created a variable for my Custom Text
        self.CustomText = StringVar()
#created a label that tells the user what the text they enter will do once the submit button is clicked
        self.lblCustomText = Label(self.master, text = 'Type in text and click submit to see it created as a webpage!', font = ("Helvetica", 16), fg = 'black', bg = 'lightgray')
        self.lblCustomText.grid(row = 0, column = 0, padx = (30, 0), pady = (30, 0))
#space created for user to enter their text
        self.txtCustomText = Entry(self.master, text = self.CustomText, font = ("Helvetica", 16), fg = 'black', bg = 'lightblue')
        self.txtCustomText.grid(row = 0, column = 1, padx = (30, 0), pady = (30, 0))
#created both a submit button and a cancel button
        self.btnSubmit = Button(self.master, text = "Submit", width = 10, height = 2, command = self.submit)
        self.btnSubmit.grid(row = 1, column = 1, padx = (0, 0), pady = (30, 0), sticky = NE)

        self.btnCancel = Button(self.master, text = "Cancel", width = 10, height = 2, command = self.cancel)
        self.btnCancel.grid(row = 1, column = 1, padx = (0, 90), pady = (30, 0), sticky = NE)

    def submit(self):
        #ct is equal to whatever String of text the user typed into the text box
        ct = self.CustomText.get()
        #f is set to trigger a function that creates a new html page
        f = open('CustomTextSite.html', 'w')

        content =     """
                        <html>
                            <body>
                                <h1>
                                    {}
                                </h1>
                            </body>
                        </html>
                      """.format(ct)#the basic framework for an html page is created and the .format is used to insert the custom text into the correct part of the html code so it will display properly
        f.write(content)
        f.close()
        webbrowser.open_new_tab('CustomTextSite.html')#opens the newly created custom web page in the users browser

    def cancel(self):
            self.master.destroy()

            
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
