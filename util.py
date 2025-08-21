import logging

# Configure logging
logging.basicConfig(filename='dups.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def print_log(msg, output=True):
    if output:
        print(msg)
    logging.info(msg)
