import logging
import sys
import os  # Import the os module
from app.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock function to simulate plugin discovery
def get_available_plugins():
    # This should be replaced with the actual logic to discover plugins
    return ["Add", "Divide", "Multiply", "Subtract", "Email", "Exit", "Goodbye", "Greet", "Menu"]

class MenuCommand(Command):
    def execute(self):
        logging.info('Executing MenuCommand')
        print('Menu')
        plugins = get_available_plugins()
        logging.info(f'Available plugins: {", ".join(plugins)}')
        print('Available plugins:')
        for plugin in plugins:
            print(f' - {plugin}')

# Example usage
if __name__ == "__main__":
    logging.info('Starting the application')

    # Example of using environment variables
    api_key = os.getenv('API_KEY')
    if api_key:
        logging.info('API Key loaded successfully.')
    else:
        logging.error('API Key is missing.')

    command = MenuCommand()
    command.execute()
