# Anew-Py: Append Unique Lines to a File

Anew-Py is a lightweight Python tool inspired by [tomnomnom's anew](https://github.com/tomnomnom/anew). It appends only unique lines to a specified file, making it ideal for tasks like maintaining clean wordlists or datasets during automation processes.

## Features
- Filters and appends **unique lines** to a file.
- Supports **case-insensitive** and **special character-stripped** comparisons.
- Includes a **verbose mode** for real-time feedback on new additions.
- Efficient and scalable, even for large files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/0xBv1/Anew-Py.git
   cd Anew-Py
   ```

2. Make the script executable (optional):
   ```bash
   chmod +x Anew-Py.py
      ```

3. Ensure Python 3 is installed on your system:
   ```bash
   python3 --version
   ```

## Usage

### Basic Syntax
```bash
<command_output> | python enhanced_anew.py <output_file> [options]
```

### Examples

1. Append unique subdomains to `unique_subdomains.txt`:
   ```bash
   cat subdomains.txt | python enhanced_anew.py unique_subdomains.txt
   ```

2. Case-insensitive comparison:
   ```bash
   cat urls.txt | python enhanced_anew.py unique_urls.txt -i
   ```

3. Strip special characters and enable verbose mode:
   ```bash
   cat wordlist.txt | python enhanced_anew.py clean_wordlist.txt -s -v
   ```

### Options
| Flag               | Description                                 |
|--------------------|---------------------------------------------|
| `-i`, `--case-insensitive` | Makes line comparisons case-insensitive.  |
| `-s`, `--strip-special`    | Removes special characters for comparison. |
| `-v`, `--verbose`          | Prints each new line as it is added.      |

### Output
The tool appends new unique lines to the specified file and displays a summary of the number of lines added.

## Example Output
```bash
Added: example.com
Added: testsite.org

2 new unique lines added to unique_subdomains.txt.
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## Contact
For questions or feedback, feel free to open an issue or contact me at [bedoadly12@gmail.com](mailto:bedoadly12@gmail.com).

