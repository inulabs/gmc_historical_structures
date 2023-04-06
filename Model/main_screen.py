from Model.base_model import BaseScreenModel


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self):
        self._id = 0
        self._name = ""
        self._description = ""
        self._type = ""
        self._built_date = ""
        self._removal_date = ""
        self._latitude = None
        self._longitude = None
        self._division = ""
        self._section = ""
        self._elevation = None
        self._location = ""
        self._images = []
        self._structure_list = []
        self._observers = []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def type(self):
        return self._type

    @property
    def built_date(self):
        return self._built_date

    @property
    def removal_date(self):
        return self._removal_date

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def section(self):
        return self._section

    @property
    def division(self):
        return self._division

    @property
    def elevation(self):
        return self._elevation

    @property
    def location(self):
        return self._location

    @property
    def structure_list(self):
        return self._structure_list

    @property
    def images(self):
        return self._images

    @id.setter
    def id(self, value):
        self._id = value
        self.notify_observers()

    @name.setter
    def name(self, value):
        self._name = value
        self.notify_observers()


    @description.setter
    def description(self, value):
        self._description = value
        self.notify_observers()

    @type.setter
    def type(self, value):
        self._type = value
        self.notify_observers()

    @built_date.setter
    def built_date(self, value):
        self._built_date = value
        self.notify_observers()

    @removal_date.setter
    def removal_date(self, value):
        self._removal_date = value
        self.notify_observers()

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
        self.notify_observers()

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
        self.notify_observers()

    @section.setter
    def section(self, value):
        self._section = value
        self.notify_observers()

    @division.setter
    def division(self, value):
        self._division = value
        self.notify_observers()

    @elevation.setter
    def elevation(self, value):
        self._elevation = value
        self.notify_observers()

    @location.setter
    def location(self, value):
        self._location = value
        self.notify_observers()
    @images.setter
    def images(self, value: list):
        self._images = value or []
        self.notify_observers()

    @structure_list.setter
    def structure_list(self, value: list):
        self._structure_list = value or []
        self.notify_observers()
    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()