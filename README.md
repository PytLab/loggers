# loggers #
##A Python library for automatic logging in some websites with some practical functions##

####Author: ####
  PytLab **<shaozhengjiang@gmail.com>**

####Version: ####
  0.3.0

####Requirements:####

  - You will need to ensure that you are running python 2.x 
  (2.7.x or greater) on your devices.[**python2.7.6**](https://www.python.org/download/releases/2.7.6/)
  - If you use `doi_logger.py`, you will also need to install [**Beautiful Soup**](http://www.crummy.com/software/BeautifulSoup/).

####Latest update info:####
#####Version 0.3.0:#####

Add `DoiLogger()` class which provide methods to download paper according to DOI number you provide.

e.g. DOI: 10.1007/s10562-013-1133-0.

最新添加了根据DOI号直接下载相应文献的功能。

例如DOI：10.1007/s10562-013-1133-0 自动下载相应文献到当前目录。

Database supported (目前支持的数据库):
  
  - [ACS](http://pubs.acs.org/)
  - [Elsevier ScienceDirect](http://www.sciencedirect.com/)
  - [Wiley](http://onlinelibrary.wiley.com/)
  - [Springer](http://link.springer.com/)
  - [Nature](http://www.nature.com/nature/index.html)
  - [RSC](http://www.rsc.org/)

###If you don't use it as a library, ignore this part, go to 'Easy use' below###

----------

#####Quick Installation:(in cmd, bash, poweshell)#####
To install, unpack the loggers archive and run
	
    python setup.py install
To uninstall, run 
	
    python setup.py install --record log
a log file will be created,
if you are on Linux, then run
		
    cat log | xagrs rm -rf

#####Detailed Installation:#####
Add this directory to the PYTHONPATH, 
	
e.g. in bash shell:
	
    export PYTHONPATH=$HOME/THIS_FOLDER_PATH:$PYTHONPATH
or in cshell:
	
    setenv PYTHONPATH $HOME/THIS_FOLDER_PATH:$PYTHONPATH
or in python shell:
	
    >>> import sys
    >>> sys.path.append(THIS_FOLDER_PATH)
You can alse place 'loggers' into your PYTHONPATH, 
	
e.g. 'C:\Python27\Lib\site-packages' on Windows
'/usr/local/lib/python2.7/site-packages/' on Linux

###Easy use:###
---------------
下面的脚本均可**免安装直接运行**，运行方法：

用编辑器打开`run_credit.py`, `run_downloader.py`, `run_ecust.py`, `run_doi.py`，然后分别将脚本第二行

    sys.path.append('D:\Dropbox\Code\Python\loggers')

中的路径(`D:\Dropbox\Code\Python\loggers`)改成你下载loggers的目标路径，然后执行即可。

####  doi_logger: ####

I've provide a simple python script `/script/doi_logger/run_doi.py` to download literature from database.

e.g. in powershell, cmd or linux shell, you want to download paper whose DOI is 10.1016/j.apcatb.2014.11.043:
   
    $ cd your_path/loggers/scripts/doi_logger/
    $ python run_doi.py 10.1016/j.apcatb.2014.11.043

wait for a few minutes,
then the corresponding `.PDF` file will appear in current path.

####  ecust_logger:  ####

I've provided a simple batch script 'run.bat' for you to run the 
'run_ecust.py' to log in ECUST Campus Network automatically.

Note: this script provide only automatic wired connection to 
Campus Network with your 4M accounts.

1. Input your log infomation:
   open loggers/ecust_logger/formdata.txt with any editor,
   change the infomation according your own need, 
   e.g. username, password ...

2. If you want to run this script with your computer booting,
   add the shortcut of 'run.bat' to your startup directory, for example
   (C:\Users\**\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup)
   Then the script will start when you boot your system.

3. If you want to run it manually, just double tap the 'run.bat' 
   or 'run_ecust.py'.

4. All infomation are written in 'ecust.log', check it when the script running.

5. Double tap 'stop.bat' to stop the script process.


####  emuch_logger(后面有空会添加Proxy): ####

This is a logger for automatic logging in emuch.net, 
and provide credit getting function and file downloading function.

I've provided a simple script 'run_credit.py' to log in and get today's credit
automatically and  'run_downloader.py' to download file freely at midnight.

- ####To get credit automatically:####
 1. Input your log infomation:
    open loggers/emuch_logger/formdata.txt with any editor,<br>
    change the infomation according your own need, <br>
    e.g. username, password ...

 2. It is recommended to put a shortcut of 'run_credit.bat' to your startup directory<br>
   e.g.C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup<br>
   to get your credit once your PC booting.

 3. If you want to run it manually, just double tap the 'run_credit.bat' <br>
   or 'run_emuch.py'.

 4. All infomation are written in 'emuch.log'.

- ####To get download file for free at midnight:####

 1. Put urls of downoad pages into 'download_list.txt'

 2. Then just double tap 'run_downloader.bat' or 'run_downloader.py' before 00:00

 3. The script will download for you automatically. Check files in the './emuch_download/' the next day, because some files may be corrupted(´-ι_-｀)

 4. Download informations are displayed in command windows, log informations are recorded in 'emuch.log'.
	  
=====================================================================================
