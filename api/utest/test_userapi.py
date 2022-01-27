import sys
sys.path.append('./src')
import functools,operator,collections



def test_sync_users(ut_testclient):
    rv = ut_testclient.post(
        '/api/v1/usersync',
        content_type="application/json")
    assert rv.status_code == 201



def test_get_users_list(ut_testclient,syncdata):
    rv = ut_testclient.get('/api/v1/users')
    assert len(rv.json) > 0
    assert rv.status_code == 200




def test_get_user(ut_testclient,syncdata):
    rv = ut_testclient.get('/api/v1/user/1')
    assert rv.status_code == 200