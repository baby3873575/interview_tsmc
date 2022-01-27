import sys, time
sys.path.append('./src')
import pytest
from datetime import datetime, timedelta, timezone
from app import create_app



@pytest.fixture
def ut_testclient():
    app = create_app('testing')
    test_client = app.test_client()
    app_context = app.app_context()
    app_context.push()
    yield test_client
    print("====tear down ut_testclient===")
    app_context.pop()



#TODO: should offline copy the data to local and put to storage
@pytest.fixture
def syncdata(ut_testclient):
    rv = ut_testclient.post(
    '/api/v1/usersync',
    content_type="application/json")
    assert rv.status_code == 201
    yield
    print("====tear down syncdata===")
    #TODO: clean up mockdb