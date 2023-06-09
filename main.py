"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
from kivy import Config
from kivy.core.window import Window
from kivy.metrics import dp, sp



from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.tab import MDTabsBase

from View.screens import screens


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''




class gmc_historical_structures(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = MDScreenManager()
        self.structure_types = ['shelter', 'lodge', 'tenting area']

    def build(self) -> MDScreenManager:
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def on_start(self, **kwargs):
        Window.maximize()


    def move_to(self, velocity):
        print(velocity)

    def set_name(self, focus, value):

        for property, value in vars(self).items():
            print(property, ":", value)

gmc_historical_structures().run()
