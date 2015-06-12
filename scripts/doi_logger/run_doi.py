import sys
sys.path.append('D:\Dropbox\Code\Python\loggers')
from loggers.doi_logger import *
import threading


class GetPdfUrlThread(threading.Thread):
    def __init__(self, func, args, name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def get_result(self):
        return self.url, self.name

    def run(self):
        print "\nCheck: %s...\n" % self.name
        self.url = apply(self.func, self.args)
        if self.url:
            print "\nIn %s.\n" % self.name
        else:
            print "\nNot in %s.\n" % self.name


if len(sys.argv) != 2:
    print "Usage: %s doi number.\n" % (sys.argv[0])
else:
    doi_number = str(sys.argv[1])
    print 'doi: %s\n' % doi_number
    #instance of DoiLogger
    print "Create logger instance..."
    m = DoiLogger(need_data_file=False)
    print 'Ok.\n'
    #get page content
    form_data_dict = {'hdl': doi_number}
    print "Geting page content..."
    print "This may take a minute, please wait..."
    page_content = m.send_post(m.url_login, form_data_dict)
    print "Ok.\n"

    #gather thread objects
    threads = []
    for database_type in m.database_dict:
        #method to get pdf url
        func = m.database_dict[database_type]
        #get args(tuple)
        if database_type == 'ACS':
            args = (page_content, doi_number)
        elif database_type == 'Wiley':
            args = (doi_number, )
        else:
            args = (page_content, )

        #create thread object
        t = GetPdfUrlThread(func, args, database_type)
        threads.append(t)

    nthreads = len(threads)  # number of thread

    #start threads
    for i in xrange(nthreads):
        threads[i].start()

    for i in xrange(nthreads):
        threads[i].join()
        url, name = threads[i].get_result()
        if url:
            pdf_url = url
            database_name = name

    if not database_name:
        raise ValueError("Unspported database.")
    #download pdf
    #choose download method
    if database_name == 'Springer':
        download_method = m.download_pdf_by_urllib
        print "Use urllib to download..."
    else:
        download_method = m.download_pdf_by_requests
        print "Use requests to download..."

    save_name = database_name + '.pdf'
    target_path = './'

    print "Downloading %s..." % save_name
    print "Download time depends on the size of file."
    print "Please wait..."
    try:
        download_method(pdf_url, target_path, save_name)
    except:
        print "\nOops! A exception was detected."
        print "Maybe the PDF file dosen't exist."
        sys.exit()
    print 'Ok. Complete!\nGo and check your file!'
