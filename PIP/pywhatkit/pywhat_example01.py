# conda activate allpy310

import pywhatkit

# Отправить WhatsApp сообщение контакту +77654321000 в 17:35
# Отправка осуществляется открытием web-версии whatsapp в браузере по умолчанию и отправки сообщения там
pywhatkit.sendwhatmsg("+77654321000", "Test message. WTF", 17, 35)
# В папке со скриптом создает файл PyWhatKit_DB.txt, где хранит задания по отправке

'''
Date: 14/3/2025
Time: 17:34
Phone Number: +7765432100
Message: Test message. WTF
--------------------
'''

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
#pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
#pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
#pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
#pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
#pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# Play a Video on YouTube
#pywhatkit.playonyt("PyWhatKit")
