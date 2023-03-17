
from View.MapScreen.map_screen import MapScreenView


class MapScreenController:
    """
    The `MapScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.map_screen.MapScreenModel
        self.view = MapScreenView(controller=self, model=self.model)

    def get_view(self) -> MapScreenView:
        return self.view
