function figure_list
%% Description
%   Print list of figures being monitered inside container
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

% get handle to python module object
obj = ost.load();
obj.figure_list()
