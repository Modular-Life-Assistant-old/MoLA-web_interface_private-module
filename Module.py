from core import ModuleManager

class Module:
    def load_configuration(self):
        web_interface = ModuleManager.get('web_interface')
        if web_interface:
            web_interface.add_home_page('Private', '/private', 'Private zone')

    def home_page(self):
        return 'private'
