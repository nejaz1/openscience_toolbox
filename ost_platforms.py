# Main OpenScience Toolbox Class for the Matlab Engine wrapper
#
# Created:
# Feb 2, 2018: Naveed Ejaz

# Load required python libraries
import matlab.engine

class ost_platforms:
    env_matlab     = []          # point to matlab engine

    # constructor
    def __init__(self):
        """Constructor purposely left empty"""

    # initialize experiment with defaults provided in yaml file
    def init_matlabengine(self):
        # open matlab engine if it has not been instantiated
        if self.env_matlab == []:
            self.env_matlab = matlab.engine.start_matlab()

    # execute the command through the appropriate platform
    def execute(self,env,cmd):
        # if environment is matlab (check if we have a handle, then execute)
        if env == 'matlab':
            self.init_matlabengine()
            cmd     = cmd[0:-1]

        # build and execute command string
        platform    = self.env_matlab
        cmdstr      = "platform." + cmd + ", nargout=0)"
        exec(cmdstr)
