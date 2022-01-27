from app.libs.users_manager import UsersManager
from unittest.mock import patch
import pytest

@patch("app.libs.jsonplaceholder_connector.Jsonplaceholder_connector.get_users",side_effect=None)
def test_sync_user_source_not_available(mock_getUser):
    mock_getUser.return_value = None
    with pytest.raises(Exception):
        UsersManager.sync_users_from_source()


def test_get_users():
    um = UsersManager()
    ul = um.get_users_list()
    assert(len(ul))>0


def test_get_user():
    um = UsersManager()
    ul = um.get_user(user_id=1)
    assert ul is not None