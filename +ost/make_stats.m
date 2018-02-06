function make_stats(name)
%% Description
%   Use container information to make stats with the given name
%	INPUT:
%		name:		this is the id used to store the stats in the container
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

% get handle to python module object
obj = ost.load();

% get contents of the container
ds = struct(obj.get_container);

% if there is at least one stats in the container
if isfield(ds,'stats')
	allfig 	= struct(ds.figures);

	% look for the required figure
	if isfield(allstats,name)
		f = struct(allstats.(name));

		% get stats details
		env 		= char(f.environment);
		cmd 		= char(f.cmd);
		datetime 	= char(f.datetime);

		% check if environment is matlab, if yes then execute command string
		if strcmp(env,'matlab')
			run(cmd);
		end;
	end;
end;



