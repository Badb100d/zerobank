#!/usr/bin/env python3

import logging
logging.basicConfig(filename='demo.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d')
logging.info('test info'+__file__)
logging.debug('test debug')
logging.warning('test warning')
logging.error('test error')
logging.critical('test critical')
