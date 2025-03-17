import json
import os
from datetime import datetime
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = os.path.abspath(os.path.join("..", "reports"))
    os.makedirs(report_dir, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/reports_{now}.html"

@pytest.fixture()
def setup_teardown():
    print("Starting")
    yield
    print("End")

@pytest.fixture()
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","payload.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data