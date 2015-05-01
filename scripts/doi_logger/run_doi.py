import sys
sys.path.append('D:\Dropbox\Code\Python\loggers')
from loggers.doi_logger import *

url = 'http://dx.doi.org/'
m = DoiLogger(need_data_file=False)
