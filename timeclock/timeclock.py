################################
# Date/Time Wrapper for Python #
################################
#      Format Directives:      #
# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
################################

import time
from datetime import datetime
import os

class Clock:

    def __init__(self, cZone):
        self.cZone = cZone

    def now(self, format="%H:%M:%S - %m/%d/%Y", tz=None):
        if tz == None:
            os.environ['TZ'] = self.cZone
        else:
            os.environ['TZ'] = tz

        return time.strftime(str(format))

    def elap(self, date1, date2, format="%Y %m %d %H %M %S"):
        td = datetime.strptime(date2, format) - datetime.strptime(date1, format)
        #return dict object
        return {"Hour":td.seconds//3600, "Min":td.seconds//60 , "Sec":td.seconds}
