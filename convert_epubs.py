{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import sys\n",
    "from ebooklib import epub\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "\n",
    "def epub_to_txt(epub_file, output_file):\n",
    "    try:\n",
    "        # Load the EPUB file\n",
    "        book = epub.read_epub(epub_file)\n",
    "\n",
    "        # Initialize an empty string to collect text\n",
    "        all_text = \"\"\n",
    "\n",
    "        # Iterate through the EPUB items\n",
    "        for item in book.items:\n",
    "            if item.get_type(\n",
    "            ) == epub.ITEM_DOCUMENT:  # Check for HTML/XHTML content\n",
    "                # Parse the HTML content\n",
    "                soup = BeautifulSoup(item.get_content(), 'html.parser')\n",
    "\n",
    "                # Extract clean text and append it\n",
    "                text = soup.get_text()\n",
    "                all_text += text + \"\\n\"\n",
    "\n",
    "        # Write the extracted text to the output file\n",
    "        with open(output_file, 'w', encoding='utf-8') as f:\n",
    "            f.write(all_text)\n",
    "\n",
    "        print(f\"Successfully converted '{epub_file}' to '{output_file}'\")\n",
    "    except Exception as e:\n",
    "        print(f\"Error: {e}\")\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    if len(sys.argv) < 2:\n",
    "        print(\n",
    "            \"Usage: python epub_to_txt.py <input_epub_file> [output_txt_file]\")\n",
    "        sys.exit(1)\n",
    "\n",
    "    # Input EPUB file\n",
    "    input_epub = sys.argv[1]\n",
    "\n",
    "    # Output TXT file (default is the same name as input with .txt extension)\n",
    "    output_txt = sys.argv[2] if len(\n",
    "        sys.argv) > 2 else os.path.splitext(input_epub)[0] + \".txt\"\n",
    "\n",
    "    # Convert EPUB to TXT\n",
    "    epub_to_txt(input_epub, output_txt)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "cleaning",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
