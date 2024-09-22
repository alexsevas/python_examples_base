# env - all2py310
# pip install python-docx
# pip install windows-tools

import time
from datetime import datetime as dt, timedelta
from platform import node
from struct import unpack
from winreg import OpenKeyEx, QueryValueEx, HKEY_LOCAL_MACHINE, QueryInfoKey, EnumKey, KEY_READ

from docx import Document

from windows_tools import product_key


if __name__ == "__main__":
    main()