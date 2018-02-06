function save_project(ds_updated)
%% Description
%   Save project data (not to be called by user)
%   INPUT:
%       ds_updated:           structure containing updated data for project
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

opt.FileName = getenv('OST_CONTAINER');        % get project file
savejson('',ds_updated,opt);
