function init(cname)
%% Description
%   Initialize a container in the given directory with name "cname"
%   INPUT:
%       cname:      name of the container e.g. myproject
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

% get handle to python module object
obj = ost.get_py_ost_handle();

% initialize container
obj.init(cname);

% set location of last container
fname   = fullfile(cd,sprintf('%s.ost',cname));
setenv('OST_CONTAINER',fname);

