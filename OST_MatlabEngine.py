# Main OpenScience Toolbox Class for the Matlab Engine wrapper
#
# Created:
# Feb 2, 2018: Naveed Ejaz

# Load required python libraries
import matlab.engine

class OST_MatlabEngine:
    eng     = []          # point to matlab engine

    # constructor
    def __init__(self):
        """Constructor purposely left empty"""

    # initialize experiment with defaults provided in yaml file
    def init(self):
        # open matlab engine if it has not been instantiated
        if self.eng == []:
            self.eng = matlab.engine.start_matlab()

    # execute the command through the matlab engine
    def execute(self,cmd):
        eng     = self.eng
        cmdstr  = "eng." + cmd[0:-1] + ", nargout=0)"
        exec(cmdstr)
