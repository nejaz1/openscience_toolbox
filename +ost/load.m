function varargout = load(fname)
%% Description
%   Get/set full path to the container file
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

% get handle to python module object
obj = ost.get_py_ost_handle();

%% get last used container/container with specified name provided
if nargin==0
    fname = getenv('OST_CONTAINER');
elseif nargin==1
    setenv('OST_CONTAINER',fname);
end;

% return loaded container
if isempty(fname)
	fprintf('[No valid container file in memory] please provide location of container file\n');
	if nargout==1
		varargout = {[]};
	end;
else
	obj.load(fname);
	if nargout==1
		varargout = {obj};
	end;
end;


