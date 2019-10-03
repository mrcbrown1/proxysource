import proxysource
import pytest

@pytest.fixture
def get_test_urls():
    return [('http://www.google.com','google'), ('http://www.google.co.uk','google'), ('http://www.google.net','google'), ('http://www.google.biz','google')]


def test_getDomain(get_test_urls):
    for data in get_test_urls:
        url = data[0]
        domain = data[1]
        assert proxysource.utils.getHostnameFromURL(url) == domain
