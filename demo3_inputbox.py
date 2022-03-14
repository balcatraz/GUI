import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # configure the main window
        self.main_window.geometry("240x64")
        self.main_window.title("Button Demo")

        # create and config frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        # create and config labels
        self.prompt_lbl = tkinter.Label(
            self.top_frame, text="Enter a distance in Kilometers:"
        )
        self.prompt_lbl.pack(side="left")

        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
        self.kilo_entry.pack(side="left")

        # create and config button
        self.button = tkinter.Button(
            self.main_window, text="Convert", command=self.convert
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.button.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214

        tkinter.messagebox.showinfo(
            "Results",
            str(kilo) + " kilometers is equal to " + str(round(miles, 2)) + " miles.",
        )


def main():
    my_gui = MyGUI()


main()
