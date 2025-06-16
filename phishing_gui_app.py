import tkinter as tk
import itertools
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from url_checker import analyze_url_wrapper

# Setup
root = tk.Tk()
root.title("Real-Time Phishing URL Detector")
root.geometry("1100x700")
root.minsize(800, 600)
root.configure(bg="#1e1e1e")

# Global theme flag
is_dark = True

# Load and resize background
bg_img = Image.open("assets/bg.png")
resample_mode = Image.Resampling.LANCZOS
bg_img = bg_img.resize((1100, 700), resample=resample_mode)
bg_img_tk = ImageTk.PhotoImage(bg_img)

# Create Canvas and background image
canvas = tk.Canvas(root, width=1100, height=700, highlightthickness=0)
canvas.pack(fill="both", expand=True)
bg_img_id = canvas.create_image(0, 0, anchor="nw", image=bg_img_tk)

# Main Frame in center
main_frame = tk.Frame(canvas, bg="#121212", bd=0)
frame_window = canvas.create_window(0, 0, anchor="center", window=main_frame)
loading_text = None
loading = False
spinner_task = None

# Header
header = tk.Label(main_frame, text="🛡️Real-Time Phishing URL Detector", font=("Segoe UI", 24, "bold"), fg="#00FFCC", bg="#121212")
header.pack(pady=(20, 10))

# Entry for URL
url_var = tk.StringVar()
url_entry = tk.Entry(main_frame, textvariable=url_var, font=("Segoe UI", 14), width=50, relief="solid", bd=2, justify="center",fg="#00FFCC", bg="#121212")
url_entry.pack(pady=(10, 10))
url_entry.configure(insertbackground="#00FFCC")  # Cursor color
def select_all(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

url_entry.bind("<Control-a>", select_all)
url_entry.bind("<Command-a>", select_all)  # For macOS compatibility
url_entry.bind("<Return>", lambda e: check_url())  # Enter triggers check

# Result label
result_label = tk.Label(main_frame, text="", font=("Segoe UI", 14), fg="#FFFFFF", bg="#121212")
result_label.pack(pady=(10, 20))

# Analyze URL
def show_loading_spinner():
    global loading_text, spinner_task
    dots = itertools.cycle(["", ".", "..", "..."])
    
    if not loading_text:
        loading_text = tk.Label(
            main_frame,
            text="Checking URL",
            font=("Segoe UI", 16, "bold"),
            fg="#00FFCC" if is_dark else "#0000CC",
            bg=main_frame["bg"]
        )
        loading_text.pack()

    def animate():
        if loading:
            dot_text = next(dots)
            loading_text.config(
                text=f"🔍 Checking URL{dot_text}",
                fg="#00FFCC" if is_dark else "#0000CC",
                bg=main_frame["bg"]
            )
            spinner_task = root.after(300, animate)
        else:
            loading_text.config(text="")

    animate()

def check_url():
    global loading, spinner_task
    url = url_var.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return

    loading = True
    show_loading_spinner()
    root.update_idletasks()

    try:
        result = analyze_url_wrapper(url)
        if result["phishing"]:
            result_label.config(text=f"⚠️ Phishing Detected: {result['reason']}", fg="#FF4C4C")
        else:
            result_label.config(text=f"✅ Legitimate: {result['reason']}", fg="#00FF00")
    except Exception as e:
        result_label.config(text="Error during analysis", fg="red")

    loading = False
    if spinner_task:
        root.after_cancel(spinner_task)

# Button styles
button_style = {
    "font": ("Segoe UI", 12, "bold"),
    "bg": "#00FFCC",
    "fg": "#000000",
    "activebackground": "#00DDBB",
    "activeforeground": "#000000",
    "bd": 0,
    "cursor": "hand2",
    "relief": "flat",
    "width": 18,
    "highlightthickness": 0
}

# Check button
check_btn = tk.Button(main_frame, text="🔍 Check URL", command=check_url, **button_style)
check_btn.pack(pady=(0, 15))

# Theme toggle
def toggle_theme():
    global is_dark
    is_dark = not is_dark
    if is_dark:
        root.configure(bg="#1e1e1e")
        main_frame.configure(bg="#121212")
        header.configure(bg="#121212", fg="#00FFCC")
        url_entry.configure(bg="#1e1e1e", fg="#00FFCC")
        result_label.configure(bg="#121212", fg="#FFFFFF")
        theme_btn.configure(text="☀️ Light Mode", bg="#00FFCC", fg="#000000")
        if loading_text:
           loading_text.config(fg="#00FFCC", bg="#121212")

    else:
        root.configure(bg="#FAFAFA")
        main_frame.configure(bg="#FFFFFF")
        header.configure(bg="#FFFFFF", fg="#000000")
        url_entry.configure(bg="#FFFFFF", fg="#000000")
        result_label.configure(bg="#FFFFFF", fg="#000000")
        theme_btn.configure(text="🌑 Dark Mode", bg="#222222", fg="#FFFFFF")
        if loading_text:
           loading_text.config(fg="#0000CC", bg="#FFFFFF")

# Toggle button
theme_btn = tk.Button(main_frame, text="☀️ Light Mode", command=toggle_theme, **button_style)
theme_btn.pack(pady=(0, 20))

# Responsive resizing
def resize(event):
    new_w, new_h = event.width, event.height
    resized = bg_img.resize((new_w, new_h), resample=resample_mode)
    bg_img_tk_resized = ImageTk.PhotoImage(resized)
    canvas.itemconfig(bg_img_id, image=bg_img_tk_resized)
    canvas.image = bg_img_tk_resized  # Prevent garbage collection
    canvas.coords(frame_window, new_w // 2, new_h // 2)

canvas.bind("<Configure>", resize)

root.mainloop()

