
class GameController():
    def __init__(self) -> None:
        super().__init__()

        self.role = ['black', 'white', 'observer']
        self.num_connected_user = 0

    def allocate_role(self):
        if self.num_connected_user < 2:
            result = self.role[self.num_connected_user]
            self.num_connected_user += 1
            return result
        else:
            return self.role[-1]