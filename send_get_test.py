from firebase import firebase
import tkinter as tk
import getpass
from datetime import date
from datetime import datetime

# UI section
root = tk.Tk()
root.geometry("400x300")
root.title("Python Window with Textbox")

textbox = tk.Text(root, height=5, width=30)
textbox.pack()

entry = tk.Entry(root)
entry.pack()



firebase = firebase.FirebaseApplication("https://first-4b2ba-default-rtdb.firebaseio.com/")
username = getpass.getuser()
global global_date
global_date = date.today()  # New chat date



def update_textbox():
    result = firebase.get('/first-4b2ba/Message', '')
    if result:
        #textbox.delete("1.0", "end")  # Clear the existing content
        for outer_key, inner_dict in result.items():
            name = inner_dict.get('name', None)
            if name is not None:
                textbox.insert("end", name + "\n")  # Append the new name with a newline
                textbox.see("end")
    root.after(1000, update_textbox)  # Check for updates every second

def post(new_chat_flag = True):
    #if new_chat_flag:
    textbox.insert("end", str(global_date) + "\n" + "\n") # tu je problem
    textbox.see("end")
    new_chat_flag = False
    c_t = datetime.now()
    current_time = c_t.strftime('%H:%M:%S')     # Add time_stamp of message
    text_box = entry.get()  # Send textbox
    DB_message = text_box + "-->" + username + " | " + current_time
    list = {
        'name':DB_message
    }
    firebase.post('/first-4b2ba/Message', list)

button = tk.Button(root, text="Send", command=post)
button.pack()

update_textbox()  # Start the update loop

root.mainloop()
