
import logging
from pathlib import Path


def setup_logger(log_folder):
    """Configure console and file logging."""

    log_folder = Path(log_folder)
    log_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    logger = logging.getLogger("retail_sales")
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Display logs in the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Save logs to a file
    file_handler = logging.FileHandler(
        log_folder / "automation.log",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger