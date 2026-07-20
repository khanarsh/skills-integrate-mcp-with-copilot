import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import src.app as app_module


@pytest.fixture
def app_module_fixture(tmp_path):
    app_module.DATA_FILE = tmp_path / "activities.json"
    app_module.activities = app_module.load_activities()
    yield app_module


def test_activity_data_persists_to_disk(app_module_fixture):
    app_module_fixture.signup_for_activity("Chess Club", "persist@example.com")

    reloaded = app_module_fixture.load_activities()

    assert "persist@example.com" in reloaded["Chess Club"]["participants"]
    assert app_module_fixture.DATA_FILE.exists()
