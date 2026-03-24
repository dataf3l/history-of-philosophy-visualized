import os
from pathlib import Path
from typing import List

def split_file_by_delimiter(input_filename: str, delimiter: str = "---") -> None:
    """
    Reads an input file and splits its content into multiple numbered .txt files
    based on a specific line delimiter.
    """
    input_path = Path(input_filename)
    
    if not input_path.exists():
        print(f"Error: {input_filename} not found.")
        return

    # Initialize counters and buffers
    file_count: int = 1
    current_content: List[str] = []

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Check if the line is exactly the delimiter (stripped of whitespace)
            if line.strip() == delimiter:
                if current_content:
                    write_to_disk(file_count, current_content)
                    file_count += 1
                    current_content = []
            else:
                current_content.append(line)

        # Write the final chunk if it exists
        if current_content:
            write_to_disk(file_count, current_content)

def write_to_disk(index: int, lines: List[str]) -> None:
    """Writes a list of strings to a zero-padded filename."""
    # Format index as 01, 02, 03...
    filename = f"{index:02d}.txt"
    
    with open(filename, 'w', encoding='utf-8') as out:
        out.writelines(lines)
    
    print(f"Created: {filename}")

if __name__ == "__main__":
    split_file_by_delimiter("glm-output.txt")