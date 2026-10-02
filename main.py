import tkinter as tk
from tkinter import PhotoImage

APP_NAME = "ChatNest"
DARK_BLUE = "#182B49"
GOLD = "#F4B942"
BACKGROUND = "#F3F5F7"
WHITE = "#FFFFFF"
TEXT = "#222222"

contacts = ["Alice", "Bob", "Charlie", "David", "Eve"]

def welcome_screen():
    root = tk.Tk()
    root.title(APP_NAME)
    root.geometry("420x600")
    root.configure(bg=BACKGROUND)

    logo = PhotoImage(file="chatnest_logo.png")
    logo_label = tk.Label(root, image=logo, bg=BACKGROUND)
    logo_label.pack(pady=50)

    button = tk.Button(
        root,
        text="Open Contacts",
        font=("Arial", 14, "bold"),
        bg=DARK_BLUE,
        fg=WHITE,
        activebackground=GOLD,
        activeforeground=TEXT,
        relief="flat",
        padx=30,
        pady=12,
        command=lambda: open_contacts(root)
    )
    button.pack()

    root.mainloop()

def open_contacts(previous_window):
    previous_window.destroy()

    window = tk.Tk()
    window.title("ChatNest - Contacts")
    window.geometry("420x600")
    window.configure(bg=BACKGROUND)

    header = tk.Frame(window, bg=DARK_BLUE, height=70)
    header.pack(fill="x")

    title = tk.Label(
        header,
        text="Chats",
        font=("Arial", 22, "bold"),
        bg=DARK_BLUE,
        fg=WHITE
    )
    title.pack(anchor="w", padx=25, pady=18)

    for contact in contacts:
        frame = tk.Frame(window, bg=WHITE, height=75)
        frame.pack(fill="x", padx=12, pady=5)

        button = tk.Button(
            frame,
            text=contact,
            font=("Arial", 15, "bold"),
            bg=WHITE,
            fg=TEXT,
            activebackground=GOLD,
            relief="flat",
            anchor="w",
            command=lambda name=contact: open_chat(name)
        )
        button.pack(fill="both", expand=True, padx=15, pady=12)

    window.mainloop()

def open_chat(contact_name):
    window = tk.Toplevel()
    window.title("ChatNest - " + contact_name)
    window.geometry("500x650")
    window.configure(bg=BACKGROUND)

    header = tk.Frame(window, bg=DARK_BLUE, height=70)
    header.pack(fill="x")

    title = tk.Label(
        header,
        text=contact_name,
        font=("Arial", 18, "bold"),
        bg=DARK_BLUE,
        fg=WHITE
    )
    title.pack(anchor="w", padx=20, pady=20)

    chat_area = tk.Text(
        window,
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 12),
        wrap="word",
        state="disabled",
        relief="flat"
    )
    chat_area.pack(fill="both", expand=True, padx=12, pady=12)

    input_frame = tk.Frame(window, bg=WHITE)
    input_frame.pack(fill="x", padx=10, pady=10)

    message_entry = tk.Entry(
        input_frame,
        font=("Arial", 12),
        relief="flat"
    )
    message_entry.pack(side="left", fill="x", expand=True, padx=10, pady=12)

    def send_message():
        message = message_entry.get()

        if message:
            chat_area.config(state="normal")
            chat_area.insert("end", "You: " + message + "\n")
            chat_area.config(state="disabled")
            chat_area.see("end")
            message_entry.delete(0, "end")

    send_button = tk.Button(
        input_frame,
        text="Send",
        font=("Arial", 11, "bold"),
        bg=GOLD,
        fg=TEXT,
        activebackground=DARK_BLUE,
        activeforeground=WHITE,
        relief="flat",
        padx=18,
        pady=8,
        command=send_message
    )
    send_button.pack(side="right", padx=5)

if __name__ == "__main__":
    welcome_screen()
