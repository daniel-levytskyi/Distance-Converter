import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(str(km_output) + " Km")

window = ttk.Window()
window.title('Measurement Converter')
window.geometry('350x200')

#application title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font = "Calibri 24 bold")
title_label.pack()

#user input field
entry_int = ttk.IntVar()

input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame, textvariable=entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side=LEFT, padx=10)
button.pack(side=LEFT)
input_frame.pack(pady=10)

#output operation
output_string = ttk.StringVar()

output_label = ttk.Label(master = window, text = "Output: ", font = "Calibri 24 bold", textvariable = output_string)
output_label.pack()

#terminate the program
exit_button = ttk.Button(master = window, text = "Exit Button", command = window.destroy)
exit_button.pack(pady=10)

window.mainloop()