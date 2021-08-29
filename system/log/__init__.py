import logging


logging.basicConfig(filename="output",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


def job_title(m: str):
    logging.debug("["+f"{m}".center(40)+"]")
