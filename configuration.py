class Configuration:

        SCANNER_DELAY = 2

        CHECKS_PATH = "checks.txt"

        CHECK_FILE = "checkInfo.json"   # File to write in
        CHECK_ADDRS = ["C:\printInfo\printer2.ini"] # list of Files to read from
        CHECK_MANUF = ["სამზარეულო","ბარი"] # list of Files to read from

        STATE_IN_PROGRESS = 0
        STATE_DONE = 1
        STATE_CLOSED = 2
