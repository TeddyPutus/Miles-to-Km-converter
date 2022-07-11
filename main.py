import tkinter

window = tkinter.Tk()
window.title("Miles To Kilometers Converter")
window.configure(padx=30, pady=30)

answer_label_text = tkinter.IntVar()
answer_label_text.set(0)


def button_click():
    global answer_label_text
    global miles_input
    answer = int(miles_input.get()) * 1.6
    round(answer, 2)
    answer_label_text.set(answer)

miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0,column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tkinter.Label(text="Is equal to")
is_equal_label.grid(row=1, column=0)

answer_label = tkinter.Label(textvariable=answer_label_text)
answer_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

button = tkinter.Button(text="Convert", command=button_click)
button.grid(row=2, column=1)

#must be at the end
window.mainloop()

