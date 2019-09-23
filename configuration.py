class Configuration:
        DISCOVERY_SCAN_DELAY = 5

        CHECKS_PATH = "checks.txt"

        CHECK_FILE = "checkInfo.json"   # File to write in
        CHECK_ADDRS = ["C:\printInfo\printer2.ini"] # list of Files to read from
        CHECK_MANUF = ["სამზარეულო","ბარი"] # list of Files to read from
        FLAG_FILE = "C:/printInfo/kds_orders.md5"

        MENU_INI = "C:/terminalInfo/menu.ini"
        MENU_ = "menu.json"

        DATE_TIME_FORMAT = '%d/%m/%y  %H:%M:%S'

        SQL_DB = 'checksInfo.db'

        STATUS_CHECK_OPEN = 0
        STATUS_CHECK_EDITED = 1
        STATUS_CHECK_TABLE_CANCELLED = 2

        STATE_IN_PROGRESS = 0
        STATE_IN_QUEUE = 1
        STATE_DONE = 2
        STATE_ERROR = 3
