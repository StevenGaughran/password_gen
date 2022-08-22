import tkinter as tk
import password


class Gui:
    def __init__(self):
        self.initiate()

    def initiate(self):
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
        # Things to do:
        #   * Make a button in the Password Window that asks if you want a new password.
        def do_the_thing():
            # Get the values:
            char = int(character_value.get())
            uppr = int(uppercase_value.get())
            num = int(number_value.get())
            sym = int(symbol_value.get())

            # Run the function to get the password:
            answer = password.password_generator(char, uppr, num, sym)
            
            # Copy the new password to the clipboard:
            window.withdraw()
            window.clipboard_clear()
            window.clipboard_append(answer)
            window.update()

            # Opens a new window with the password:
            new_window = tk.Toplevel(window)
            new_window.title("Your password is ready!")
            new_window.geometry("200x150")

            new_password = tk.Label(new_window, text=f"Your password is: \n{answer}")
            new_password.grid(row=0, column=0)

            explanation = tk.Label(new_window, text="It has been copied to your clipboard.")
            explanation.grid(row=2, column=0)

            go_again = tk.Label(master=new_window, text="Another password?")
            go_again.grid(row=3, column=0)

            # Buttons to restart or end the program.
            def again():
                new_window.destroy()
                self.initiate()

            def not_again():
                exit()

            restart_yes = tk.Button(master=new_window, text="Yes", command=again)
            restart_yes.grid(row=4, column=0)

            restart_no = tk.Button(master=new_window, text="No", command=not_again)
            restart_no.grid(row=5, column=0)

        operate = tk.Button(master=window, text="Get my password!", command=do_the_thing)
        operate.grid(row=4, column=1)

        window.mainloop()
