import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.word = self.get_word()
        self.current = self.get_start_string()
        self.pack()
        self.create_widgets()
        self.get_word()

    def get_word(self):
        data = ["Africa", "America", "Asia", "Europe"]
        return data[random(0, len(data) - 1)]

    def get_start_string(self):
        return "".join("-" for x in self.word)

    def create_widgets(self):
        # info label
        self.info_label = tk.Label(self, text="hangmanJack", fg="blue")
        self.info_label.pack(side="top")

        # Words
        self.info_label = tk.Label(self, fg="green")
        self.info_label.pack(side="top")

        # Input
        self.city_input = tk.Entry(self)
        self.city_input.pack(side="top")

        # request button
        self.request_button = tk.Button(self, text="submit", fg="green", command=self.submit)
        self.request_button.pack(side="top")

        # Error message
        self.info_label = tk.Label(self, fg="red")
        self.info_label.pack(side="top")
        
        # Life status
        self.info_label = tk.Label(self, text="Lifes left: 10", fg="blue")
        self.info_label.pack(side="top")

        # exit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()


