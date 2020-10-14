# Installation instructions
#   1. Change the name, terminal command, python script name, and method to run in this file
#   2. Run the following command in terminal:
#       The location is the folder with the setup.py file. Notice the . at the end of the path location.
#       pip install -e /Projects/empty-starter/.
#   3. By default the executable is located at: /Users/[username]/Library/Python/2.7/bin
#       You can run the script by calling its exact location like this:
#       /Users/[username]/Library/Python/2.7/bin/hello-world
#   4. If you add the executable installation folder to your bash profile you can run executables with simple commands
#       Add the following to your bash profile:
#       export PATH="/Users/[username]/Library/Python/2.7/bin:$PATH"
#       Now you can run hello-world as a command in bash

import setuptools
setuptools.setup(
    name='hello-world',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            # '[terminal command]=[python script name]:[method in script to run]'
            'hello-world=app:run'
        ]
    }
)
