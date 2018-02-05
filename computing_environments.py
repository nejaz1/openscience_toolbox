# Main OpenScience Toolbox Class for the Matlab Engine wrapper
#
# Created:
# Feb 2, 2018: Naveed Ejaz

# Load required python libraries

class computing_environments:
    handle_matlab     = []          # point to matlab engine

    # constructor
    def __init__(self):
        """Constructor purposely left empty"""

    # initialize experiment with defaults provided in yaml file
    def init_matlabengine(self):
        # open matlab engine if it has not been instantiated
        if self.handle_matlab == []:
            import matlab.engine
            self.handle_matlab = matlab.engine.start_matlab()

    # execute the command through the appropriate platform
    def execute(self,env,cmd):
        # if environment is matlab (check if we have a handle, then execute)
        if env == 'matlab':
            self.init_matlabengine()
            cmd         = cmd[0:-1]
            handle_env  = self.env_matlab

        # build and execute command string
        cmdstr      = "handle_env." + cmd + ", nargout=0)"
        exec(cmdstr)
