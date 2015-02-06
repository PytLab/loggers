# loggers
##A Python library for automatic logging in some websites with other functions##
==================================================================
Author: PytLab <shaozhengjiang@gmail.com>

Version: 0.2.1

==================================================================
Requirements:

	You will need to ensure that you are running python 2.x 
	(2.7.x or greater) on your devices.
	https://www.python.org/download/releases/2.7.6/
	
==================================================================
Update info:
update version 0.2.1:

	Continue to login when there is no internet connection or
	no wlan account logged in.
update version 0.2.0:

	Add new script to download files during 00:00 ~ 7:00
	without costing any credit!
	
update version 0.1.5:
	fix bugs in display of credit number.
	
update version 0.1.4:

	check internet connection in script 'run_emuch.py'
	show credit number
	
update version 0.1.3:

	Fix some bugs.
	
update version 0.1.2:

	remove the application of nonstandard lib -->"BeautifulSoup"
update version 0.1.1:

	show user's coin number in log file.
	
update version 0.1.0 : 

	add EmuchLogger class to log in 'emuch.net' automatically
	add method of EmuchLogger to get credit automatically
	
==================================================================
**if you don't use it as a library, ignore this part**

#####Quick Installation:(in cmd, bash, poweshell)#####
To install, unpack the loggers archive and run
	
    ``python setup.py install``
To uninstall, run 
	
    ``python setup.py install --record log``
a log file will be created,
if you are on Linux, then run
		
    ``cat log | xagrs rm -rf ``

#####Detailed Installation:#####
Add this directory to the PYTHONPATH, 
	
e.g. in bash shell:
	
    ``export PYTHONPATH=$HOME/THIS_FOLDER_PATH:$PYTHONPATH``
		
or in cshell:
	
    ``setenv PYTHONPATH $HOME/THIS_FOLDER_PATH:$PYTHONPATH`` 
or in python shell:
	
    >>> import sys
    >>> sys.path.append(THIS_FOLDER_PATH)

You can alse place 'loggers' into your PYTHONPATH, 
	
e.g. 'C:\Python27\Lib\site-packages' on Windows
'/usr/local/lib/python2.7/site-packages/' on Linux

===================================================================================
##Easy use:##

###  ecust_logger:  ###

I've provide a simple batch script 'run.bat' for you to run the 
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


###  emuch_logger: ###

This is a logger for automatic logging in emuch.net, 
and provide credit getting function and file downloading function.

I've provide a simple script 'run_credit.py' to log in and get today's credit
automatically and  'run_downloader.py' to download file freely at midnight.

####To get credit automatically:####
1. Input your log infomation:
    open loggers/emuch_logger/formdata.txt with any editor,<br>
    change the infomation according your own need, <br>
    e.g. username, password ...

2. It is recommended to put a shortcut of 'run_credit.bat' to your startup directory<br>
   e.g.C:\Users\**\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup<br>
   to get your credit once your PC booting.

3. If you want to run it manually, just double tap the 'run_credit.bat' <br>
   or 'run_emuch.py'.

4. All infomation are written in 'emuch.log'.

####To get download file for free at midnight:####

1.put urls of downoad pages into 'download_list.txt'

2.then just double tap 'run_downloader.bat' or 'run_downloader.py' before 00:00

3.the script will download for you automatically. Check files in the './emuch_download/'the next day,<br>
  because some files may be crrupted(´-ι_-｀)
	  
=====================================================================================
