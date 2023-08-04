
import tkinter as tk
from time import strftime


def time_display():
    
    # Get current time
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)


    # Update the time every 1000ms (1 second)
    label.after(1000, time_display)



# Create the main window
root = tk.Tk()
root.title("Digital Clock")



# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(pady=20)


# Start displaying the time
time_display()


# Run the main event loop
root.mainloop()
