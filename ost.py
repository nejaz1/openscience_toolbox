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
    container     = []          # location of the ost project file
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
        self.container  = filepath

    # return the contents of the container (useful for processing in other environments)
    def get_container(self):
        self.load(self.container)
        return self.ds

    # print current state of project container (overview only)
    def print_summary(self):
        self.load(self.container)

        print "Project name\t: " + str(self.ds['project']['name'])
        print "Date created\t: " + str(self.ds['project']['datetime'])
        print "Total figures\t: " + str(self.ds['project']['num_figures'])
        print "Total stats\t: " + str(self.ds['project']['num_stats']) + "\n"

    # print list of figures in project container
    def figure_list(self):
        self.load(self.container)

        # get nested dictionary for figures
        #   - list all available figures
        if self.ds['project']['num_figures']>0:
            f   = self.ds['figures'].keys()

            for i in range(len(f)):
                s   = str(f[i])                 # get ith figure name
                print "Figure name\t: " + s
                print "Date created\t: " + self.ds['figures'][s]['datetime']
                print "Environment\t: " + self.ds['figures'][s]['environment']
                print "Command\t\t: " + self.ds['figures'][s]['cmd'] + "\n"
        else:
            print "No figures added to container"

    # print list of stats in project container
    def stats_list(self):
        self.load(self.container)

        # get nested dictionary for stats
        #   - list all available stats
        if self.ds['project']['num_stats']>0:
            f   = self.ds['stats'].keys()

            for i in range(len(f)):
                s   = str(f[i])                 # get ith stats name
                print "Stats name\t: " + s
                print "Date created\t: " + self.ds['stats'][s]['datetime']
                print "Environment\t: " + self.ds['stats'][s]['environment']
                print "Command\t\t: " + self.ds['stats'][s]['cmd'] + "\n"
        else:
            print "No stats added to container"            

    # generate figure with given id
    def make_figure(self, name):
        self.load(self.container)

        env = self.ds['figures'][name]['environment']
        cmd = self.ds['figures'][name]['cmd']

        self.env.execute(env,cmd)

    # generate stats with given id
    def make_stats(self, name):
        self.load(self.container)

        env = self.ds['stats'][name]['environment']
        cmd = self.ds['stats'][name]['cmd']

        self.env.execute(env,cmd)        
