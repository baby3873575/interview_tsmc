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
@pytest.fixture(scope="session",autouse=True)
def syncdata():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()
    from app.libs.users_manager import UsersManager
    UsersManager.sync_users_from_source()
    yield
    print("====tear down syncdata===")
    app_context.pop()
    #TODO: clean up mockdb