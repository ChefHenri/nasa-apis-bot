import functools
import logging

from datetime import date

DATE_FMT = '%Y-%m-%d'
LOGGER_NAME = 'nasa_bot_logger'
LOG_FILE = f"nasa-log-{date.today().strftime(DATE_FMT)}.log"
LOG_FMT = '%(asctime)s:%(levelname)s:%(name)s: - %(message)s'


def init_logger(log_lvl, log_dir):
    """ Initializes the logger """
    logging.basicConfig(level=eval(log_lvl), filename=f"{log_dir}/{LOG_FILE}", format=LOG_FMT)


@functools.lru_cache(maxsize=None)
def get_logger():
    """ Gets the root logger and caches it """
    return logging.getLogger(name=LOGGER_NAME)


def wrap(pre, post):
    """ Wrapper """

    def decorate(func):
        """ Decorator """

        def call(*args, **kwargs):
            """ Original function """
            pre(func)
            result = func(*args, **kwargs)
            post(func)

            return result

        return call

    return decorate


def entering(func):
    """ Pre function logging """
    logger = get_logger()

    logger.debug(f"Entered {func.__name__}")
    logger.info(func.__doc__)
    logger.info(f"Function at line {func.__code__.co_firstlineno} in {func.__code__.co_filename}")


def exiting(func):
    """ Post function logging """
    get_logger().debug(f"Exited {func.__name__}")
