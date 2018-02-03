# OpenScience Toolbox
This toolbox provides general purposes functions within python to manage data and analysis scripts required to generate statistics, figures for a particular study.

## Matlab specific setup

### Installing JSONLab

Project settings are stored in a JSON text file, which makes it simple to track changes over the life-time of the project. Unfortunately MATLAB does a poor job of read/writing from JSON files. Therefore this toolbox uses a third-party library provided for accesses JSON files. The library can be obtained through [fangg's Github page](https://github.com/fangq/jsonlab).

### Using the Matlab engine within Python 

The GUI based version of this library is built using python. To provide the user with easy access to their data and functions, I have provided access to MATLAB scripts using the MATLAB/Python engine. To activate this engine execute the following commands within the terminal environment. `matlabroot` is the location of your matlab install e.g. `/Applications/MATLAB_R2015b.app` 


On Windows systems —

```
cd "matlabroot\extern\engines\python"
python setup.py install
```

On Mac or Linux systems —

```
cd "matlabroot/extern/engines/python"
python setup.py install
```


