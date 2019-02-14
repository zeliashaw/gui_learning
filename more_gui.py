import tkinter

def say_hi():
    print("hi")

root = tkinter.Tk()

root.title("hello world")
root.geometry("600x200")

button1 = tkinter.Button(root)
button1.config(text="say hi", fg="#3CE8BD", command=say_hi)
button1.grid()


root.mainloop()