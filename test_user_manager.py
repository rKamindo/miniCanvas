

from user import UserManager


def test_create_user_successful():
  user_manager = UserManager()

  user_id = user_manager.create_a_user("John", "password", "student")

  assert user_id in [user.user_id for user in user_manager.user_list]

def test_create_user_without_name_password_type_unsuccessful():
    user_manager = UserManager()

    user_id = user_manager.create_a_user("", "", "")

    assert user_id is None
    assert user_id not in [user.user_id for user in user_manager.user_list]
