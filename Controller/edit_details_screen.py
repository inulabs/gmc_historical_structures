
from View.EditDetailsScreen.edit_details_screen import EditDetailsScreenView


class EditDetailsScreenController:
    """
    The `EditDetailsScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.edit_details_screen.EditDetailsScreenModel
        self.view = EditDetailsScreenView(controller=self, model=self.model)

    def get_view(self) -> EditDetailsScreenView:
        return self.view
