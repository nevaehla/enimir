import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('config.ini')

# Get the value of the 'database' option from the 'DEFAULT' section
database = config['DEFAULT']['database']

# Print the value of the 'database' option
print(database)
