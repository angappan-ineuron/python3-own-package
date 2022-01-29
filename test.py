import logging

logging.basicConfig(filename='error.txt', filemode='a',
                    format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level='DEBUG')

logging.error("Test")
logging.info("Info")
