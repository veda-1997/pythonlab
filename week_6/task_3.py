import re

text = "Unity in Diversity!!! Contact unity@gmail.com. Meghana, Veda. I have 3 flags."

text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '[EMAIL HIDDEN]', text)
text = re.sub(r'(\w+),\s*(\w+)', r'\2 \1', text)

def double_number(match):
    return str(int(match.group()) * 2)

text = re.sub(r'\d+', double_number, text)
text, count = re.subn(r'([!?])\1+', r'\1', text)

print(text)
print("Replacements:", count)

# Output:
# Unity in Diversity! Contact [EMAIL HIDDEN]. Veda Meghana. I have 6 flags.
# Replacements: 1
