import threading

class Periodic(object):
    '''
    This class represents a list of interfaces and their configurations
    '''
    def __init__(self):
        self.timer = None
    
    def schedule(self):
        if self.timer is not None:
            self.timer.cancel()
        self.timer = threading.Timer(1, self.run)
        self.timer.start()

    def cancel(self):
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None
            
    def run(self):
        raise NotImplemented()

        
# p = Periodic()
# p.schedule()

class OsInterfaces(Periodic):
    def __init__(self):
        Periodic.__init__(self)
        
    def run(self):
        try:
            self.check_new_removed_interfaces()
            self.check_interfaces_status()
        finally:
            self.schedule()

    def x(self):
        ic = IfaceMitmSuitabilityCheck(iface)
        