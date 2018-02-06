function print_summary
%% Description
%   Print summary of information held inside container
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

% get handle to python module object
obj = ost.load();
obj.print_summary()
