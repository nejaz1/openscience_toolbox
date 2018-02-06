# Main OpenScience Toolbox Class
#
# Created:
# Feb 2, 2018: Naveed Ejaz

# Load required python libraries
import json
import os
from datetime import datetime
from computing_environments import computing_environments


class ost:
    proj_file     = []          # location of the ost project file
    ds            = []          # contents of the project 

    # constructor
    def __init__(self):
        """Constructor purposely left empty"""
        self.env = computing_environments()

    # initialize project repository 
    def init(self, name):
        now     = datetime.now()
        dstr    = now.strftime("%d-%b-%Y %X")
        d       = {'project': {'name': name, 'num_figures': 0, 'num_stats': 0, 'datetime': dstr}}

        fname   = os.getcwd() + '/' + name + '.ost'

        # write default data
        with open(fname, 'w') as f:
            json.dump(d, f)
        f.close()

        # load project back in
        self.load(fname)

    # initialize experiment with defaults provided in yaml file
    def load(self, filepath):
        # load the contents of the project (structure is a json file)
        fid                 = open(filepath, 'r')
        self.ds             = json.load(fid)
        fid.close()

        # save file path location
        self.proj_file  = filepath

    # initialize data manager and provide format to expect data in
    def print_project_details(self):
        self.load(self.proj_file)

        print "Project name\t: " + str(self.ds['project']['name'])
        print "Date created\t: " + str(self.ds['project']['datetime'])
        print "Total figures\t: " + str(self.ds['project']['num_figures'])
        print "Total stats\t: " + str(self.ds['project']['num_stats'])

    # plot figure with given name
    def plot_figure(self, name):
        self.load(self.proj_file)

        env = self.ds['figures'][name]['environment']
        cmd = self.ds['figures'][name]['cmd']

        self.env.execute(env,cmd)


