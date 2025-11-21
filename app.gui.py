import tkinter

main = tkinter.Tk()

main.geometry("500x400")

label = tkinter.Label(main, text="Välkomne till påsen!")
label.pack()

quit_button = tkinter.Button(main, text="Avsluta", command=main.quit)
quit_button.pack(pady=20)

imputtext = tkinter.Entry(main)
imputtext.pack(pady=10)

text_box = tkinter.Text(main, height=10, width=40)
text_box.pack()

def add_to_bag(event=None):
    text_box.insert(tkinter.END, imputtext.get() + "\n")

add_button = tkinter.Button(main, text="Lägg till i påsen", command=add_to_bag)
add_button.pack(pady=10)

main.mainloop()
