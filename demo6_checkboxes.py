from email import message
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

        # create and config check boxes
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.top_frame, text="Option 1", variable=self.cb_var1
        )
        self.cb2 = tkinter.Checkbutton(
            self.top_frame, text="Option 2", variable=self.cb_var2
        )
        self.cb3 = tkinter.Checkbutton(
            self.top_frame, text="Option 3", variable=self.cb_var3
        )

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # create and config button
        self.button = tkinter.Button(
            self.btm_frame, text="OK", command=self.show_choice
        )

        self.quit_button = tkinter.Button(
            self.btm_frame, text="Quit", command=self.main_window.destroy
        )

        self.button.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def show_choice(self):
        self.message = "You have selected:\n"

        if self.cb_var1.get():
            self.message += "1\n"
        if self.cb_var2.get():
            self.message += "2\n"
        if self.cb_var3.get():
            self.message += "3\n"

        tkinter.messagebox.showinfo("Selection", self.message)


def main():
    my_gui = MyGUI()


main()
