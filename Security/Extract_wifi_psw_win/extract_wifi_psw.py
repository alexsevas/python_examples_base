import subprocess

def extract_wifi_password():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('cp866', errors='ignore').split('\n')
    # print(profiles_data)
    #
    # for item in profiles_data:
    #     print(item)

    profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i]
    # print(profiles)

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('cp866', errors='ignore').split('\n')
        #print(profile_info)

        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i][0]
        except IndexError:
            password = None

        # print(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}') # Результат скрипта в консоль
        with open(file='wifi_passwords.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}')

def main():
    extract_wifi_password()

if __name__ == '__main__':
    main()