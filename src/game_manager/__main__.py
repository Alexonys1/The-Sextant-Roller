from loguru import logger

from game_manager.roller import run_roll


logger.add(
    sink="logs.log",
    format="[{time: DD.MM.YYYY HH:MM:SS} {level}]: {message}",
    level="DEBUG"
)


@logger.catch
def main() -> None:
    run_roll()


if __name__ == '__main__':
    main()
