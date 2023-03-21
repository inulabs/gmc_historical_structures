from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout


class ContentNavigationDrawer(BoxLayout):
    pass


class DesktopScreenView(MDScreen):

    def __init__(self, set_type, **kw):
        super().__init__(**kw)
        menu_items = [
            {
                "text": "shelter",
                "viewclass": "OneLineListItem",
                "on_release": lambda: set_type("shelter")
            },
            {
                "text": "lodge",
                "viewclass": "OneLineListItem",
                "on_release": lambda: set_type("lodge")
            },
            {
                "text": "tenting area",
                "viewclass": "OneLineListItem",
                "on_release": lambda: set_type("tenting area")
            }

        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.type,
            items=menu_items,
            width_mult=4,
        )

    def on_model_change(self, model):
        self.ids.id.text = str(model.id or "")
        self.ids.name.text = str(model.name or "")
        self.ids.description.text = str(model.description or "")
        self.ids.type.text = str(model.type or "Select").lower()
        self.ids.built_date.text = str(model.built_date or "")
        self.ids.removal_date.text = str(model.removal_date or "")
        self.ids.latitude.text = str(model.latitude or 0)
        self.ids.longitude.text = str(model.longitude or 0)
        self.ids.section.text = str(model.section or "")
        self.ids.division.text = str(model.division or "")
        self.ids.elevation.text = str(model.elevation or "")
        self.ids.location.text = str(model.location or "")
