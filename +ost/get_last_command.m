function varargout = get_last_command
%% Description
%   Gets the last command from the user command history
%
% Author
%   Naveed Ejaz (ejaz.naveed@gmail.com)

h = xmlread(fullfile(prefdir,'History.xml'));       % load user history
c = h.getElementsByTagName('command');              % get all commands
l = c.getLength;                                    % how many commands?

x   = c.item(l-2);              % get second last command (ignore the command to run this function)
cmd = x.getTextContent;         % get command text

% perform some house-keeping on retrieved command
cmd = char(cmd);            % convert to char
cmd = strrep(cmd,';','');   % remove trailing semicolon

varargout = {cmd};
