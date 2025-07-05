import os
import re

words = ["password", "user", "pass"]
rx = re.compile('|'.join(words), re.IGNORECASE)

for root, dirs, files, in os.walk("E:\\test"):
    for filename in files:
        file_path = os.path.join(root, filename)
        try:
            with open(file_path, 'r', errors='ignore') as df:
                data = df.read()
            for match in rx.finditer(data):
                print(f"Match found in {file_path}:{match.group()} at position {match.span()}")
                print(" ")
        except Exception as e:
            print(f"could not read file: {file_path}. Reason: {e}")