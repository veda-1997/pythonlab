import re

pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
variables = ["_count2", "2fast", "total_sum"]

for var in variables:
    print(var, ":", bool(re.fullmatch(pattern, var)))

pets = "I have a cat, a dog, and a bird. My cat likes to play with the dog."
pattern = r'\b(cat|dog|bird)\b'
print(re.findall(pattern, pets))

colors = "#FFAA00 #000 #12AB #ABCDEF"
pattern = r'^#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?$'

for color in colors.split():
    print(color, ":", bool(re.fullmatch(pattern, color)))

log = "2024-06-01 08:15:32 ERROR Disk full"
pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.*)'

match = re.match(pattern, log)

print("Date:", match.group("date"))
print("Time:", match.group("time"))
print("Level:", match.group("level"))
print("Message:", match.group("message"))

# Output:
# _count2 : True
# 2fast : False
# total_sum : True
# ['cat', 'dog', 'bird', 'cat', 'dog']
# #FFAA00 : True
# #000 : True
# #12AB : False
# #ABCDEF : True
# Date: 2024-06-01
# Time: 08:15:32
# Level: ERROR
# Message: Disk full
