import logging

logging.basicConfig(
            filename="log.log",
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )


logging.error("hello error")
logging.critical("hello critical")
logging.debug("hello debug")
logging.exception("hello Exception")
logging.fatal("hello fatal")
logging.log(3, "hello log")
logging.warning("hello warning")