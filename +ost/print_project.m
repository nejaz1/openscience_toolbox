function print_project
%% Description
%   Print project settings (specified by project file)
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

% get project file name (needs to be set by user using ost.project_file)
ds = ost.read_project;

% display project settings
fprintf('Project name\t: %s\n',ds.project.name);
fprintf('Total figures\t: %d\n',ds.project.num_figures);
fprintf('Total stats\t: %d\n',ds.project.num_stats);