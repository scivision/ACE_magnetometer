[![Build Status](https://travis-ci.com/scivision/ACE_magnetometer.svg?branch=master)](https://travis-ci.com/scivision/ACE_magnetometer)
[![Coverage Status](https://coveralls.io/repos/github/scivision/ACE_magnetometer/badge.svg?branch=master)](https://coveralls.io/github/scivision/ACE_magnetometer?branch=master)
[![Build status](https://ci.appveyor.com/api/projects/status/iirc72tlooono1k0?svg=true)](https://ci.appveyor.com/project/scivision/ace-magnetometer)
[![PyPi versions](https://img.shields.io/pypi/pyversions/ace_magnetometer.svg)](https://pypi.python.org/pypi/ace_magnetometer)
[![PyPi format](https://img.shields.io/pypi/format/ace_magnetometer.svg)](https://pypi.python.org/pypi/ace_magnetometer)
[![PyPi Download stats](http://pepy.tech/badge/ace_magnetometer)](http://pepy.tech/project/ace_magnetometer)


# ACE magnetometer: Load and plot

Load and Plot ACE satelite magnetometer data for Python.

![ACE magnetometer time series plot](tests/timeplot.png)


## Data

Get data from [FTP site](ftp://mussel.srl.caltech.edu/pub/ace/browse/MAG16sec).

## Python

Download ACE magnetometer 16 second cadence by date:
```sh
DownloadACE.py 2012-02-03 ~/data
```

Load and Plot ACE magnetometer data
```sh
PlotACE.py 2012-02-03 ~/data
```

## Matlab
Matlab is not regularly used.

```matlab
PlotACE()
```
