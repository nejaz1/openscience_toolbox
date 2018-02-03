function varargout = read_project
%% Description
%   Load project settings (specified by project file)
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

% get project file name (needs to be set by user using ost.project_file)
fname = ost.project_file;

if exist(fname,'file')
    dat         = loadjson(fname);
    varargout   = {dat};
else
    disp('project file name needs to be provided using ost.project_file');
end;
