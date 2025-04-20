from cvbot.communication.controller import Controller

class EasyDriveController:
    
    def __init__(self, control: Controller):
        self.control = control
        self.motor_configuration = ["M2", "M1", "M3", "M4"]
        """Motor configuration in order Front-Left, Front-Right, Back-Right, Back-Left."""


    def straight(self, speed: int) -> None:
        """Drive straight with a given speed."""
        
        # Set all motors to the same speed.
        # L
        