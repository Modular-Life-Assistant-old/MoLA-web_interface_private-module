from core import ModuleManager

from modules.web_interface_private.pages import home

class Module:
    def load_configuration(self):
        web_interface = ModuleManager.get('web_interface')
        if web_interface:
            web_interface.add_home_page('Private', '/private', 'Private zone')

            web_interface.register_blueprint(home.app)
