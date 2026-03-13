#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

import netCDF4
from netCDF4 import Dataset

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

import xarray as xr
import pandas as pd

import os
from glob import glob
import cmocean
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

import matplotlib.gridspec as gridspec
import matplotlib.ticker as mticker

import scipy
from scipy.stats import norm
from scipy.stats import brunnermunzel

import geopandas as gpd






