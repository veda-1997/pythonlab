import re

def clean_text(html):
    html = re.sub(r'<[^>]+>', '', html)
    html = re.sub(r'\s+', ' ', html)
    return html.strip()

text = "<p>Unity   in <b>Diversity</b></p>\n   is our strength."

print(clean_text(text))

# Output:
# Unity in Diversity is our strength.
