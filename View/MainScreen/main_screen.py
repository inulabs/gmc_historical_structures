from kivy.uix.modalview import ModalView
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from View.MainScreen.components import (
    MobileScreenView,
    TabletScreenView,
    DesktopScreenView,
)
from View.base_screen import BaseScreenView
from kivy.properties import ObjectProperty
from Utility.observer import Observer


class Tab(MDFloatLayout, MDTabsBase):
    pass


class MainScreenView(MDResponsiveLayout, BaseScreenView, Observer):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.mobile_view = MobileScreenView()
        self.tablet_view = TabletScreenView()
        self.desktop_view = DesktopScreenView(self.set_type, self.set_section, self.get_sections, self.add_image, self.delete_image, self.update_image, self.nav_to_strucure)
        self.model.add_observer(self)


    controller = ObjectProperty()
    model = ObjectProperty()

    def update_image(self, image):
        self.controller.update_image(image)

    def add_image(self, id, path):
        self.controller.add_structure_image(id, path)

    def get_sections(self):
        return self.controller.get_sections()

    def delete_record(self):
        self.controller.delete_record()

    def delete_image(self, id):
        self.controller.delete_image(id)

    def new_record(self):
        print ("ADDING NEW STRUCTURE")
        self.controller.new_record()



    def nav_to_strucure(self, sid):
        self.controller.nav_to_structure(sid)

    def skip(self, direction):
        self.controller.skip(direction)

    def set_id(self, focus, value):
        if not focus:
            self.controller.set_id(value)

    def set_name(self, focus, value):
        print("set_name", "view", value)
        if not focus:
            self.controller.set_name(value)

    def set_description(self, focus, value):
        print("set_description", "view", value)

        if not focus:
            self.controller.set_description(value)

    def set_type(self, value):
        print("set_type", "view", value)
        self.controller.set_type(value)

    def set_built_date(self, focus, value):
        print("set_built_date", "view", value)

        if not focus:
            self.controller.set_built_date(value)

    def set_removal_date(self, focus, value):
        print("set_removal_date", "view", value)
        if not focus:
            self.controller.set_removal_date(value)

    def set_latitude(self, focus, value):
        print("set_latitude", "view", value)
        if not focus:
            self.controller.set_latitude(value)

    def set_longitude(self, focus, value):
        print("set_longitude", "view", value)

        if not focus:
            self.controller.set_longitude(value)

    def set_division(self, focus, value):
        print("set_division", "view", value)

        if not focus:
            self.controller.set_division(value)

    def set_section(self, value):
        print("VIEW: SET SECTION TO: ", value)
        self.controller.set_section(value)

    def set_elevation(self, focus, value):
        print("VIEW: SET ELEVATION TO:", value)

        if not focus:
            self.controller.set_elevation(value)

    def set_location(self, focus, value):
        print("set_location", "view", value)

        if not focus:
            self.controller.set_location(value)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.desktop_view.on_model_change(self.model)
        self.tablet_view.on_model_change(self.model)
        self.mobile_view.on_model_change(self.model)


