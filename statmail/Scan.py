from .SMBase import SMBase
from .Types import Types

""" A class to keep track of server scans.
This is so that they can be collected into a list and re-run or
queried after the fact.
"""

class Scan(SMBase):
    """an object to keep track of a scan on a server"""

    def __init__(self, host, stype):
        """Initalize a scan object."""
        self.host = host
        self.stype = stype
        # get the command for the type
        self.reporter = Type.find_reporter(stype)
        pass

    def remote_run(self, cmd):
        """Run a command on the host for the class."""
        pass

    def scan(self):
        """Run the scan."""
        # check if host is reachable
        # run the command
        for report in self.reporter:
            # add result to end of that report
            report.append(self.remote_run(report[1]))
        return self.reporter
