from itertools import permutations, combinations

# put the words from custom list to make every possible combination from them, include special characters (like !, @, #, $) for better passwords
words = [
    "!", "!!", "#", "#!", "@", "@!", "05", "05!", "051", "058", "059",
    "!1", "#1", "@1", "1998", "1998!", "19981", "19988", "19989", "5", "5!",
    "51", "58", "59", "!8", "#8", "@8", "!9", "#9", "@9",
    "alex", "Alex", "Alex!", "Alex1", "Alex8", "Alex9",
    "august", "August", "August!", "August1", "August8", "August9",
    "baseball", "Baseball", "Baseball!", "Baseball1", "Baseball8", "Baseball9",
    "Bell@", "Bell@!", "bella", "Bella", "Bella!", "Bella1", "Bella8", "Bella9",
    "B@seb@ll", "B@seb@ll!", "@lex!", "maria", "Maria", "Maria!", "Maria1", "Maria8", "Maria9",
    "mark", "Mark", "Mark!", "Mark1", "Mark8", "Mark9", "markwhite", "Markwhite",
    "Markwhite!", "Markwhite1", "Markwhite8", "Markwhite9", "M@ri@", "M@ri@!",
    "M@rk", "M@rk!", "M@rkwhite", "M@rkwhite!", "Nexur@", "Nexur@!", "nexura", "Nexura",
    "Nexura!", "Nexura1", "Nexura8", "Nexura9", "sanfrancisc0", "Sanfrancisc0",
    "Sanfrancisc0!", "Sanfrancisco!", "Sanfrancisco1", "Sanfrancisco8", "Sanfrancisco9",
    "S@nfr@ncisc0", "S@nfr@ncisc0!", "S@nfr@ncisco", "S@nfr@ncisco!", "@ugust!"
]

max_words_in_combo = 3 
output = set()

for r in range(1, max_words_in_combo + 1):
    for combo in combinations(words, r):
        for perm in permutations(combo):
            joined = ''.join(perm)
            if len(joined) >= 12: #maximum lenght of password
                output.add(joined)


with open("filtered_combinations.txt", "w") as f:
    for line in sorted(output):
        f.write(line + "\n")

print(f"Saved {len(output)} combinations with length >= 12 to 'filtered_combinations.txt'")
