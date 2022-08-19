import tkinter as tk
import brain

window = tk.Tk()
window.title("Password Generator")

# Character Selection
character_value_label = tk.Label(master=window, text="How many characters?")
character_value_label.grid(row=0, column=0)

character_value = tk.Spinbox(window, from_=0, to=20)
character_value.grid(row=0, column=1)

# Uppercase selection
uppercase_value_label = tk.Label(master=window, text="How many uppercase letters?")
uppercase_value_label.grid(row=1, column=0)

uppercase_value = tk.Spinbox(window, from_=0, to=20)
uppercase_value.grid(row=1, column=1)

# Number Selection
number_value_label = tk.Label(master=window, text="How many numbers?")
number_value_label.grid(row=2, column=0)

number_value = tk.Spinbox(window, from_=0, to=20)
number_value.grid(row=2, column=1)

# Symbol Selection
symbol_value_label = tk.Label(master=window, text="How many symbols?")
symbol_value_label.grid(row=3, column=0)

symbol_value = tk.Spinbox(window, from_=0, to=20)
symbol_value.grid(row=3, column=1)


# DO THE THING
# Still trying to figure out the following:
#   * Can I get this function to run from brain.py? Is it necessary?
#   * Open a new window upon execution that says: "Your password is X."
def do_the_thing():
    # Get the values:
    char = int(character_value.get())
    uppr = int(uppercase_value.get())
    num = int(number_value.get())
    sym = int(symbol_value.get())

    # Run the function to get the password:
    answer = brain.password_generator(char, uppr, num, sym)

    # Print the answer while I'm still writing the code to make sure it's working:
    print(answer)

    # Copy the new password to the clipboard:
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append(answer)
    window.update()


operate = tk.Button(master=window, text="Get my password!", command=do_the_thing)
operate.grid(row=4, column=1)


window.mainloop()
