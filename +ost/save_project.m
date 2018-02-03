function save_project(ds_updated)
%% Description
%   Save project data (not to be called by user)
%   INPUT:
%       ds_updated:           structure containing updated data for project
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

opt.FileName = ost.project_file;        % get project file
savejson('',ds_updated,opt);
