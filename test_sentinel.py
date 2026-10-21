
import unittest
from unittest.mock import patch

from sentinel import (
    check_ip,
    check_request
)

class TestSentinel(unittest.TestCase):

    # Tests an allowed IP address
    def test_allowed_ip(self):
        result = check_ip("192.0.2.25")
        self.assertEqual(result, "ALLOW")

    # Tests a blacklisted IP address
    def test_blocked_ip(self):
        result = check_ip("203.0.113.10")
        self.assertEqual(result, "BLOCK")

    # Tests a request from a blacklisted IP
    def test_blocked_request(self):
        result = check_request("203.0.113.10", "Hello")
        self.assertEqual(result, "BLOCK: IP address is blacklisted")

    # Tests a suspicious payload
    def test_suspicious_payload(self):
        result = check_request("192.0.2.25", "Possible malware")
        self.assertEqual(result, "BLOCK: Suspicious payload")

    # Tests a legitimate request
    def test_allowed_request(self):
        result = check_request("192.0.2.25", "Hello")
        self.assertEqual(result, "ALLOW: Request accepted")


if __name__ == "__main__":
    unittest.main()
