import random
import string
import argparse
import json
import os

class PasswordManager:
    def __init__(self, file_path='passwords.json'):
        self.file_path = file_path
        self.passwords = self.load_passwords()
    
    def load_passwords(self):
        """Load passwords from the file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return {}
    
    def save_passwords(self):
        """Save passwords to the file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.passwords, file)
    
    def generate_password(self, length=16):
        """Generate a random password with a minimum length of 16 characters."""
        if length < 16:
            raise ValueError("Password length should be at least 16 characters")
        
        # Define the characters to use in the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Ensure the password has at least one character from each category
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        
        # Fill the rest of the password length with random characters
        password += random.choices(characters, k=length-4)
        
        # Shuffle the password to ensure randomness
        random.shuffle(password)
        
        # Convert the list to a string and return
        return ''.join(password)
    
    def add_password(self, account, password=None, length=16):
        """Add a password for an account. Generate one if not provided."""
        if not password:
            password = self.generate_password(length)
        self.passwords[account] = password
        self.save_passwords()
        return password
    
    def get_password(self, account):
        """Retrieve the password for an account."""
        return self.passwords.get(account, "Account not found")
    
    def update_password(self, account, password=None, length=16):
        """Update the password for an account. Generate one if not provided."""
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

def main():
    parser = argparse.ArgumentParser(description="Simple Password Manager")
    
    parser.add_argument("-a", "--add", help="Add a new password for an account. Usage: -a <account> <length>", nargs=2, metavar=('account', 'length'), type=str)
    parser.add_argument("-g", "--get", help="Get the password for an account. Usage: -g <account>", metavar='account', type=str)
    parser.add_argument("-u", "--update", help="Update the password for an account. Usage: -u <account> <length>", nargs=2, metavar=('account', 'length'), type=str)
    parser.add_argument("-d", "--delete", help="Delete the password for an account. Usage: -d <account>", metavar='account', type=str)
    
    args = parser.parse_args()
    
    pm = PasswordManager()
    
    if args.add:
        account, length = args.add
        try:
            length = int(length)
            password = pm.add_password(account, length=length)
            print(f"Password for {account}: {password}")
        except ValueError:
            print("Length must be an integer")
    
    if args.get:
        account = args.get
        password = pm.get_password(account)
        print(f"Password for {account}: {password}")
    
    if args.update:
        account, length = args.update
        try:
            length = int(length)
            password = pm.update_password(account, length=length)
            print(f"Updated password for {account}: {password}")
        except ValueError:
            print("Length must be an integer")
    
    if args.delete:
        account = args.delete
        result = pm.delete_password(account)
        print(result)

if __name__ == "__main__":
    main()
