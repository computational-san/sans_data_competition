#!/usr/bin/env python
# coding: utf-8

# # Data
# 
# For this data competition, we will be using the Friday Night Lights dataset from:
# 
# Chang, L. J., Jolly, E., Cheong, J. H., Rapuano, K. M., Greenstein, N., Chen, P. H. A., & Manning, J. R. (2021). Endogenous variation in ventromedial prefrontal cortex state dynamics during naturalistic viewing reflects affective experience. *Science Advances, 7(17), eabf7129*.
# 
# In this dataset, participants (n=35) watched the pilot episode of the NBC television show Friday Night Lights while undergoing fMRI. We are sharing the raw data in the BIDS format. We are also sharing data that has been preprocessed using fMRIPrep version 20.2.1. See ```derivatives/code/fmriprep.sh``` for the script used to run preprocessing. We have also performed denoising on the preprocessed data by running a univariate GLM, which included the following regressors:
# 
# - Intercept, Linear & Quatdratic Trends (3)
# - Expanded Realignment Parameters (24). Derivatives, quadratics, quadratic derivatives
# - Spikes based on global outliers greater than 3 SD and also based on average frame differencing
# - CSF regressor (1)
# 
# See ```derivatives/code/Denoise_Preprocessed_Data.ipynb``` file for full details of the denoising model. We have included denoised data that is unsmoothed and also has been smoothed with a 6mm FWHM Gaussian kernel. We have included nifti and hdf5 versions of the data. Nifti files can be loaded using any software. HDF5 files are much faster to load if you are using our [nltools](https://nltools.org/) toolbox for your data analyses. Note that subject sub-sid000496 had bad normalization using this preprocessing pipeline, so we have not included this participant in the denoised data. 
# 
# 
# We are also sharing additional data from this paper, which may be used in projects:
# 
# - Study 1 (n=13) fMRI Data viewing episodes 1 & 2 - Available on [OpenNeuro](https://openneuro.org/datasets/ds003524).
# 
# - Study 3 (n=20) Face Expression Data - Available on [OSF](https://osf.io/f9gyd/). We are only sharing extracted Action Unit Values. We do not have permission to share raw video data.
# 
# - Study 4 (n=192) Emotion Ratings - Available on [OSF](https://osf.io/f9gyd/). Rating data was collected on Amazon Mechanical Turk using a custom Flask [web application](https://github.com/cosanlab/moth_app).
# 
# - Code from the original paper is available on [Github](https://github.com/cosanlab/vmPFC_dynamics)
# 
# # Downloading Data
# 
# All of the data is being hosted by [OpenNeuro](https://openneuro.org/datasets/ds003521). The entire dataset is about 16gb and can be downloaded directly from the website and also using the AWS command line interface. See the OpenNeuro [instructions](https://openneuro.org/datasets/ds003521/download) for downloading. If you have limited storage space, we recommend using Datalad to download only the files you want to work with. 
# 

# ## DataLad
# 
# The easist way to access the data is using [DataLad](https://www.datalad.org/), which is an open source version control system for data built on top of [git-annex](https://git-annex.branchable.com/). Think of it like git for data. It provides a handy command line interface for downloading data, tracking changes, and sharing it with others.
# 
# While DataLad offers a number of useful features for working with datasets, there are three in particular that we think make it worth the effort to install for this course.
# 
# 1) Cloning a DataLad Repository can be completed with a single line of code `datalad install <repository>` and provides the full directory structure in the form of symbolic links. This allows you to explore all of the files in the dataset, without having to download the entire dataset at once.
# 
# 2) Specific files can be easily downloaded using `datalad get <filename>`, and files can be removed from your computer at any time using `datalad drop <filename>`. As these datasets are large, this will allow you to only work with the data that you need for a specific tutorial and you can drop the rest when you are done with it.
# 
# 3) All of the DataLad commands can be run within Python using the datalad [python api](http://docs.datalad.org/en/latest/modref.html).
# 
# We will only be covering a few basic DataLad functions to get and drop data. We encourage the interested reader to read the very comprehensive DataLad [User Handbook](http://handbook.datalad.org/en/latest/) for more details and troubleshooting.
# 
# ### Installing Datalad
# 
# DataLad can be easily installed using [pip](https://pip.pypa.io/en/stable/).
# 
# `pip install datalad`
# 
# Unfortunately, it currently requires manually installing the [git-annex](https://git-annex.branchable.com/) dependency, which is not automatically installed using pip.
# 
# If you are using OSX, we recommend installing git-annex using [homebrew](https://brew.sh/) package manager.
# 
# `brew install git-annex`
# 
# If you are on Debian/Ubuntu we recommend enabling the [NeuroDebian](http://neuro.debian.net/) repository and installing with apt-get.
# 
# `sudo apt-get install datalad`
# 
# For more installation options, we recommend reading the DataLad [installation instructions](https://git-annex.branchable.com/).
# 

# In[1]:


get_ipython().system('pip install datalad')


# ### Download Data with DataLad
# 
# The FNL dataset can be accessed at the following location https://openneuro.org/datasets/ds003521. To download the dataset run `datalad install https://github.com/OpenNeuroDatasets/ds003521.git` in a terminal in the location where you would like to install the dataset. Don't forget to change the directory to a folder on your local computer. The full dataset is approximately 16gb.
# 
# You can run this from the notebook using the `!` cell magic.

# In[7]:


get_ipython().system('mkdir ~/Downloads/FridayNightLights ')

get_ipython().system('cd ~/Downloads/FridayNightLights')

get_ipython().system('datalad install https://github.com/OpenNeuroDatasets/ds003521.git')


# ## Datalad Basics
# 
# You might be surprised to find that after cloning the dataset that it barely takes up any space `du -sh`. This is because cloning only downloads the metadata of the dataset to see what files are included.
# 
# You can check to see how big the entire dataset would be if you downloaded everything using `datalad status`.

# In[6]:


get_ipython().run_line_magic('cd', '~/Downloads/FridayNightLights/ds003521')

get_ipython().system('datalad status --annex')


# ### Getting Data
# One of the really nice features of datalad is that you can see all of the data without actually storing it on your computer. When you want a specific file you use `datalad get <filename>` to download that specific file. Importantly, you do not need to download all of the data at once, only when you need it.
# 
# Now that we have cloned the repository we can grab individual files. For example, suppose we wanted to grab the first subject's confound regressors generated by fmriprep.

# In[8]:


get_ipython().system('datalad get participants.tsv')


# Now we can check and see how much of the total dataset we have downloaded using `datalad status`

# In[9]:


get_ipython().system('datalad status --annex all')


# If you would like to download all of the files you can use `datalad get .`. Depending on the size of the dataset and the speed of your internet connection, this might take awhile. One really nice thing about datalad is that if your connection is interrupted you can simply run `datalad get .` again, and it will resume where it left off.
# 
# You can also install the dataset and download all of the files with a single command `datalad install -g https://github.com/OpenNeuroDatasets/ds003521.git`. You may want to do this if you have a lot of storage available and a fast internet connection. For most people, we recommend only downloading the files you need for your project.

# ### Dropping Data
# Most people do not have unlimited space on their hard drives and are constantly looking for ways to free up space when they are no longer actively working with files. Any file in a dataset can be removed using `datalad drop`. Importantly, this does not delete the file, but rather removes it from your computer. You will still be able to see file metadata after it has been dropped in case you want to download it again in the future.
# 
# As an example, let's drop the Localizer participants .tsv file.

# In[10]:


get_ipython().system('datalad drop participants.tsv')


# ## Datalad has a Python API!
# One particularly nice aspect of datalad is that it has a Python API, which means that anything you would like to do with datalad in the commandline, can also be run in Python. See the details of the datalad [Python API](http://docs.datalad.org/en/latest/modref.html).
# 
# For example, suppose you would like to clone a data repository, such as the Localizer dataset. You can run `dl.clone(source=url, path=location)`. Make sure you set `localizer_path` to the location where you would like the Localizer repository installed.

# In[11]:


import os
import glob
import datalad.api as dl
import pandas as pd

localizer_path = '~/Downloads/FridayNightLights'

dl.clone(source='https://github.com/OpenNeuroDatasets/ds003521.git', path=localizer_path)


# We can now create a dataset instance using `dl.Dataset(path_to_data)`.

# In[6]:


ds = dl.Dataset(localizer_path)


# How much of the dataset have we downloaded?  We can check the status of the annex using `ds.status(annex='all')`.

# In[12]:


results = ds.status(annex='all')


# Looks like it's empty, which makes sense since we only cloned the dataset. 
# 
# Now we need to get some data. Let's start with something small to play with first.
# 
# Let's use `glob` to find all of the tab-delimited confound data generated by fmriprep. 

# In[14]:


file_list = glob.glob(os.path.join(localizer_path, '*', 'fmriprep', '*', 'func', '*tsv'))
file_list.sort()
file_list[:10]


# glob can search the filetree and see all of the relevant data even though none of it has been downloaded yet.
# 
# Let's now download the first subjects confound regressor file and load it using pandas.

# In[15]:


result = ds.get(file_list[0])

confounds = pd.read_csv(file_list[0], sep='\t')
confounds.head()


# What if we wanted to drop that file? Just like the CLI, we can use `ds.drop(file_name)`.

# In[16]:


result = ds.drop(file_list[0])


# To confirm that it is actually removed, let's try to load it again with pandas.

# In[17]:


confounds = pd.read_csv(file_list[0], sep='\t')


# Looks like it was successfully removed.
# 
# We can also load the entire dataset in one command if want using `ds.get(dataset='.', recursive=True)`. We are not going to do it right now as this will take awhile and require lots of free hard disk space.
# 
# Let's actually download one of the files we will be using in the tutorial. First, let's use glob to get a list of all of the functional data that has been preprocessed by fmriprep, denoised, and smoothed.

# In[12]:


file_list = glob.glob(os.path.join(localizer_path, 'derivatives', 'smoothed', '*_task-movie_run-1_space-MNI152NLin2009cAsym_desc-preproc_trim_smooth6_denoised_bold.hdf5'))
file_list.sort()
file_list


# Now let's download the first subject's file using `ds.get()`. This file is 825mb, so this might take a few minutes depending on your internet speed.

# In[19]:


result = ds.get(file_list[0])


# How much of the dataset have we downloaded?  We can check the status of the annex using `ds.status(annex='all')`.

# In[21]:


result = ds.status(annex='all')

