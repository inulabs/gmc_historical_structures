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
        self.desktop_view = DesktopScreenView()
        self.model.add_observer(self)

    controller = ObjectProperty()
    model = ObjectProperty()


    def new_record(self):
        print ("ADDING NEW STRUCTURE")
        self.controller.new_record()

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

    def set_type(self, focus, value):
        print("set_type", "view", value)
        if not focus:
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

    def set_section(self, focus, value):
        print("set_section", "view", value)

        if not focus:
            self.controller.set_section(value)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.desktop_view.on_model_change(self.model)
        self.tablet_view.on_model_change(self.model)
        self.mobile_view.on_model_change(self.model)

