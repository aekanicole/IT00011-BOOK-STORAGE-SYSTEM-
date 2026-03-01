import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# -----------------------------
# TABLES
# -----------------------------

# ----- USER INFORMATION -----
cursor.execute("""CREATE TABLE IF NOT EXISTS members (
               member_id INTEGER PRIMARY KEY AUTOINCREMENT,
               email TEXT UNIQUE NOT NULL,
               password TEXT NOT NULL,
               full_name TEXT,
               age INTEGER,
               student_number TEXT)""")

# ----- BOOK INFORMATION -----
cursor.execute("""CREATE TABLE IF NOT EXISTS books (
               book_id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               genre TEXT NOT NULL,
               author TEXT,
               date_published TEXT,
               status TEXT DEFAULT 'AVAILABLE'
               )""")

# ----- TRANSACTION INFORMATION -----
cursor.execute("""CREATE TABLE IF NOT EXISTS transactions(
               trans_id INTEGER PRIMARY KEY AUTOINCREMENT,
               member_id INTEGER,
               book_id INTEGER,
               borrow_date TEXT,
               duration INTEGER,
               FOREIGN KEY(member_id) REFERENCES members(member_id),
               FOREIGN KEY(book_id) REFERENCES books(book_id)
               )""")
# -----------------------------
# COLOR THEME
# -----------------------------
PRIMARY = "#2E7D32"
DARK_GREEN = "#1B5E20"
LIGHT_BG = "#F4F6F7"
WHITE = "#FFFFFF"
TEXT_DARK = "#212121"

# -----------------------------
# MAIN APP CONTROLLER
# -----------------------------
class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Sorting System")
        self.geometry("1100x650")
        self.configure(bg=LIGHT_BG)
        self.resizable(False, False)

        self.current_frame = None
        self.show_home()

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    def show_home(self):
        self.switch_frame(HomePage)

    def show_login(self):
        self.switch_frame(LoginPage)

    def show_signup(self):
        self.switch_frame(SignupPage)

# -----------------------------
# HOME PAGE
# -----------------------------
class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=LIGHT_BG)

        # TOP TITLE BAR
        top_bar = tk.Frame(self, bg=DARK_GREEN, height=50)
        top_bar.pack(fill="x")
        tk.Label(top_bar, text="HOME PAGE", bg=DARK_GREEN,
                 fg="white", font=("Arial", 16, "bold")).pack(pady=10)

        # NAVIGATION BAR
        nav = tk.Frame(self, bg=PRIMARY, height=60)
        nav.pack(fill="x")

        tk.Label(nav, text="LOGO", bg="white",
                 width=8).pack(side="left", padx=20, pady=15)

        search = tk.Entry(nav, width=30)
        search.pack(side="left", padx=10)

        tk.Button(nav, text="HOME", bg="white",
                  command=master.show_home).pack(side="left", padx=10)

        tk.Button(nav, text="CATEGORY", bg="white").pack(side="left", padx=10)
        tk.Button(nav, text="HELP", bg="white").pack(side="left", padx=10)

        tk.Button(nav, text="USER", bg="white").pack(side="right", padx=10)
        tk.Button(nav, text="Login", bg="white",
                  command=master.show_login).pack(side="right", padx=10)

        # HERO SECTION
        hero = tk.Frame(self, bg="gray", height=300)
        hero.pack(fill="x", pady=20, padx=40)

        tk.Label(hero,
                 text="FAR EASTERN TECHNOLOGY LIBRARY",
                 bg="gray",
                 fg="white",
                 font=("Arial", 24, "bold")).pack(expand=True)

        # CARD SECTION
        card_section = tk.Frame(self, bg=LIGHT_BG)
        card_section.pack(pady=20)

        for title in ["RESEARCH", "ALL RESOURCES", "ABOUT"]:
            card = tk.Frame(card_section, bg=WHITE, width=250, height=150,
                            highlightbackground="#cccccc", highlightthickness=1)
            card.pack(side="left", padx=20)
            card.pack_propagate(False)

            tk.Label(card, text=title,
                     font=("Arial", 14, "bold"),
                     bg=WHITE).pack(expand=True)

        # FOOTER
        footer = tk.Frame(self, bg=PRIMARY, height=40)
        footer.pack(fill="x", side="bottom")
        tk.Label(footer, text="FOOTER",
                 bg=PRIMARY, fg="white").pack(pady=10)

# -----------------------------
# LOGIN PAGE
# -----------------------------
class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=LIGHT_BG)

        tk.Label(self, text="Login to Library System",
                 bg=LIGHT_BG, fg=TEXT_DARK,
                 font=("Arial", 20, "bold")).pack(pady=40)

        card = tk.Frame(self, bg=WHITE, width=350, height=300,
                        highlightbackground="#cccccc",
                        highlightthickness=1)
        card.pack()
        card.pack_propagate(False)

        tk.Label(card, text="Email", bg=WHITE).pack(pady=10)
        email_entry = tk.Entry(card, width=30)
        email_entry.pack()

        tk.Label(card, text="Password", bg=WHITE).pack(pady=10)
        password_entry = tk.Entry(card, width=30, show="*")
        password_entry.pack()

        def login():
            email = email_entry.get()
            password = password_entry.get()
            if not email or not password:
                messagebox.showwarning("Warning", "Please fill all fields")
            else:
                messagebox.showinfo("Success", "Login Successful!")
                master.show_home()

        tk.Button(card, text="Login",
                  bg=PRIMARY, fg="white",
                  width=20,
                  command=login).pack(pady=20)

        tk.Button(card, text="Don't have an account? Signup",
                  bg=WHITE, fg=PRIMARY,
                  bd=0,
                  command=master.show_signup).pack()

        tk.Button(self, text="Back to Home",
                  command=master.show_home).pack(pady=20)

# -----------------------------
# SIGNUP PAGE
# -----------------------------
class SignupPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=LIGHT_BG)

        tk.Label(self, text="Create Library Account",
                 bg=LIGHT_BG, fg=TEXT_DARK,
                 font=("Arial", 20, "bold")).pack(pady=30)

        main = tk.Frame(self, bg=LIGHT_BG)
        main.pack()

        # LEFT BRANDING SECTION
        left = tk.Frame(main, bg=PRIMARY, width=400, height=400)
        left.pack(side="left", padx=20)
        left.pack_propagate(False)

        tk.Label(left,
                 text="Join the Library Community",
                 bg=PRIMARY, fg="white",
                 font=("Arial", 16, "bold"),
                 wraplength=300).pack(expand=True)

        # RIGHT SIGNUP CARD
        right = tk.Frame(main, bg=WHITE, width=400, height=400,
                         highlightbackground="#cccccc",
                         highlightthickness=1)
        right.pack(side="left")
        right.pack_propagate(False)

        fields = ["Email", "Password", "Confirm Password",
                  "Full Name", "Age", "Student Number"]

        entries = {}

        for field in fields:
            tk.Label(right, text=field, bg=WHITE).pack(pady=5)
            show_char = "*" if "Password" in field else ""
            entry = tk.Entry(right, width=30, show=show_char)
            entry.pack()
            entries[field] = entry

        def signup():
            values = [entries[f].get() for f in fields]
            if "" in values:
                messagebox.showwarning("Warning", "All fields are required")
            elif entries["Password"].get() != entries["Confirm Password"].get():
                messagebox.showerror("Error", "Passwords do not match")
            else:
                messagebox.showinfo("Success", "Account Created!")
                master.show_login()

        tk.Button(right, text="Create Account",
                  bg=PRIMARY, fg="white",
                  width=25,
                  command=signup).pack(pady=15)

        tk.Button(right, text="Already have account? Login",
                  bg=WHITE, fg=PRIMARY,
                  bd=0,
                  command=master.show_login).pack()

        tk.Button(self, text="Back to Home",
                  command=master.show_home).pack(pady=20)

# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
