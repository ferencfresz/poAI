# PO File Translator with OpenAI

This script uses the OpenAI API to translate a .po file from one language to another. It reads in a .po file, loops through the messages within it, and translates them using the OpenAI API. The translated messages are then written back to the .po file and saved.

## Requirements
* Python 3.7 or higher
* openai library
* polib library

## Installation
1. Clone the repository or download the script file.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Replace `YOUR openai KEY` with your OpenAI API key.
4. Replace `YOUR PO FILE` with the path to the .po file you want to translate.
5. Replace `YOUR LaANGUAGE` with your language.
6. Replace `YOUR OUTPUT PO FILE` with the desired path and name for the translated .po file.

## Usage
1. Run the script by running `python poAI.py` in the command line.
2. The translated .po file will be saved in the path specified in step 5 of the installation process.
3. The script waits for a random amount of time between each translation to avoid overloading the OpenAI API.

Note: This script uses the OpenAI API, which requires an API key. Be sure to use your own key and not share it with others. 
Please note that this script is experimental and is provided as-is. Use at your own risk and please report any issues or bugs to the author.
