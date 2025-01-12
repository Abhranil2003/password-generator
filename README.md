# Password Generator

A Python-based password generator that creates secure passwords with customizable length and character composition. This tool is designed to help users create strong and unpredictable passwords for enhanced security.

## Features

- Generate passwords of any length.
- Include/exclude uppercase letters, numbers, and special characters.
- Simple and interactive command-line interface.

## Requirements

- Python 3.x

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. Ensure you have Python 3 installed. You can check by running:

   ```bash
   python3 --version
   ```

## Usage

1. Run the script:

   ```bash
   python3 password-generator.py
   ```

2. Follow the prompts to generate a password:
   - Enter the desired password length.
   - Specify whether to include uppercase letters, numbers, and special characters.

3. The generated password will be displayed in the terminal.

## Example

Below is an example of the interaction with the program:

```text
Enter the length of the password: 12
Include uppercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): yes

A strong password has been generated. Please copy it from the program output.
%jD8@X!a$R2&
```

## Code Overview

### password_generator.py

This script contains:

- **`password_generator(length, use_uppercase, use_numbers, use_special_chars)`**: Generates a password based on the specified criteria.
- **`main()`**: The entry point of the script, providing an interactive interface for the user.

## Contributing

Contributions are welcome! If you have ideas for improving this project or find a bug, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

**Author:** Abhranil Poddar
