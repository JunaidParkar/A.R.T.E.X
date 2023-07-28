import os
import subprocess

def set_permanent_environment_variable(variable_name, variable_value):
    # Set the environment variable for the current session
    os.environ[variable_name] = variable_value

    # Set the environment variable permanently using setx command (requires admin privileges)
    try:
        subprocess.run(['setx', variable_name, variable_value], check=True)
        print(f"Environment variable {variable_name} set permanently with value: {variable_value}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while setting the environment variable: {e}")

if __name__ == "__main__":
    variable_name = 'hi'
    variable_value = 'hooo'

    set_permanent_environment_variable(variable_name, variable_value)
