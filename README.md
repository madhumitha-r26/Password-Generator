# Password Generator
A simple, GUI-based password generator built with Python's Tkinter library, this project allows users to input their desired length (between 8 and 15 characters) to generate a highly secure password for protection, combining numbers, lowercase letters, uppercase letters, and special symbols, ensuring at least one of each type and shuffling the final result for maximum security.

## Features
- **Password Length**: Accepts input for password length between 8 and 15 characters.
- **Character Variety**: Ensures inclusion of:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Symbols (*@/|\-.?!+$%^#_&~)
- **Randomization**: Uses Python's `random` module to select and shuffle characters.
- **GUI Interface**: User-friendly Tkinter-based interface with buttons for generating, clearing, and copying passwords.
- **Copy to Clipboard**: Allows copying the generated password to the system clipboard.
- **Error Handling**: Validates input and provides feedback for invalid lengths or non-integer inputs.

## Requirements
- Python 3.x (Tkinter is included in standard Python installations).
- No external libraries are required beyond the standard library.

## Installation
1. Ensure Python is installed on your system.
2. Download or copy the provided code into a file named `password_generator.py`.

## Usage
1. Run the script:
   ```
   python password_generator.py
   ```
2. Enter a password length between 8 and 15 in the input field.
3. Click the "Generate" button to create a password.
4. The generated password will be displayed.
5. Click "Copy Password" to copy it to your clipboard.
6. Use the "Clear" button to reset the input and hide the copy button.

## Example
- Input: 10
- Output: A randomly generated password like `A1b!C2d@E3f`

## Code Structure
- **Character Sets**: Defined at the top for lowercase, uppercase, numbers, and symbols.
- **generate_password()**: Core function to create the password based on length.
- **clear_password()**: Clears the input and result.
- **copy_password()**: Copies the generated password to clipboard.
- **GUI Elements**: Tkinter widgets for labels, entry, buttons, and layout.
