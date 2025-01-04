from signLanguage.exception import SignException
from signLanguage.logger import logging
import sys
try:
    a = 1/2
    logging.info("a: {}".format(a))
except Exception as e:
    exception = SignException(e, sys)
    logging.error(exception)
    raise exception