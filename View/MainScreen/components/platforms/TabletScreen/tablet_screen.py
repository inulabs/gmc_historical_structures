import os

from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
import shutil

from kivymd.uix.textfield import MDTextField




class ImageBox(MDBoxLayout):

    update_image_title = ObjectProperty()
    delete_image = ObjectProperty()


def partial(func, param):
    def inner(*args, **kwargs):
        return func(param)

    return inner


class ContentNavigationDrawer(BoxLayout):
    pass


class TabletScreenView(MDScreen):

    def __init__(self, set_type, set_section, get_sections, add_image, delete_image, update_image, nav_to_structure, **kw):
        super().__init__(**kw)
        self.nav_to_structure = nav_to_structure
        self.update_image = update_image
        self.delete_image = delete_image
        self.add_image = add_image
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
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
        sections = get_sections()
        section_items = [{
            "text": s.name,
            "viewclass": "OneLineListItem",
            "on_release": partial(set_section, s.name)
        } for s in sections]

        self.sections_menu = MDDropdownMenu(
            caller=self.ids.section,
            items=section_items,
            width_mult=4,
        )

    def on_model_change(self, model):
        self.ids.top_bar.title = "Structures: " + str(model.id or "")
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
        pix = [i for i in self.ids.photos.children]
        print(pix)
        for pic in pix:
            self.ids.photos.remove_widget(pic)
        for i in model.images:
            if i is not None:
                iBox = ImageBox()
                iBox.image = i
                iBox.ids.image.source = i.path or ""
                iBox.ids.title.text = i.title or ""
                iBox.ids.description.text = i.description or ""
                iBox.ids.caption.text = i.caption or ""
                iBox.ids.image_date.text = i.date or ""
                iBox.set_image_title = self.update_image_field("title", i)
                iBox.set_image_description = self.update_image_field("description", i)
                iBox.set_image_caption = self.update_image_field("caption", i)
                iBox.set_image_date = self.update_image_field("date", i)
                iBox.delete_image = self.remove_image(i)
                self.ids.photos.add_widget(iBox)

    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        root_dir = os.path.dirname(os.path.abspath("main.py"))
        print(root_dir)
        folder = os.path.join(root_dir, "assets", "images", "structures", self.ids.id.text)
        print(folder)
        dst = os.path.join("assets", "images", "structures", self.ids.id.text, os.path.basename(path))
        print(dst)
        os.makedirs(folder, exist_ok=True)
        shutil.copyfile(path, dst)

        self.add_image(self.ids.id.text, dst)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


    def remove_image(self, image):
        def delete():
            foo = image.as_dict()
            self.delete_image(foo["id"])
        return delete
    def update_image_field(self, field, image):
        def update(focus, value):
            print(value)
            print(type(image))
            if not focus:
                foo = image.as_dict()
                foo[field] = value
                self.update_image(foo)

        return update


