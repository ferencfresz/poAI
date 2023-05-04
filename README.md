# PO File Translator
This script uses the OpenAI API to translate a .po file from one language to another. It reads in a .po file, loops through the messages within it, and translates them using the OpenAI API. The translated messages are then written back to the .po file and saved.

# Requirements
Python 3.7 or higher
openai library
polib library

# Installation
Clone the repository or download the script file.
Install the required libraries by running pip install -r requirements.txt.
Replace YOUR openai KEY with your OpenAI API key.
Replace YOUR PO FILE with the path to the .po file you want to translate.
Replace YOUR OUTPUT PO FILE with the desired path and name for the translated .po file.
# Usage
Run the script by running python poAi.py in the command line. The translated .po file will be saved in the path specified in step 4 of the installation process. The script waits for a random amount of time between each translation to avoid overloading the OpenAI API.

Note: This script uses the OpenAI API, which requires an API key. Be sure to use your own key and not share it with others.
