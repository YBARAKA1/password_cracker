import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import time

def hash_password(password, algorithm="sha256"):
    """Hashes a password with the given algorithm."""
    if algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hash algorithm")

def crack_password():
    hash_to_crack = hash_entry.get()
    wordlist_path = filedialog.askopenfilename(title="Select Wordlist", filetypes=(("Text Files", "*.txt"),))

    if not hash_to_crack or not wordlist_path:
        messagebox.showerror("Error", "Please enter a hash and select a wordlist.")
        return

    start_time = time.time()

    try:
        with open(wordlist_path, "r") as file:
            for word in file:
                word = word.strip()
                hashed_word = hash_password(word)

                if hashed_word == hash_to_crack:
                    elapsed_time = time.time() - start_time
                    messagebox.showinfo("Success", f"Password cracked: {word}\nTime taken: {elapsed_time:.2f} seconds")
                    return

        messagebox.showwarning("Failure", "Password not found in the wordlist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Real-Life Password Cracker")

tk.Label(root, text="Enter Hash to Crack:").pack(pady=5)
hash_entry = tk.Entry(root, width=60)
hash_entry.pack(pady=5)

crack_button = tk.Button(root, text="Crack Password", command=crack_password)
crack_button.pack(pady=10)

root.geometry("400x200")
root.mainloop()
