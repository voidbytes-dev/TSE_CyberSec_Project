import tkinter as tk
from tkinter import ttk, messagebox
import socket

# Boolean variable to control defense state
isDefending = True


def testConnection():
    ipPort = ipPortEntry.get().strip()
    duration = durationEntry.get().strip()

    if not ipPort or not duration.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid IP/Port and duration.")
        return

    try:
        host, port = ipPort.split(':')
        port = int(port)

        # Simulating a network connection test
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)  # Timeout for the connection attempt
            result = s.connect_ex((host, port))

        if result == 0:
            messagebox.showinfo("Success", f"Connection to {host}:{port} successful!")
        else:
            messagebox.showwarning("Failed", f"Unable to connect to {host}:{port}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input format or network issue: {e}")


def defend():
    global isDefending
    if isDefending:
        messagebox.showinfo("Defend", "Defending!")


# Create main window
win = tk.Tk()
win.title("Network Connection Tester")
win.geometry("400x300")
win.configure(bg="#36393F")

style = ttk.Style()
style.configure("TLabel", background="#36393F", foreground="white", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

# Frame for UI elements
frame = ttk.Frame(win, padding="20")
frame.pack(expand=True)


# Defend Button
defendButton = ttk.Button(frame, text="Defend", command=defend)
defendButton.grid(row=3, column=0, columnspan=2, pady=(20, 0))

# Run the application
win.mainloop()