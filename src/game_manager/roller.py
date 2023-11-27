from game_manager.user import User


# TODO: Сделать так, чтобы настройки сохранялись в AppData Windows.
def run_roll() -> None:
    user = User()
    user.open_user_stash()
