#!"c:\users\ayanda dladla\documents\another1\anotherone\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'awsebcli==3.19.4','console_scripts','ebp'
__requires__ = 'awsebcli==3.19.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('awsebcli==3.19.4', 'console_scripts', 'ebp')()
    )
