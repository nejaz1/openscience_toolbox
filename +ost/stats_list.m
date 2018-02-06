function stats_list
%% Description
%   Print list of stats being monitered inside container
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

% get handle to python module object
obj = ost.load();
obj.stats_list()
