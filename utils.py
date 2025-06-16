import re
import socket
import ssl
import http.client
from urllib.parse import urlparse

def is_url_valid(url):
    regex = re.compile(
        r'^(?:http|https)://'  # http:// or https://
        r'\w+(?:[\.-]?\w+)*\.\w{2,}(?:\:\d+)?(?:[\/\?#][^\s]*)?$',
        re.IGNORECASE
    )
    return re.match(regex, url) is not None

def resolve_dns(url):
    try:
        hostname = urlparse(url).hostname
        socket.gethostbyname(hostname)
        return True
    except:
        return False

def check_http_response(url):
    try:
        parsed = urlparse(url)
        conn = http.client.HTTPSConnection(parsed.hostname, timeout=5) if parsed.scheme == "https" else http.client.HTTPConnection(parsed.hostname, timeout=5)
        conn.request("HEAD", parsed.path or "/")
        resp = conn.getresponse()
        return resp.status < 400
    except:
        return False

def check_https_certificate(url):
    try:
        hostname = urlparse(url).hostname
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.settimeout(5)
            s.connect((hostname, 443))
            s.getpeercert()
        return True
    except:
        return False

