function varargout = project_file(fname)
%% Description
%   Get/set full path to file which specifies the project settings
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

%% 0. Figure out installation directory
installDir  = getenv('OST_INSTALL_DIR');
if isempty(installDir)
    pth         = which('ost.project_file');     % get install directory
    d           = fileparts(pth);
    setenv('OST_INSTALL_DIR',d);
end;

%% 0. Get/Set project file name
if nargin==0
    f = getenv('OST_PROJECT_FILE');
    if nargout == 1
        varargout = {f};
    elseif nargout == 2
        varargout = {f,installDir};
    end;
elseif nargin==1
    setenv('OST_PROJECT_FILE',fname);
end;

