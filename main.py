import os
import sys

import googletrans
from googletrans import Translator

OUTPUT_DIR_NAME = "translations"

def main():
    args = sys.argv
    if (len(args) != 2):
        print(f"\tUsage: python {args[0]} [INPUT_FILE_NAME]")
        return
    
    content = readTextFile(args[1])
    if (content == None):
        print("ERROR: Unable to read txt file content!")
        return
    
    mkdir(OUTPUT_DIR_NAME)
    translator = Translator()
    langs = googletrans.LANGUAGES

    counter = 1
    langAmount = len(langs)
    for code, name in langs.items():
        name = name.capitalize()

        s = None
        try:
            s = translator.translate(content, dest=code).text
        except ValueError:
            print(f"ERROR: Unable to translate to {name} ({code})", end="")
        else:
            print(f"Translated to {name} ({code})", end="")
            outputPath = f"./{OUTPUT_DIR_NAME}/{name}_{code}.txt"
            ignored = writeTextFile(outputPath, s)
        finally:
            print(f" [{counter} / {langAmount}]")
            counter += 1
        
    print("--- End of Program ---")

def writeTextFile(fileName, content, encoding="utf-8"):
    try:
        with open(fileName, "w+", encoding=encoding) as f:
            f.write(content)
        return True
    except:
        return False

def readTextFile(fileName):
    try:
        s = None
        with open(fileName, "r", encoding="utf-8") as f:
            s = f.read()
        return s
    except:
        return None

def mkdir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

if (__name__ == "__main__"):
    main()