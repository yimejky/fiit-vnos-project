import logging

formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

