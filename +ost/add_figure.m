function add_figure(name)
%% Description
%   Add a new figure to the project settings
%   INPUT:
%       name:           name of the figure (e.g. fig2b)
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

cmd = ost.get_last_command; % log last command

% get project file name (needs to be set by user using ost.project_file)
ds = ost.read_project;

ds.figures.(name).environment   = 'matlab';
ds.figures.(name).cmd           = cmd;
ds.figures.(name).datetime      = datestr(now);         % tag with current time

% save updated data
ost.save_project(ds);
