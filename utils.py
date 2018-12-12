import logging


def get_logger(name=''):
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter(
		'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	fh = logging.FileHandler('jira_sync.log')
	fh.setLevel(logging.DEBUG)
	fh.setFormatter(formatter)
	logger.addHandler(fh)

	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	ch.setFormatter(formatter)
	logger.addHandler(ch)

	return logger