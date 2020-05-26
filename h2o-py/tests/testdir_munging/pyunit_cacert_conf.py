import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils
from h2o.exceptions import H2OConnectionError


def test_cacert_in_config():
    cfg = {
        "ip": "self-signed.badssl.com",
        "port": 443,
        "verify_ssl_certificates": True,
        "https": True
    }
    try:
        h2o.connect(config=cfg)
        assert False
    except H2OConnectionError as e:
        assert "CERTIFICATE_VERIFY_FAILED" in e.message

    # not ideal, but at least we test the parameter does get used
    cfg["cacert"] = "/invalid/cacert/path"
    try:
        h2o.connect(config=cfg)
        assert False
    except H2OConnectionError as e:
        assert "No such file or directory" in e.message


if __name__ == "__main__":
    pyunit_utils.standalone_test(test_cacert_in_config)
else:
    test_cacert_in_config()
