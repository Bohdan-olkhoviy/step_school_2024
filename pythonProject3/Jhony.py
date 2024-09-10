import tkinter as tk
def onclick():

    a = int(rect_width_entry.get())
    b = int(rect_height_entry.get())
    label3.config(text=f'Площа прямокутника:\n{a * b}')
window = tk.Tk()
window.title('Tkinter App')
window.geometry('300x300')
FONT = ("Comic Sans MS", 18)
label1 = tk.Label(text='Довжина прямокутника', font=FONT)
label1.pack()
rect_width_entry = tk.Entry(font=FONT)
rect_width_entry.pack()
label2 = tk.Label(text='Висота прямокутника', font=FONT)
label2.pack()
rect_height_entry = tk.Entry(font=FONT)
rect_height_entry.pack()
button1 = tk.Button(text="Розрахувати площу", font=FONT, command=onclick, bg='lightblue')
button1.pack()
label3 = tk.Label(text='', font=FONT)
label3.pack()
window.mainloop()

