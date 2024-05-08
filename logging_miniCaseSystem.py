import logging

logging.basicConfig(level=logging.INFO, filename="miniCaseSystem.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("Warning")
logging.error("error")
logging.critical("critical")