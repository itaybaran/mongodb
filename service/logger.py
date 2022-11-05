import logging
import time
import os


class Logger:
    def __init__(self,configuration):
        self.log_dir_path= configuration.get_log_dir_path()
        self.log_level=configuration.get_log_level()
        self.logger = logging.getLogger(configuration.get_log_name()) #To start logging using the Python logging module, the factory function logging.getLogger(name) is typically executed.
                                                                      #The getLogger() function accepts a single argument - the logger's name.
                                                                      #It returns a reference to a logger instance with the specified name if provided, or root if not.
                                                                      #Multiple calls to getLogger() with the same name will return a reference to the same logger object.

    def set_logger(self):
        try:
            self.logger.setLevel(self.log_level)
            # create console handler and set level to debug
            ch = logging.StreamHandler() # The StreamHandler class, located in the core logging package, sends logging output to streams such as sys.stdout,
                                         # sys.stderr or any file-like object (or, more precisely, any object which supports write() and flush() methods).
                                         # class logging.StreamHandler(stream=None)
                                         # Returns a new instance of the StreamHandler class. If stream is specified, the instance will use it for logging output;
                                         # otherwise, sys.stderr will be used.The StreamHandler class, located in the core logging package, sends logging output to streams
                                         # such as sys.stdout, sys.stderr or any file-like object (or, more precisely, any object which supports write() and flush() methods).
            ch.setLevel(self.log_level)
            # create file handler and set level to info
            file_name = time.strftime("%Y-%m-%d") + '.log'
            file_path = self.log_dir_path
            file_location = os.path.join(file_path,file_name)

            fl = logging.FileHandler(filename=file_location, encoding='utf-8') # If errors is specified, it’s used to determine how encoding errors are handled.
                                                                               # FileHandler() is a subclass of the Handler class. The FileHandler() class, located in the core logging package,
                                                                               # sends the logging output to disk-file. it inherits the output functionality from StreamHandler
                                                                               # return a new instance of FileHandler class.

            fl.setLevel(self.log_level)

            # create formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # add formatter to ch
            ch.setFormatter(formatter)
            # add formatter to ch
            fl.setFormatter(formatter)

            # add handlers to logger
            self.logger.addHandler(ch)
            self.logger.addHandler(fl)
        except Exception as e:
            print("Unable to create Logger {}"+e)