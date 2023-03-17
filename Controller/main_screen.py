
from View.MainScreen.main_screen import MainScreenView


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

    def get_view(self) -> MainScreenView:
        return self.view

    def get_screen(self) -> MainScreenView:
        return self.view

    def set_id(self, value):
        """
        When finished editing the data entry field for `ID`, the controller
        changes the `id` property of the model.
        """

        self.model.id = value

    def set_name(self, value):
        """
        When finished editing the data entry field for `name`, the controller
        changes the `bame` property of the model.
        """
        print("CONTROLLER: set_name")
        self.model.name = value

    def set_description(self, value):
        """
        When finished editing the data entry field for `Description`, the controller
        changes the `description` property of the model.
        """

        self.model.description = value

    def set_type(self, value):
        """
        When finished editing the data entry field for `Type`, the controller
        changes the `type` property of the model.
        """

        self.model.type = value

    def set_built_date(self, value):
        """
        When finished editing the data entry field for `Build Date`, the controller
        changes the `build_date` property of the model.
        """

        self.model.build_date = value

    def set_removal_date(self, value):
        """
        When finished editing the data entry field for `Removal Date`, the controller
        changes the `removal_date` property of the model.
        """

        self.model.removal_date = value

    def set_latitude(self, value):
        """
        When finished editing the data entry field for `Latitude`, the controller
        changes the `latitude` property of the model.
        """

        self.model.latitude = value

    def set_longitude(self, value):
        """
        When finished editing the data entry field for `Longitude`, the controller
        changes the `longitude` property of the model.
        """

        self.model.longitude = value

    def set_division(self, value):
        """
        When finished editing the data entry field for `Division`, the controller
        changes the `division` property of the model.
        """

        self.model.division = value

    def set_section(self, value):
        """
        When finished editing the data entry field for `Section`, the controller
        changes the `section` property of the model.
        """

        self.model.section = value

