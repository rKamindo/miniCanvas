

from user import User, UserManager


def test_create_user_successful():
  user_manager = UserManager()

  user_id = user_manager.create_a_user("John", "password", "student")

  assert user_id in [user.user_id for user in user_manager.user_list]

def test_create_user_without_name_password_type_unsuccessful():
    user_manager = UserManager()

    user_id = user_manager.create_a_user("", "", "")

    assert user_id is None
    assert user_id not in [user.user_id for user in user_manager.user_list]

def test_find_all_users_returns_all_matching_users():
    user_manager = UserManager()

    user1 = User(1, "User 1", "password1", "student")
    user2 = User(2, "USer 2", "password2", "student")

    user_manager.user_list.append(user1)
    user_manager.user_list.append(user2)

    users = user_manager.find_users([user1.user_id, user2.user_id])

    assert users is not None
    assert user1.name in [user.name for user in user_manager.user_list]