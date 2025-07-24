import sys
sys.path.append('.')  # Ensures 'app' is recognized as a package

from app.utils import load_mappings, save_mappings, generate_short_code
from app.models import URLMapping

BASE_URL = "http://short.ly/"

def shorten_url(original_url):
    mappings = load_mappings()
    for m in mappings:
        if m.original_url == original_url:
            return BASE_URL + m.short_code

    short_code = generate_short_code()
    while any(m.short_code == short_code for m in mappings):
        short_code = generate_short_code()

    new_mapping = URLMapping(short_code, original_url)
    mappings.append(new_mapping)
    save_mappings(mappings)
    return BASE_URL + short_code

def expand_url(shortened_url):
    mappings = load_mappings()
    short_code = shortened_url.replace(BASE_URL, '')
    for m in mappings:
        if m.short_code == short_code:
            return m.original_url
    return "URL not found."

if __name__ == "__main__":
    print("DEBUG: main block executing")
    print("URL Shortener Menu")
    print("1. Shorten URL")
    print("2. Expand Short URL")
    choice = input("Choose (1 or 2): ").strip()

    if choice == "1":
        long_url = input("Enter long URL: ").strip()
        print("Shortened URL:", shorten_url(long_url))
    elif choice == "2":
        short_url = input("Enter short URL: ").strip()
        print("Original URL:", expand_url(short_url))
    else:
        print("Invalid choice.")
