# Opencv Image Manipulation

Useful image manipulation techniques using OpenCV with Python


## Installation
1. Install virtual env wrapper using these commands:
    - `pip install virtualenvwrapper`

    - Add three lines to your shell startup file (.bashrc, .profile, etc.) to set the location where the virtual environments should live, the location of your       development project directories, and the location of the script installed with this package:
    ```
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh
    ```
    - After editing it, reload the startup file (e.g., run source ~/.bashrc).
   
2. Make a Virtual environment: `mkvirtualenv <virtual_env_name> --python=3.8.5` Use python version 3.7 and above.

3. Activate Virtual Environment: `workon <virtual_en_name>`

4. Install requirements: `pip install -r requirements.txt`

NB: Make sure that your pip version is up-to-date (19.3 is the minimum supported version): pip install --upgrade pip. Check version with pip -V.
