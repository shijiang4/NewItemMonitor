import pycurl
from io import BytesIO

# Buffer to store the response
buffer = BytesIO()

# Initialize a cURL object
curl = pycurl.Curl()

# Set the URL to fetch
curl.setopt(pycurl.URL, "http://example.com")

# Set proxy details
curl.setopt(pycurl.PROXY, "http://proxy_address:proxy_port")  # Proxy URL
# curl.setopt(pycurl.PROXY, "socks5://proxy_address:proxy_port")  # For SOCKS5 proxy

# Optional: Set proxy authentication if required
# curl.setopt(pycurl.PROXYUSERPWD, "username:password")

# Set user agent to mimic a real browser
curl.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# Set timeout
curl.setopt(pycurl.TIMEOUT, 10)

# Write response to buffer
curl.setopt(pycurl.WRITEDATA, buffer)

# Perform the request
try:
    curl.perform()
    http_code = curl.getinfo(pycurl.HTTP_CODE)
    print(f"HTTP Response Code: {http_code}")
    print(buffer.getvalue().decode('utf-8'))  # Print the response
except pycurl.error as e:
    print(f"Error: {e}")
finally:
    # Clean up
    curl.close()
