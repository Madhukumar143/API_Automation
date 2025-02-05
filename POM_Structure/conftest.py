from datetime import datetime
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/reports_{now}.html"

@pytest.fixture()
def setup_teardown():
    print("Starting")
    yield
    print("End")