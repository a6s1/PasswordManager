import random
import string
import json
import os
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import pyperclip
from cryptography.fernet import Fernet, InvalidToken

class PasswordManager:
    def __init__(self, file_path='passwords.json', key_path='secret.key'):
        self.file_path = file_path
        self.key_path = key_path
        self.key = self.load_key()
        self.cipher = Fernet(self.key)
        self.passwords = self.load_passwords()
    
    def load_key(self):
        """Load or generate an encryption key."""
        if os.path.exists(self.key_path):
            with open(self.key_path, 'rb') as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_path, 'wb') as key_file:
                key_file.write(key)
            return key

    def encrypt_password(self, password):
        """Encrypt a password."""
        return self.cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        """Decrypt a password."""
        try:
            return self.cipher.decrypt(encrypted_password.encode()).decode()
        except (InvalidToken, ValueError, TypeError):
            return "Decryption failed"

    def load_passwords(self):
        """Load and decrypt passwords from the file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                encrypted_passwords = json.load(file)
                decrypted_passwords = {}
                for account, encrypted_pwd in encrypted_passwords.items():
                    try:
                        decrypted_passwords[account] = self.decrypt_password(encrypted_pwd)
                    except Exception as e:
                        print(f"Failed to decrypt password for {account}: {e}")
                        decrypted_passwords[account] = "Decryption failed"
                return decrypted_passwords
        return {}
    
    def save_passwords(self):
        """Encrypt and save passwords to the file."""
        encrypted_passwords = {account: self.encrypt_password(pwd) for account, pwd in self.passwords.items()}
        with open(self.file_path, 'w') as file:
            json.dump(encrypted_passwords, file)
    
    def generate_password(self, length=16):
        """Generate a random password with a minimum length of 16 characters."""
        if length < 16:
            raise ValueError("Password length should be at least 16 characters")
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        password += random.choices(characters, k=length-4)
        random.shuffle(password)
        return ''.join(password)
    
    def add_password(self, account, password=None, length=16):
        """Add a password for an account."""
        if not password:
            password = self.generate_password(length)
        self.passwords[account] = password
        self.save_passwords()
        return password
    
    def get_password(self, account):
        """Retrieve the password for an account."""
        return self.passwords.get(account, "Account not found")
    
    def update_password(self, account, password=None, length=16):
        """Update the password for an account."""
        if account in self.passwords:
            if not password:
                password = self.generate_password(length)
            self.passwords[account] = password
            self.save_passwords()
            return password
        else:
            return "Account not found"
    
    def delete_password(self, account):
        """Delete the password for an account."""
        if account in self.passwords:
            del self.passwords[account]
            self.save_passwords()
            return "Password deleted"
        else:
            return "Account not found"

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title=None, prompt=None):
        super().__init__(parent)
        self.transient(parent)
        self.title(title)

        self.result = None

        label = tk.Label(self, text=prompt)
        label.pack(padx=20, pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(padx=20, pady=10)
        self.entry.focus_set()

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        ok_button = ttk.Button(button_frame, text="OK", command=self.ok)
        ok_button.pack(side=tk.LEFT, padx=5)
        cancel_button = ttk.Button(button_frame, text="Cancel", command=self.cancel)
        cancel_button.pack(side=tk.LEFT, padx=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        self.geometry("300x150")

    def ok(self, event=None):
        self.result = self.entry.get()
        self.destroy()

    def cancel(self, event=None):
        self.destroy()

class PasswordManagerGUI(tk.Tk):
    def __init__(self, pm):
        super().__init__()
        self.pm = pm
        self.title("Password Manager")
        self.geometry("400x350")
        self.configure(bg="#f0f0f0")

        self.style = ttk.Style(self)
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)
        
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Password Manager", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.add_btn = ttk.Button(self, text="Add Password", command=self.add_password)
        self.add_btn.pack(pady=10, fill=tk.X, padx=20)

        self.get_btn = ttk.Button(self, text="Get Password", command=self.get_password)
        self.get_btn.pack(pady=10, fill=tk.X, padx=20)

        self.update_btn = ttk.Button(self, text="Update Password", command=self.update_password)
        self.update_btn.pack(pady=10, fill=tk.X, padx=20)

        self.delete_btn = ttk.Button(self, text="Delete Password", command=self.delete_password)
        self.delete_btn.pack(pady=10, fill=tk.X, padx=20)

    def add_password(self):
        account = self.show_dialog("Add Password", "Account Name:")
        length = self.show_integer_dialog("Add Password", "Password Length:", 16)
        if account and length:
            password = self.pm.add_password(account, length=length)
            pyperclip.copy(password)
            messagebox.showinfo("Password Added", f"Password for {account}: {password}\n(Copied to clipboard)")

    def get_password(self):
        account = self.show_dialog("Get Password", "Account Name:")
        if account:
            password = self.pm.get_password(account)
            pyperclip.copy(password)
            messagebox.showinfo("Password Retrieved", f"Password for {account}: {password}\n(Copied to clipboard)")

    def update_password(self):
        account = self.show_dialog("Update Password", "Account Name:")
        length = self.show_integer_dialog("Update Password", "Password Length:", 16)
        if account and length:
            password = self.pm.update_password(account, length=length)
            pyperclip.copy(password)
            messagebox.showinfo("Password Updated", f"Updated password for {account}: {password}\n(Copied to clipboard)")

    def delete_password(self):
        account = self.show_dialog("Delete Password", "Account Name:")
        if account:
            result = self.pm.delete_password(account)
            messagebox.showinfo("Password Deleted", result)

    def show_dialog(self, title, prompt):
        dialog = CustomDialog(self, title=title, prompt=prompt)
        self.wait_window(dialog)
        return dialog.result

    def show_integer_dialog(self, title, prompt, initialvalue):
        dialog = CustomDialog(self, title=title, prompt=prompt)
        dialog.entry.insert(0, str(initialvalue))
        self.wait_window(dialog)
        try:
            return int(dialog.result)
        except (ValueError, TypeError):
            return None

def main():
    pm = PasswordManager()
    app = PasswordManagerGUI(pm)
    app.mainloop()

if __name__ == "__main__":
    main()
