import time

class EmonHubCargo(object):
    uri = 0
    timestamp = 0.0
    target = 0
    nodeid = 0
    realdata = []
    rssi = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, timestamp, target, nodeid, realdata, rssi, rawdata):
        EmonHubCargo.uri += 1
        self.uri = EmonHubCargo.uri
        self.timestamp = float(timestamp)
        self.target = int(target)
        self.nodeid = int(nodeid)
        self.realdata = realdata
        self.rssi = int(rssi)

        self.datacodes = []
        self.datacode = ""
        self.scale = 0
        self.scales = []
        self.rawdata = rawdata
        self.encoded = {}
        self.realdatacodes = []

def new_cargo(rawdata="", realdata=[], nodeid=0, timestamp=0.0, target=0, rssi=0.0):
    """

    :rtype : object
    """

    if not timestamp:
        timestamp = time.time()
    cargo = EmonHubCargo(timestamp, target, nodeid, realdata, rssi, rawdata)
    return cargo
