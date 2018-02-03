# Main OpenScience Toolbox Class
#
# Created:
# Feb 2, 2018: Naveed Ejaz

# Load required python libraries
import json
from OST_MatlabEngine import OST_MatlabEngine


class OST:
    proj_file_loc = []          # location of the ost project file
    ds            = []          # contents of the project 
    matlabengine  = []          # handle to matlab engine

    # constructor
    def __init__(self):
        """Constructor purposely left empty"""
        self.matlabengine = OST_MatlabEngine()

    # initialize experiment with defaults provided in yaml file
    def init(self, filepath):
        # load the contents of the project (structure is a json file)
        fid                 = open(filepath, 'r')
        self.ds             = json.load(fid)
        fid.close()

        # save file path location
        self.proj_file_loc  = filepath

    # initialize matlab engine
    def init_matlabengine(self):
        self.matlabengine.init()

    # initialize data manager and provide format to expect data in
    def print_project_details(self):
        print "Project name\t: " + str(self.ds['project']['name'])
        print "Total figures\t: " + str(self.ds['project']['num_figures'])
        print "Total stats\t: " + str(self.ds['project']['num_stats'])

    # plot figure with given name
    def plot_figure(self, name):
        env = self.ds['figures'][name]['environment']
        cmd = self.ds['figures'][name]['cmd']

        if env == 'matlab':
            self.init_matlabengine()
            self.matlabengine.execute(cmd)

