import vk
import getpass

APP_ID = 6427265
VK_API_VERSION = 5.73


def get_user_login():
    login = getpass._raw_input("Login: ")
    return login


def get_user_password():
    password = getpass.getpass()
    return password


def create_vk_session(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    vk_api = vk.API(session)
    return vk_api


def get_friends_online(vk_session):
    friends_online_ids = vk_session.friends.getOnline(v=VK_API_VERSION)
    return friends_online_ids


def get_friends_online_info(friends_online_ids, vk_session):
    friends_online_info = vk_session.users.get(
        user_ids=friends_online_ids, v=VK_API_VERSION)
    return friends_online_info


def output_friends_to_console(friends_online_info):
    for friend in friends_online_info:
        print('{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    vk_session = create_vk_session(login, password)
    friends_online = get_friends_online(vk_session)
    friends_online_info = get_friends_online_info(friends_online, vk_session)
    output_friends_to_console(friends_online_info)
