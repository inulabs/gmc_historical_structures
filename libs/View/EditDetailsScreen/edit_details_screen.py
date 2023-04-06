from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.EditDetailsScreen.components import (
    MobileScreenView,
    TabletScreenView,
    DesktopScreenView,
)
from View.base_screen import BaseScreenView


class EditDetailsScreenView(MDResponsiveLayout, BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileScreenView()
        self.tablet_view = TabletScreenView()
        self.desktop_view = DesktopScreenView()

    def model_is_changed(self, model) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.ids.id.text = str(model.id)
        self.ids.name.text = str(model.name)
        self.ids.description.text = str(model.description)
        self.ids.type.text = str(model.type)
        self.ids.built_date.text = str(model.built_date)
        self.ids.removal_date.text = str(model.removal_date)
        self.ids.latitude.text = str(model.latitude)
        self.ids.longitude.text = str(model.longitude)
        self.ids.section.text = str(model.section)
        self.ids.division.text = str(model.division)

