from keyed_network.command import Command

class Watermark:
    def __init__(self,transformation_commands = []):
        self.transformation_commands = transformation_commands

    def add(self, command: Command):
         self.transformation_commands.append(command)
    
    def get_info(self):
        return {
            "type": "key",
            "info": {
                "transformations": self.transformation_commands
            }
        }