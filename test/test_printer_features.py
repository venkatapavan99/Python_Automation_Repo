from utils.driver_factory import get_driver

def test_9up_feature():
    driver = get_driver()
    driver.get("https://example.com")
    assert "Example" in driver.title
    driver.quit()

def test_booklet_feature():
    driver = get_driver()
    driver.get("https://example.com")
    assert driver.current_url == "https://example.com/"
    driver.quit()

