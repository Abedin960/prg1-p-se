import tkinter

main = tkinter.Tk()

main.geometry("500x400")

label = tkinter.Label(main, text="Välkomne till påsen!")
label.pack()


quit_button = tkinter.Button(main, text="Avsluta", command=main.quit)
quit_button.pack(pady=20)


input_entry = tkinter.Entry(main)
input_entry.pack(pady=10)
input_entry.focus_set()

text_box = tkinter.Text(main, height=10, width=40)
text_box.pack()

inventory = []

def add_to_bag(event=None):
  
    item = input_entry.get().strip()
    if not item:
        return
    inventory.append(item)
    text_box.insert(tkinter.END, f"{item} \n")
    input_entry.delete(0, tkinter.END)


input_entry.bind("<Return>", add_to_bag)

add_button = tkinter.Button(main, command=add_to_bag)
add_button.pack(pady=10)

main.mainloop()
