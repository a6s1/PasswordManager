# Simple Password Manager

A simple password manager written in Python that allows you to generate, store, update, and delete passwords for different accounts. Passwords are securely saved to a file, ensuring they persist between runs of the script.

## Features

- **Generate Password**: Creates a secure password with a minimum length of 16 characters.
- **Add Password**: Stores a generated or provided password for a specific account.
- **Get Password**: Retrieves the stored password for a given account.
- **Update Password**: Updates the password for a given account with a new generated or provided password.
- **Delete Password**: Deletes the stored password for a given account.
- **Command-Line Interface**: Interact with the password manager through command-line arguments.

## Usage

### Adding a Password

To add a password for an account, use the `-a` or `--add` argument followed by the account name and the desired password length.

```sh
python app.py -a <account> <length>
```

Example:

```sh
python app.py -a google 16
```

### Getting a Password

To retrieve the password for an account, use the `-g` or `--get` argument followed by the account name.

```sh
python app.py -g <account>
```

Example:

```sh
python app.py -g google
```

### Updating a Password

To update the password for an account, use the `-u` or `--update` argument followed by the account name and the desired password length.

```sh
python app.py -u <account> <length>
```

Example:

```sh
python app.py -u google 20
```

### Deleting a Password

To delete the password for an account, use the `-d` or `--delete` argument followed by the account name.

```sh
python app.py -d <account>
```

Example:

```sh
python app.py -d google
```

### Displaying Help

To display help and see all available options, use the `-h` or `--help` argument.

```sh
python app.py -h
```

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `app.py` file.
3. Open your terminal or command prompt and navigate to the directory containing `app.py`.

## Example

```sh
# Add a password for Google
python app.py -a google 16
# Output: Password for google: ]VH?D1g_<2<L["fY

# Retrieve the password for Google
python app.py -g google
# Output: Password for google: ]VH?D1g_<2<L["fY

# Update the password for Google
python app.py -u google 20
# Output: Updated password for google: wH2+SDd7!zU@J&Lk^YtZ

# Delete the password for Google
python app.py -d google
# Output: Password deleted

# Try to retrieve the deleted password
python app.py -g google
# Output: Account not found
```


## Contributions

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## Contact

For any questions or suggestions, please open an issue in this repository.

