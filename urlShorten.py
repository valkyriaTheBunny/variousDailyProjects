def main() -> None:
    import string
    import random

    class URLShortener:
        def __init__(self):
            self.url_to_short = {}
            self.short_to_url = {}

        def shorten(self, url):
            if url in self.url_to_short:
                return self.url_to_short[url]

            characters = string.ascii_letters + string.digits
            short_url = ''.join(random.choice(characters) for _ in range(6))
            while short_url in self.short_to_url:
                short_url = ''.join(random.choice(characters) for _ in range(6))

            self.url_to_short[url] = short_url
            self.short_to_url[short_url] = url

            return short_url

        def restore(self, short):
            return self.short_to_url.get(short, None)

    # Example usage
    shortener = URLShortener()
    short_url = shortener.shorten("https://www.google.com")
    print("Short URL:", short_url)
    original_url = shortener.restore(short_url)
    print("Original URL:", original_url)

if __name__ == "__main__":
    main()