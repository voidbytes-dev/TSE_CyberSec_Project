import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Attack Interface")
win.geometry("400x300")
win.configure(bg="#36393F")

isclicked = False

# Custom rounded button class
class RoundedButton(tk.Canvas):
    def __init__(self, master=None, text="", radius=25, bg="#7289DA", fg="white", **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#36393F", highlightthickness=0)  # Set background to match the theme
        self.radius = radius
        self.bg = bg
        self.fg = fg
        self.text = text
        self.bind("<Button-1>", self.when_clicked)
        self.draw_button()

    def draw_button(self):
        self.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()
        self.create_rounded_rectangle(0, 0, width, height, radius=self.radius, fill=self.bg)
        self.create_text(width // 2, height // 2, text=self.text, fill=self.fg, font=("Arial", 12, "bold"))

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.create_polygon(points, **kwargs, smooth=True)

    def clickpopup(self):
        top = tk.Toplevel(win)
        top.geometry("750x750")
        top.title("Child Window")
        tk.Label(top, text="Attack successful", font=('Mistral 18 bold')).place(x=150, y=80)

    def when_clicked(self, event):
        global isclicked
        if isclicked is False:
            # Get the values from the input fields
            ip_port = ip_port_entry.get()
            amount_duration = amount_duration_entry.get()
            if ip_port == '' or amount_duration == '':
                print("Invalid input")
            else:
                # Print the values
                print(f"IP/Port: {ip_port}")
                print(f"Amount/Duration: {amount_duration}")
                isclicked = True
                self.clickpopup()

        else:
            print("DDoS attack successful")


# Frame for the interface
frame = ttk.Frame(win, padding="20")
frame.grid(row=0, column=0, sticky="nsew")

style = ttk.Style()
style.configure("Custom.TFrame", background="#36393F")
style.configure("Custom.TLabel", background="#36393F", foreground="white")

# IP/Port Input
ip_port_label = ttk.Label(frame, text="IP/Port:", style="Custom.TLabel")
ip_port_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
ip_port_entry = ttk.Entry(frame, width=30)
ip_port_entry.grid(row=0, column=1, pady=(0, 5))

# Amount Input
amount_duration_label = ttk.Label(frame, text="Amount/Duration:", style="Custom.TLabel")
amount_duration_label.grid(row=1, column=0, sticky="w", pady=(0, 5))
amount_duration_entry = ttk.Entry(frame, width=30)
amount_duration_entry.grid(row=1, column=1, pady=(0, 5))

# Start Attack Button
start_attack_button = RoundedButton(frame, text="Start Attack", radius=20, bg="#7289DA", fg="white", width=150, height=40)
start_attack_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

# Configure grid weights
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Run the application
win.mainloop()