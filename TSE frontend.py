import tkinter as tk
from tkinter import ttk, messagebox
import socket

def test_connection():
    ip_port = ip_port_entry.get().strip()
    duration = duration_entry.get().strip()
    
    if not ip_port or not duration.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid IP/Port and duration.")
        return
    
    try:
        host, port = ip_port.split(':')
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

# Create main window
win = tk.Tk()
win.title("Network Connection Tester")
win.geometry("400x250")
win.configure(bg="#36393F")

style = ttk.Style()
style.configure("TLabel", background="#36393F", foreground="white", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

# Frame for UI elements
frame = ttk.Frame(win, padding="20")
frame.pack(expand=True)

# IP/Port Input
ip_port_label = ttk.Label(frame, text="IP:Port:")
ip_port_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
ip_port_entry = ttk.Entry(frame, width=30)
ip_port_entry.grid(row=0, column=1, pady=(0, 5))

# Duration Input
duration_label = ttk.Label(frame, text="Test Duration (s):")
duration_label.grid(row=1, column=0, sticky="w", pady=(0, 5))
duration_entry = ttk.Entry(frame, width=30)
duration_entry.grid(row=1, column=1, pady=(0, 5))

# Start Test Button
test_button = ttk.Button(frame, text="Test Connection", command=test_connection)
test_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

# Run the application
win.mainloop()
