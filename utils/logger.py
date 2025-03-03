import logging
import os

# Create logs directory if it doesn't exist
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure log file path
log_file = os.path.join(log_dir, "test_execution.log")


def setup_logger(name="test_framework"):
    """
    Sets up a logger that logs messages from all modules, including test logs.
    Also Ensures handlers are not duplicated.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # Capture all log levels

    # Prevent duplicate handlers
    if not logger.hasHandlers():
        # File Handler - Logs to a file
        file_handler = logging.FileHandler(log_file, mode="w")  # Append mode
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s"))

        # Console Handler - Logs to terminal
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Only show INFO+ logs in console
        console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


# Create a global logger instance
logger = setup_logger()
