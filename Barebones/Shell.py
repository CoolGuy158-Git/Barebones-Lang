# /// Barebones \\\
# A minimalist experimental programming language
# MIT License © 2025 CoolGuy158

import Barebones

while True:
    text = input(">>> ")
    result, error = Barebones.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)


