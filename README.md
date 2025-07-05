While going through the Penetration Tester path on HTB, I created a few Python scripts to automate tasks and improve my understanding of common pentesting techniques.

# **str_finder.py**
This is a post-exploitation tool that crawls directories to find specific strings or keywords you provide. I may add support for command-line arguments in the future.

# **combo.py**
This script uses combinations and permutations to generate all possible password candidates based on the given words. It's recommended to use this for creating custom wordlists, especially after mutating a base list using tools like Hashcat with the best64.rule. It works like the combinator feature of hashcat
