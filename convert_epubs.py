import warnings

# Suppress FutureWarnings from ebooklib
warnings.filterwarnings("ignore", category=FutureWarning)

import os
from ebooklib import epub
from bs4 import BeautifulSoup

def epub_to_txt(epub_file, output_file):
    """
    Convert a single EPUB file to a TXT file.
    
    Parameters
    ----------
    epub_file : str
        Path to the EPUB file to be converted.
        
    output_file : str
        Path to the output TXT file.
    """
    try:
        # Load the EPUB file
        book = epub.read_epub(epub_file)
        
        # Initialize an empty string to collect text
        all_text = ""

        # Iterate through the EPUB items
        for item in book.items:
            # Check for HTML/XHTML content
            if isinstance(item, epub.EpubHtml):  
                # Parse the HTML content
                soup = BeautifulSoup(item.get_content(), 'html.parser')
                
                # Extract clean text and append it
                text = soup.get_text()
                all_text += text + "\n"

        # Write the extracted text to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(all_text)
        
        print(f"Converted: '{epub_file}' -> '{output_file}'")
    except Exception as e:
        print(f"Error processing '{epub_file}': {e}")

def convert_epub_in_folder(input_folder):
    """
    Convert all EPUB files in the specified folder to TXT files.
    """
    # Check if the folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Folder '{input_folder}' does not exist.")
        return
    
    # Iterate over all files in the folder
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith('.epub'):
            # Construct full file paths
            epub_path = os.path.join(input_folder, file_name)
            txt_path = os.path.join(input_folder, os.path.splitext(file_name)[0] + ".txt")
            
            # Convert EPUB to TXT
            epub_to_txt(epub_path, txt_path)

if __name__ == '__main__':
    # Prompt the user for the folder path
    input_folder = input("Enter the path to the folder containing EPUB files: ").strip()
    convert_epub_in_folder(input_folder)
