from game_manager.user import User
from data_classes import Region


# TODO: Сделать так, чтобы настройки сохранялись в AppData Windows.
def run_roll() -> None:
    user = User()
    user.open_user_stash()
    for _ in range(10):
        user.move_to_region(Region(500, 500, 500, 500), duration=0.3)
        user.make_left_mouse_click()
