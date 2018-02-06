function varargout = get_py_ost_handle()
%% Description
%   Return an object of the module/class ost from the python library
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)


pyost   = py.importlib.import_module('ost');
obj     = pyost.ost();

if nargout==1
    varargout = {obj};
elseif nargout==2
    varargout = {obj,pyost};
end;
