import logging

def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("test_log.log", mode="w", encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

