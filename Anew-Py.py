import sys
from pathlib import Path
import argparse

def normalize_line(line, case_insensitive=False, strip_special=False):
    """Normalize a line for comparison."""
    if case_insensitive:
        line = line.lower()
    if strip_special:
        line = ''.join(filter(str.isalnum, line)) 
    return line.strip()

def anew(input_lines, output_file, case_insensitive=False, strip_special=False, verbose=False):
    output_path = Path(output_file)
    if not output_path.is_file():
        output_path.touch()
    
    existing_lines = set()
    with open(output_file, 'r') as f:
        for line in f:
            existing_lines.add(normalize_line(line, case_insensitive, strip_special))
    
    new_lines_count = 0
    with open(output_file, 'a') as f:
        for line in input_lines:
            clean_line = normalize_line(line, case_insensitive, strip_special)
            if clean_line and clean_line not in existing_lines:
                f.write(clean_line + '\n')
                existing_lines.add(clean_line)
                new_lines_count += 1
                if verbose:
                    print(f"Added: {clean_line}")
    
    print(f"\n{new_lines_count} new unique lines added to {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Append unique lines to a file.")
    parser.add_argument("output_file", help="The file to append unique lines to.")
    parser.add_argument("-i", "--case-insensitive", action="store_true", help="Make line comparison case-insensitive.")
    parser.add_argument("-s", "--strip-special", action="store_true", help="Strip special characters from lines for comparison.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print each new line as it is added.")
    
    args = parser.parse_args()
    output_file = args.output_file
    case_insensitive = args.case_insensitive
    strip_special = args.strip_special
    verbose = args.verbose

    try:
        input_lines = sys.stdin.readlines()  
        anew(input_lines, output_file, case_insensitive, strip_special, verbose)
    except KeyboardInterrupt:
        print("\nOperation canceled.")
    except Exception as e:
        print(f"Error: {e}")
