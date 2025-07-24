import string
import random
import json
from app.models import URLMapping

DATA_FILE = 'url_data.json'

def load_mappings():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [URLMapping.from_dict(entry) for entry in data]
    except FileNotFoundError:
        return []

def save_mappings(mappings):
    with open(DATA_FILE, 'w') as f:
        json.dump([m.to_dict() for m in mappings], f, indent=2)

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
