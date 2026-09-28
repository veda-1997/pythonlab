import re

sentence = "1024 requests were served in 3 seconds"

result = re.match(r"\d", sentence)

if result:
    print("Sentence starts with a digit")
else:
    print("Sentence does not start with a digit")

result = re.search(r"served", sentence)

if result:
    print("Found:", result.group())
    print("Start/End position:", result.span())

s1 = "12345"
s2 = "123a5"

print("12345:", re.fullmatch(r"\d+", s1))
print("123a5:", re.fullmatch(r"\d+", s2))
#Sentence starts with a digit
#Found: served
#Start/End position: (19, 25)
#12345: <re.Match object; span=(0, 5), match='12345'>
#123a5: None
