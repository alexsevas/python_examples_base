# conda activate allpy310_2

# C:\Users\USER\.local\share\argos-translate - папка со словарями тут

import argostranslate.package
import argostranslate.translate

from_code = "en"
to_code = "ru"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

# Translate
#translatedText = argostranslate.translate.translate("Hello World. What are fuck?", from_code, to_code)
translatedText = argostranslate.translate.translate('''
We are forming a commission to define best practices for UI/UX design for browser agents. 
Together, we're exploring how software redesign improves the performance of AI agents and gives these companies a 
competitive advantage by designing their existing software to be at the forefront of the agent age.
''', from_code, to_code)
print(translatedText)
# '¡Hola Mundo!'