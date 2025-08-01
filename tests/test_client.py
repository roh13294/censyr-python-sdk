import censyr_sdk

def test_import_and_client_class():
    # Package imports successfully
    assert censyr_sdk.__version__ == "1.0.0"
    # Client class exists
    assert hasattr(censyr_sdk, "CensyrClient")
    client = censyr_sdk.CensyrClient("https://api.censyr.ai", "fake_key")
    assert client.base_url == "https://api.censyr.ai"
