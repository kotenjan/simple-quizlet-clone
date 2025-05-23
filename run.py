import os
import json
import re

for root, _, files in os.walk('.'):
    for fname in files:
        if fname.lower().endswith('.json'):
            path = os.path.join(root, fname)
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for item in data:
                item['answer'] = re.split(r'[\\/]', item['answer'])[-1]
                item['question'] = re.split(r'[\\/]', item['question'])[-1]
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
