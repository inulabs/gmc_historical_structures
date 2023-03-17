# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.map_screen import MapScreenModel
from Controller.map_screen import MapScreenController
from Model.edit_details_screen import EditDetailsScreenModel
from Controller.edit_details_screen import EditDetailsScreenController
from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.profile_screen import ProfileScreenModel
from Controller.profile_screen import ProfileScreenController
from Model.pix_screen import PixScreenModel
from Controller.pix_screen import PixScreenController

screens = {
    # "map screen": {
    #     "model": MapScreenModel,
    #     "controller": MapScreenController,
    # },
    #
    # "edit details screen": {
    #     "model": EditDetailsScreenModel,
    #     "controller": EditDetailsScreenController,
    # },

    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    }

    # "profile screen": {
    #     "model": ProfileScreenModel,
    #     "controller": ProfileScreenController,
    # },
    #
    # "pix screen": {
    #     "model": PixScreenModel,
    #     "controller": PixScreenController,
    # },
}