import sys
from app.commands import Command

# Mock function to simulate plugin discovery
def get_available_plugins():
    # This should be replaced with the actual logic to discover plugins
    return ["Add", "Divide", "Multiply", "Subtract", "Email", "Exit", "Goodbye", "Greet", "Menu"]

class MenuCommand(Command):
    def execute(self):
        print('Menu')
        plugins = get_available_plugins()
        print('Available plugins:')
        for plugin in plugins:
            print(f' - {plugin}')

# Example usage
if __name__ == "__main__":
    command = MenuCommand()
    command.execute()
