# Building Segmentation for Disaster Resilience (Open Cities AI)



The aim of this project is to develop a building detection machine learning pipeline that will detect buildings given aerial drone photo-maps. Given overhead images of multiple African cities, our machine learning model aims to accurately predict the outline of the buildings. These insights can be used to support mapping for disaster risk management in African cities. Spacenet4 is our model of choice along with the Solaris machine learning pipeline.

### Setup

To run the pipeline (ML Pipeline.ipynb), setup the Solaris environment in Anaconda :- 
- Clone and download the repository 
- conda env create -f  solaris-gpu.yml   (Setup the solaris environment using the solaris YAML file)
- conda activate solaris (Activate the solaris environemnt)
- conda install -c anaconda ipykernel
- python -m ipykernel install --user --name=solaris
- jupyter-notebook (Run the notebook)

Alternatively, you can also set up the Solaris environment by following the below steps. (In case the above approach does not work)
  - Clone the solaris git repository (git clone https://github.com/cosmiq/solaris.git)
  - Create the solaris environment in Anaconda (conda env create -f environment-gpu.yml) (Has been tested for GPU only in our project, although there is a CPU YAML environment file as well)
  - Activate the solaris environment (conda activate solaris)
  - Run the command (pip install .)
  - Install the other required packages if not installed already (Refer to the package list in solaris-gpu.yml) manually using the anaconda pip command
    - Run the command- which pip
    (Output is /home/anaconda/envs/solaris/bin/pip)
    - Install the other packages manually using the pip package
    (/home/anaconda/envs/solaris/bin/pip install <package_name>)

 (You can check out if the pre-requisite packages are installed by running the import statements in the first cell of ML Pipeline.ipynb)

### Data Download

The dataset used for training and testing the ML model for this project is the competition training data (**train_tier_1**) for the Open Cities AI challenge (https://www.drivendata.org/competitions/60/building-segmentation-disaster-resilience/page/151/)
Download the data from the URL above prior to running the pipeline

### Solaris ML Pipeline

Run the notebook file (ML Pipeline.ipynb) sequentially.

The models are stored in the **checkpoints** folder (The trained **SpaceNet4** model file over the 10 African cities data is **xdxd.pth**)

If you wish to avoid re-training the entire model from scratch, remove the **checkpoints** folder path variable before running the following command in the Jupyter notebook.

~~~
##Remove the checkpoints folder from directories (if you don't want to re-train the mode)
for directory in directories:
    shutil.rmtree(directory, ignore_errors=True)
    os.makedirs(directory)
    file_name = directory + '/.keep'
    f = open(file_name, 'a+')
    f.close
~~~

### Changing the hyperparameters

While training and fine-tuning the model, the hyperparameters might have to be changed. This can be changed at the **model.yml** file. Some of the key hyperparameters that were modified include the Normalize parameters, epochs and the lr (**learning rate**)
 
