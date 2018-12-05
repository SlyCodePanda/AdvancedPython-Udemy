from tkinter import *
import tkinter
import socket
from threading import Thread


# Handles received messages.
def receive():
    while True:
        try:
            msg = s.recv(1024).decode("utf8")
            # Insert msg at the end of the msg_list.
            msg_list.insert(tkinter.END, msg)
        except:
            print("Error receiving message...")
            break

def send(event=None):
    # Store message typed in msg variable.
    msg = my_msg.get()
    # Clear message entry space.
    my_msg.set("")
    # Send message to the server.
    s.send(bytes(msg, "utf8"))

    if msg == "#quit":
        s.close()
        window.quit()

def on_closing():
    my_msg.set("#quit")
    send()


# Colour/Font Scheme.
bg_colour = "#17414f"
bg02_colour = "#333333"
font01_colour = "#66ff66"
font02_colour = "#66ffff"
font03_colour = "#ff6666"
msg_font = "Andale"
msg_font02 = "Courier"
msg_font03 = ("Andale", 10, "bold")
font03 = "Arial"

window = Tk()
window.title("Servo Face Chat Room")
window.configure(bg=bg02_colour)
messages_frame = Frame(window, height=100, width=100, bg=bg_colour)
my_msg = StringVar()
my_msg.set("")
scroll_bar = Scrollbar(messages_frame)
msg_list = Listbox(messages_frame, height=15, width=100, bg=bg_colour, fg=font01_colour, font=msg_font,
                   yscrollcommand=scroll_bar.set)

# Pack widget into window.
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

button_label = Label(window, text="Enter Your Message", fg=font01_colour, font=msg_font, bg=bg02_colour)
button_label.pack()

entry_field = Entry(window, textvariable=my_msg, fg=font03_colour, bg=bg_colour, font=msg_font03, width=50)
# Binds the enter key to allow you to press 'Enter' to send message.
entry_field.bind('<Return>', send)
entry_field.pack()

send_button = Button(window, text="Send", bg=bg_colour, font=font03, fg="white", relief=FLAT, command=send)
send_button.pack()

quit_button = Button(window, text="Quit", bg=font03_colour, font=font03, fg="white", relief=FLAT, command=on_closing)
quit_button.pack()

window.protocol("WM_DELETE_WINDOW", on_closing)

host = '10.1.1.17'
port = 8080

s = socket.socket()
s.connect((host, port))

recieve_thread = Thread(target=receive)
recieve_thread.start()

# Waits for events and updates GUI.
mainloop()
