# Python 3 Mercury web browser API

A small script that performs a simple connection to [Mercury Web Parser][url].

## Usage:
```python
from mercury_parser3 import MercuryParser

parser = MercuryParser("<your api key>")
page = parser.parse("http://example.com/")
print(page.title)
```

 Available Attributes:
 - content
 - date_published
 - dek
 - direction
 - domain
 - excerpt
 - lead_image_url
 - next_page_url
 - rendered_pages
 - title
 - total_pages
 - url
 - word_count

See [their site][url] for more.

## License
Licensed under MIT License, see LICENSE.md for more.

[url]:https://mercury.postlight.com/web-parser/ "Mercury Web Parser"
