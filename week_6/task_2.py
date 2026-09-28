import re

paragraph = "NASA and USA scientists developed advanced technology for international research."

capital_words = re.findall(r"\b[A-Z]{2,}\b", paragraph)
print("Capital words:", capital_words)

for match in re.finditer(r"\b\w{7,}\b", paragraph):
    print(match.group(), match.start())

prices = "apples: $3.50, bananas: $1.20, mango: $4.75"

amounts = re.findall(r"\$\d+\.\d+", prices)
print("Dollar amounts:", amounts)

print("Number of occurrences:", len(re.findall(r"\b\w{7,}\b", paragraph)))
#Capital words: ['NASA', 'USA']
#scientists 13
#developed 24
#advanced 34
#technology 43
#international 58
#research 72
#Dollar amounts: ['$3.50', '$1.20', '$4.75']
#Number of occurrences: 6
