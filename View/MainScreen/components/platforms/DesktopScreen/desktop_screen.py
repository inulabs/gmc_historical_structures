from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout

class ContentNavigationDrawer(BoxLayout):
    pass

class DesktopScreenView(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
  
    def on_model_change(self, model):
        self.ids.id.text = str(model.id or "")
        self.ids.name.text = str(model.name or "")
        self.ids.description.text = str(model.description or "")
        self.ids.type.text = str(model.type or "")
        self.ids.built_date.text = str(model.built_date or "")
        self.ids.removal_date.text = str(model.removal_date or "")
        self.ids.latitude.text = str(model.latitude or 0)
        self.ids.longitude.text = str(model.longitude or 0)
        self.ids.section.text = str(model.section or "")
        self.ids.division.text = str(model.division or "")
