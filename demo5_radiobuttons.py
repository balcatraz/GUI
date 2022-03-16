import tkinter
import tkinter.messagebox
from tkinter.ttk import Radiobutton


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # configure the main window
        self.main_window.geometry("240x136")
        self.main_window.title("Radio Button Demo")

        # create and config frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.btm_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side="top")
        self.btm_frame.pack(side="top")

        # create and config radio buttons
        self.radiovar = tkinter.IntVar()

        self.radiovar.set(1)

        self.rb1 = tkinter.Radiobutton(
            self.top_frame, text="Option 1", variable=self.radiovar, value=1
        )
        self.rb2 = tkinter.Radiobutton(
            self.top_frame, text="Option 2", variable=self.radiovar, value=2
        )
        self.rb3 = tkinter.Radiobutton(
            self.top_frame, text="Option 3", variable=self.radiovar, value=3
        )

        self.rb1.pack(side="top")
        self.rb2.pack(side="top")
        self.rb3.pack(side="top")

        # create and config button
        self.button = tkinter.Button(
            self.btm_frame, text="OK", command=self.show_choice
        )

        self.button2 = tkinter.Button(
            self.btm_frame, text="Reset", command=self.rb1.select
        )

        self.quit_button = tkinter.Button(
            self.btm_frame, text="Quit", command=self.main_window.destroy
        )

        self.button.pack(side="left")
        self.button2.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo(
            "Selection", "You have selected option " + str(self.radiovar.get()) + "."
        )


def main():
    my_gui = MyGUI()


main()
