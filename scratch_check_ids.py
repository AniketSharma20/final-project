import re, collections
text = open('templates/dashboard.html', encoding='utf-8').read()
ids = re.findall(r'id=\"([^\"]+)\"', text)
dups = collections.Counter(ids)
for k, v in dups.items():
    if v > 1:
        print(f"Duplicate ID: {k} (found {v} times)")
