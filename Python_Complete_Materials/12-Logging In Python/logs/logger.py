## configuring logging
import logging

logging.basicConfig(
    filename='/Users/tahir/Desktop/Github/MLOps/Python_Complete_Materials/12-Logging In Python/logs/app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )