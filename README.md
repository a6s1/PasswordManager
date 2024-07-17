```markdown
# Simple Password Manager

A simple password manager written in Python with a graphical user interface (GUI) that allows you to generate, store, update, and delete passwords for different accounts. Passwords are securely saved to a file, ensuring they persist between runs of the application. Retrieved passwords are automatically copied to the clipboard for easy pasting.

## Features

- **Generate Password**: Creates a secure password with a minimum length of 16 characters.
- **Add Password**: Stores a generated or provided password for a specific account.
- **Get Password**: Retrieves the stored password for a given account and copies it to the clipboard.
- **Update Password**: Updates the password for a given account with a new generated or provided password and copies it to the clipboard.
- **Delete Password**: Deletes the stored password for a given account.
- **Graphical User Interface**: Easy-to-use interface for interacting with the password manager.
- **Copy to Clipboard**: Automatically copies retrieved, added, or updated passwords to the clipboard.

## Usage

### Running the Application

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `app.py` file.
3. Open your terminal or command prompt and navigate to the directory containing `app.py`.

### Installing Dependencies

Install the required Python packages using pip:

```sh
pip install pyperclip tk
```

### Creating the Executable

You can create an executable file using PyInstaller:

1. Install PyInstaller:

    ```sh
    pip install pyinstaller
    ```

2. Generate the executable:

    ```sh
    pyinstaller --onefile --noconsole app.py
    ```

3. The executable file will be created in the `dist` directory.

### Using the Application

Double-click the `app.exe` file in the `dist` directory to launch the GUI. You can also run the Python script directly:

```sh
python app.py
```

### GUI Options

- **Add Password**: Adds a new password for an account. You will be prompted to enter the account name and desired password length.
- **Get Password**: Retrieves the password for an account. You will be prompted to enter the account name.
- **Update Password**: Updates the password for an account. You will be prompted to enter the account name and desired password length.
- **Delete Password**: Deletes the password for an account. You will be prompted to enter the account name.

## Example

1. **Add a Password**:

    - Click "Add Password"
    - Enter the account name (e.g., `google`)
    - Enter the desired password length (e.g., `16`)
    - The generated password will be shown in a message box and copied to the clipboard.

2. **Get a Password**:

    - Click "Get Password"
    - Enter the account name (e.g., `google`)
    - The retrieved password will be shown in a message box and copied to the clipboard.

3. **Update a Password**:

    - Click "Update Password"
    - Enter the account name (e.g., `google`)
    - Enter the desired password length (e.g., `20`)
    - The updated password will be shown in a message box and copied to the clipboard.

4. **Delete a Password**:

    - Click "Delete Password"
    - Enter the account name (e.g., `google`)
    - A confirmation message will be shown.


## Contributions

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## Contact

For any questions or suggestions, please open an issue in this repository.
```
