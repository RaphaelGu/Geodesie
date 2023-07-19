''' 
batch_rnx2rtkp - template to run multiple simultaneous solutions of rnx2rtkp in Windows.
    This example is configured to run the cellphone data sets available at 
    https://data.mendeley.com/datasets/5prmtwgph3/2
 '''
 
import os
import subprocess
import psutil
import time
from pathlib import Path
 
# set location of data and rnx2rtkp executable
#datapath = Path.cwd() / "batch_processing" / "DATA" / "PHONE_RTKLIBEXPLORER"
#datapath = str(datapath).replace("G:", "\\srv-stj-data\quarta")
datapath = r"batch_processing\DATA\PHONE_RTKLIBEXPLORER"
binpath = Path.home() / "Desktop" / "geodesie" / "rtklib_2.4.2" / "bin" / "rnx2rtkp.exe"

# Choose datasets to process
DATA_SET = 0  # 0=open-sky, 1=partial forest, 2=forest
USE_GROUND_PLANE = True  # True or False
 
# set input files
cfgs = ['ppk_ar_1027_snr24']  # list of config files to run (files should have .conf ext)
rovFile = 'GEOP*.19o'  # rover files with wild cards
baseFile = 'BBYS*.19o' # base files with wild cards
navFile = r'"..\brdm*.19p"' # navigation files with wild cards
outFile = 'ppk_ar_1027'
 
# set maximum number of simultaneous occurences of rnx2rtkp to run
max_windows = 10
 
# get list of current threads running in Windows
current_process = psutil.Process()
num_start = len(current_process.children())
 
# get list of date folders in data path
dates = os.listdir(datapath)
 
# loop through date folders
for date in dates:
    datepath = datapath + '/' + date
    print(datepath)  
       
    # Filter which folders to process
    if not os.path.isdir(datepath):  # skip if not folder
        continue
    if USE_GROUND_PLANE:
        if date[-2:] != 'gp':  #skip folders without ground plane tag in name
            continue
    else: # no ground plane
        if date[-2:] == 'gp':  #skip folders with ground plane tag in name
            continue
 
    # Get list of datasets in this date folder
    datasets = os.listdir(datapath + '/' + date)
     
    # Select desired folder in data set 
    dataset = datepath + '/' + datasets[DATA_SET] # 0=open-sky, 1=partial forest, 2=forest 
    os.chdir(dataset)
  
    # Run a solution for each config file in list       
    for cfg in cfgs:
        # create command to run solution
        rtkcmd=r'%s\rnx2rtkp -x 0 -y 2 -k ..\..\%s.conf -o %s.pos %s %s %s' % (binpath, cfg, outFile + '_' + cfg, rovFile, baseFile, navFile)    
        print(rtkcmd)
        # run command
        subprocess.Popen(rtkcmd)
 
 
    # if max windows open, wait for one to close
    while len(current_process.children())-num_start >= max_windows:
        time.sleep(1) #wait here for existing window to close
 
# Wait for all solutions to finish
print('Waiting for solutions to complete ...')  
while len(current_process.children())-num_start > 0:
    pass #wait here if max windows open        
print('Done')