import tkinter
root = tkinter.Tk()

root.title("hello world")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="Purpelicious", fg="purple", font=("Times", "50", "bold"))
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="asdfghjkl", fg="blue", justify="left")
my_label.grid()


root.mainloop()
