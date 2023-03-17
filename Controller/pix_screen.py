
from View.PixScreen.pix_screen import PixScreenView


class PixScreenController:
    """
    The `PixScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.pix_screen.PixScreenModel
        self.view = PixScreenView(controller=self, model=self.model)

    def get_view(self) -> PixScreenView:
        return self.view
