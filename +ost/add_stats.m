function add_stats(name)
%% Description
%   Add a new statistics to the project container
%   INPUT:
%       name:           name of the stats (e.g. t-test for fig2b)
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

cmd = ost.get_last_command; % log last command

% get container file name (needs to be set by user using ost.project_file)
ds 	= loadjson(getenv('OST_CONTAINER'));

% add figure details
ds.stats.(name).environment 	= 'matlab';
ds.stats.(name).cmd           	= cmd;
ds.stats.(name).datetime      	= datestr(now);         % tag with current time

% update stats number
ds.project.num_stats          	= ds.project.num_stats + 1;

% save updated data
ost.save_project(ds);
