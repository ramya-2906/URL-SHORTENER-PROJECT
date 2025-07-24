class URLMapping:
    def __init__(self, short_code, original_url):
        self.short_code = short_code
        self.original_url = original_url

    def to_dict(self):
        return {
            "short_code": self.short_code,
            "original_url": self.original_url
        }

    @staticmethod
    def from_dict(data):
        return URLMapping(data['short_code'], data['original_url'])
