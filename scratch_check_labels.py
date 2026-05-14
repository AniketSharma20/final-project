import re

text = open('templates/dashboard.html', encoding='utf-8').read()
# Find all labels
labels = re.finditer(r'<label\b([^>]*)>(.*?)</label>', text, re.DOTALL | re.IGNORECASE)

# Also find all input, select, textarea ids
input_ids = set(re.findall(r'id=["\']([^"\']+)["\']', text))

violating_labels = []
for idx, match in enumerate(labels):
    attrs = match.group(1)
    content = match.group(2)
    
    # Check for 'for' attribute
    for_match = re.search(r'for=["\']([^"\']+)["\']', attrs)
    
    if for_match:
        for_id = for_match.group(1)
        if for_id not in input_ids:
            violating_labels.append(f"Label {idx} has for='{for_id}' but no such ID exists.")
    else:
        # Check if it wraps an input, select, or textarea
        if not re.search(r'<(input|select|textarea)\b', content, re.IGNORECASE):
            violating_labels.append(f"Label {idx} has NO 'for' attribute and NO nested input: {attrs} -> {content.strip()}")

for v in violating_labels:
    print(v)
print(f"Total violating labels found: {len(violating_labels)}")
