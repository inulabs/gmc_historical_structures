from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout

class ContentNavigationDrawer(BoxLayout):
    pass

class DesktopScreenView(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
  
    def on_model_change(self, model):
        self.ids.id.text = str(model.id)
        self.ids.name.text = model.name
        self.ids.description.text = model.description
        self.ids.type.text = model.type
        self.ids.built_date.text = model.built_date
        self.ids.removal_date.text = model.removal_date
        self.ids.latitude.text = str(model.latitude)
        self.ids.longitude.text = str(model.longitude)
        self.ids.section.text = model.section
        self.ids.division.text = model.division
