import openai
import polib
import time
import random

# Setting the appropriate API key
openai.api_key = 'YOUR openai KEY'

# Reading in the .po file to be translated
po = polib.pofile('YOUR PO FILE')

# Translating the texts within the following loop
for entry in po:
    text = entry.msgid
    # If the text is empty or already translated, skip it
    if not text or entry.msgstr:
        continue

    prompt=f"translate to YOUR LANGUAGE: {text}"
    # Translating the text using the OpenAI API
    result = openai.Completion.create(
        engine='text-davinci-003',
        prompt= prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.1
    )

    # Writing the translated text to the .po file
    entry.msgstr = result.choices[0].text.strip()

    print(text,entry.msgstr)

    # Waiting for a random amount of time between 1 and 2 seconds to avoid overloading the API
    wait_time = random.randint(1, 2)
    time.sleep(wait_time)

# Saving the .po file that contains the translated results
po.save('YOUR OUTPUT PO FILE')
