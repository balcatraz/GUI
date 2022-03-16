from email import message
import tkinter
import tkinter.messagebox
from tkinter.ttk import Radiobutton
from turtle import color


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # configure the main window
        self.main_window.geometry("240x136")
        self.main_window.title("Student Test Average")
        self.main_window.configure(background="gray")

        # create and config frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame1 = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.mid_frame3 = tkinter.Frame(self.main_window)
        self.btm_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side="top")
        self.mid_frame1.pack(side="top")
        self.mid_frame2.pack(side="top")
        self.mid_frame3.pack(side="top")
        self.btm_frame.pack(side="top")

        self.top_frame.configure(background="gray")
        self.mid_frame1.configure(background="gray")
        self.mid_frame2.configure(background="gray")
        self.mid_frame3.configure(background="gray")
        self.btm_frame.configure(background="gray")

        # create and config check boxes
        self.prompt_lbl1 = tkinter.Label(
            self.top_frame, text="Enter the score for test 1:"
        )
        self.prompt_lbl2 = tkinter.Label(
            self.mid_frame1, text="Enter the score for test 2:"
        )
        self.prompt_lbl3 = tkinter.Label(
            self.mid_frame2, text="Enter the score for test 3:"
        )

        self.prompt_lbl1.pack(side="left")
        self.prompt_lbl2.pack(side="left")
        self.prompt_lbl3.pack(side="left")

        self.prompt_lbl1.configure(background="gray", font="arial", fg="white")
        self.prompt_lbl2.configure(background="gray", font="arial", fg="white")
        self.prompt_lbl3.configure(background="gray", font="arial", fg="white")

        self.grade_entry1 = tkinter.Entry(self.top_frame, width=10)
        self.grade_entry1.pack(side="right")
        self.grade_entry2 = tkinter.Entry(self.mid_frame1, width=10)
        self.grade_entry2.pack(side="right")
        self.grade_entry3 = tkinter.Entry(self.mid_frame2, width=10)
        self.grade_entry3.pack(side="right")

        # create and config show average
        self.descr_lbl = tkinter.Label(self.mid_frame3, text="Average:")
        self.descr_lbl.pack(side="left")
        self.avg_var = tkinter.StringVar()
        self.avg_lbl = tkinter.Label(self.mid_frame3, textvariable=self.avg_var)
        self.avg_lbl.pack(side="right")

        self.descr_lbl.configure(background="gray", font="arial", fg="white")
        self.avg_lbl.configure(background="gray", font="arial", fg="white")
        # create and config button
        self.button = tkinter.Button(
            self.btm_frame, text="Average", command=self.average
        )

        self.quit_button = tkinter.Button(
            self.btm_frame, text="Quit", command=self.main_window.destroy
        )

        self.button.pack(side="left")
        self.quit_button.pack(side="right")

        self.button.configure(background="gray", font="arial", fg="white")
        self.quit_button.configure(background="gray", font="arial", fg="white")

        tkinter.mainloop()

    def average(self):
        avg = (
            float(self.grade_entry1.get())
            + float(self.grade_entry2.get())
            + float(self.grade_entry3.get())
        ) / 3.0

        self.message = str(round(avg, 2))

        self.avg_var.set(self.message)


def main():
    my_gui = MyGUI()


main()
