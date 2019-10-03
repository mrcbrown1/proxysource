import proxysource
import pytest

@pytest.fixture
def passing_test_vectors():
    return [('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt','githubusercontent')]

def test_getDomainPassing(passing_test_vectors):
    for data in passing_test_vectors:
        url = data[0]
        module = data[1]
        assert proxysource.obtain_proxysearch(url).__class__.__name__ == module


@pytest.fixture
def failing_test_vectors():
    return ["http://www.google.co.uk", "github.com"]

def test_getDomainFailing(failing_test_vectors):
    for data in failing_test_vectors:
        url = data
        with pytest.raises(ImportError) as excinfo:
            proxysource.obtain_proxysearch(url)

        assert "cannot be handled by this tool" in str(excinfo.value)
