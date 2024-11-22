# В любом ENV работает (стандартная модуль winreg идет вместе с python))

import winreg

def enum_installed_soft(sub_key, sub_key_name):
    try:
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_key, 0, winreg.KEY_READ)
        index = 0
        while True:
            try:
                key_name = winreg.EnumKey(hkey, index)
                sub_key_path = sub_key + "\\" + key_name
                hsubkey = winreg.OpenKey(hkey, key_name)
                sub_key_value = winreg.QueryValueEx(hsubkey, sub_key_name)[0]
                print(f"{key_name} : {sub_key_value}")
                winreg.CloseKey(hsubkey)
                index += 1
            except OSError:
                break
    except FileNotFoundError:
        return False
    finally:
        if hkey:
            winreg.CloseKey(hkey)
    return True

def main():
    enum_installed_soft("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall", "DisplayName")
    enum_installed_soft("Software\\Classes\\Installer\\Products", "ProductName")

if __name__ == "__main__":
    main()