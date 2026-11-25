import logging

logger = logging.getLogger("Experiment14Logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("experiment14.log", mode="a", encoding="utf-8")

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("DEBUG: Detailed diagnostic information for troubleshooting.")
logger.info("INFO: Program started and is running normally.")
logger.warning("WARNING: Disk space is running low; check system storage.")
logger.error("ERROR: Failed to open the requested data file.")
logger.critical("CRITICAL: Serious system failure; application cannot continue.")
