
from View.MainScreen.main_screen import MainScreenView
from data_layer import structures, sections, images
from Utility.find_index import find_index
from data_layer.data_models.image import Image


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """
    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)
        self.structures = structures.fetch_all()
        self.currentIndex = 0
        self.model.id = self.structures[self.currentIndex].id
        self.model.name = self.structures[self.currentIndex].name
        self.model.description = self.structures[self.currentIndex].description
        self.model.type = self.structures[self.currentIndex].type
        self.model.built_date = self.structures[self.currentIndex].built_date
        self.model.removal_date = self.structures[self.currentIndex].removal_date
        self.model.latitude = self.structures[self.currentIndex].latitude
        self.model.longitude = self.structures[self.currentIndex].longitude
        self.model.division = self.structures[self.currentIndex].division
        self.model.section = self.structures[self.currentIndex].section
        self.model.structure_list = [(s.id, s.name) for s in self.structures]
        my_images = images.fetch_all_by_structure(self.model.id)
        self.model.images = my_images

    def build(self):
        self.view.build()

    def get_view(self) -> MainScreenView:
        return self.view

    def get_screen(self) -> MainScreenView:
        return self.view

    def get_sections(self):
        return sections.fetch_all()

    def delete_record(self):
        structures.delete_structure(self.model.id)
        self.structures = structures.fetch_all()
        if self.currentIndex > len(self.structures):
            self.currentIndex = 0
        self.model.id = self.structures[self.currentIndex].id
        self.model.name = self.structures[self.currentIndex].name
        self.model.description = self.structures[self.currentIndex].description
        self.model.type = self.structures[self.currentIndex].type
        self.model.built_date = self.structures[self.currentIndex].built_date
        self.model.removal_date = self.structures[self.currentIndex].removal_date
        self.model.latitude = self.structures[self.currentIndex].latitude
        self.model.longitude = self.structures[self.currentIndex].longitude
        self.model.division = self.structures[self.currentIndex].division
        self.model.section = self.structures[self.currentIndex].section
        my_images = images.fetch_all_by_structure(self.model.id)
        self.model.images = my_images
    def new_record(self):
        new_id = structures.add_structure()
        self.structures = structures.fetch_all()
        self.currentIndex = find_index("id", self.structures, new_id)
        self.model.id = self.structures[self.currentIndex].id
        self.model.name = self.structures[self.currentIndex].name
        self.model.description = self.structures[self.currentIndex].description
        self.model.type = self.structures[self.currentIndex].type
        self.model.built_date = self.structures[self.currentIndex].built_date
        self.model.removal_date = self.structures[self.currentIndex].removal_date
        self.model.latitude = self.structures[self.currentIndex].latitude
        self.model.longitude = self.structures[self.currentIndex].longitude
        self.model.division = self.structures[self.currentIndex].division
        self.model.section = self.structures[self.currentIndex].section
        my_images = images.fetch_all_by_structure(self.model.id)
        self.model.images = my_images

    def nav_to_structure(self, sid):
        print("SID: ", sid)
        self.currentIndex = next(i for i, s in enumerate(self.structures) if s.id == sid)
        self.model.id = self.structures[self.currentIndex].id
        self.model.name = self.structures[self.currentIndex].name
        self.model.description = self.structures[self.currentIndex].description
        self.model.type = self.structures[self.currentIndex].type
        self.model.built_date = self.structures[self.currentIndex].built_date
        self.model.removal_date = self.structures[self.currentIndex].removal_date
        self.model.latitude = self.structures[self.currentIndex].latitude
        self.model.longitude = self.structures[self.currentIndex].longitude
        self.model.division = self.structures[self.currentIndex].division
        self.model.section = self.structures[self.currentIndex].section
        my_images = images.fetch_all_by_structure(self.structures[self.currentIndex].id)
        self.model.images = my_images

    def skip(self, direction):
        print("Direction", direction)

        if direction > 0:
            self.currentIndex += 1
            if self.currentIndex >= len(self.structures):
                self.currentIndex = 0
        else:
            self.currentIndex -= 1
            if self.currentIndex < 0:
                self.currentIndex = len(self.structures) - 1
        self.model.id = self.structures[self.currentIndex].id
        self.model.name = self.structures[self.currentIndex].name
        self.model.description = self.structures[self.currentIndex].description
        self.model.type = self.structures[self.currentIndex].type
        self.model.built_date = self.structures[self.currentIndex].built_date
        self.model.removal_date = self.structures[self.currentIndex].removal_date
        self.model.latitude = self.structures[self.currentIndex].latitude
        self.model.longitude = self.structures[self.currentIndex].longitude
        self.model.division = self.structures[self.currentIndex].division
        self.model.section = self.structures[self.currentIndex].section
        my_images = images.fetch_all_by_structure(self.structures[self.currentIndex].id)
        self.model.images = my_images


        print("New Model", self.model)


    def set_id(self, value):
        """
        When finished editing the data entry field for `ID`, the controller
        changes the `id` property of the model.
        """
        self.model.id = value

    def set_name(self, value):
        """
        When finished editing the data entry field for `name`, the controller
        changes the `name` property of the model.
        """
        print("CONTROLLER: SET NAME TO: ", value)
        self.model.name = value
        structures.update_structure(self.model)

    def set_description(self, value):
        """
        When finished editing the data entry field for `Description`, the controller
        changes the `description` property of the model.
        """
        print("CONTROLLER: SET DESCRIPTION TO: ", value)
        self.model.description = value
        structures.update_structure(self.model)


    def set_type(self, value):
        """
        When finished editing the data entry field for `Type`, the controller
        changes the `type` property of the model.
        """
        print("CONTROLLER: SET TYPE TO: ", value)
        self.model.type = value
        structures.update_structure(self.model)


    def set_built_date(self, value):
        """
        When finished editing the data entry field for `Build Date`, the controller
        changes the `build_date` property of the model.
        """
        print("CONTROLLER: SET BUILT DATE TO: ", value)
        self.model.build_date = value
        structures.update_structure(self.model)


    def set_removal_date(self, value):
        """
        When finished editing the data entry field for `Removal Date`, the controller
        changes the `removal_date` property of the model.
        """
        print("CONTROLLER: SET REMOVAL DATE TO: ", value)
        self.model.removal_date = value
        structures.update_structure(self.model)


    def set_latitude(self, value):
        """
        When finished editing the data entry field for `Latitude`, the controller
        changes the `latitude` property of the model.
        """
        print("CONTROLLER: SET LATITUDE TO: ", value)
        self.model.latitude = value
        structures.update_structure(self.model)


    def set_longitude(self, value):
        """
        When finished editing the data entry field for `Longitude`, the controller
        changes the `longitude` property of the model.
        """
        print("CONTROLLER: SET LONGITUDE TO: ", value)
        self.model.longitude = value
        structures.update_structure(self.model)


    def set_division(self, value):
        """
        When finished editing the data entry field for `Division`, the controller
        changes the `division` property of the model.
        """
        print("CONTROLLER: SET DIVISION TO: ", value)
        self.model.division = value
        structures.update_structure(self.model)


    def set_section(self, value):
        """
        When finished editing the data entry field for `Section`, the controller
        changes the `section` property of the model.
        """
        print("CONTROLLER: SET SECTION TO: ", value)
        self.model.section = value
        structures.update_structure(self.model)

    def set_location(self, value):
        """
        When finished editing the data entry field for `Location`, the controller
        changes the `location` property of the model.
        """
        print("CONTROLLER: SET LOCATION TO: ", value)
        self.model.location = value
        structures.update_structure(self.model)

    def set_elevation(self, value):
        """
        When finished editing the data entry field for `Elevation`, the controller
        changes the `elevation` property of the model.
        """
        print("CONTROLLER: SET ELEVATION TO: ", value)
        self.model.elevation = value
        structures.update_structure(self.model)

    def set_images(self, value):
        """
        When finished editing the data entry field for `Images`, the controller
        changes the `images` property of the model.
        """
        print("CONTROLLER: SET IMAGES TO: ", value)
        self.model.images = value
        images.update_structure_image(self.model)

    def add_structure_image(self, id, file):
        print("CONTROLLER: ADD STRUCTURE IMAGE TO: ", id, file)
        images.add_structure_image(id, file)
        self.model.images = images.fetch_all_by_structure(id)

    def delete_image(self, id):
        print("CONTROLLER: DELETE IMAGE: ", id)
        images.delete_image(id)
        self.model.images = images.fetch_all_by_structure(self.model.id)

    def update_image(self, image):
        print("CONTROLLER: UPDATE STRUCTURE IMAGE TO: ", image)
        images.update_image(image)
        my_images = images.fetch_all_by_structure(self.model.id)
        print(my_images)
        self.model.images = my_images


