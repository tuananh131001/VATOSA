STEP 1 : Install Pycharm and Annaconda
https://www.jetbrains.com/pycharm/
https://www.anaconda.com/

Step 2 : clone this Github  ( a bit long)

# Feature Extraction ( take information from voice files)
## 1. Setup Enviroment
### Step 1. Change python interepter to orginal python ![image](https://user-images.githubusercontent.com/67695658/181903398-3be9f989-7372-4f69-a445-0185dec59a91.png)  

![image](https://user-images.githubusercontent.com/67695658/181903369-b7e9308e-cc7c-49de-a03d-4ea142c3547f.png)


### Step 2 . Open ![image](https://user-images.githubusercontent.com/67695658/181903426-5d62d42f-b062-4e5a-afae-1f1e1306d425.png)  
### Step 3 Check modules 

![image](https://user-images.githubusercontent.com/67695658/181903442-9d0a3308-3610-4f7b-9668-c336021956a8.png)

if any red underline hold cursor on the line and it will ask you to install
### Step 4 Run
if error like this  mean you missing module 
![image](https://user-images.githubusercontent.com/67695658/181903528-19af98a6-8645-45d4-86c5-67ee61309d9b.png)

click on blue line to the file you will see like this. Repeat Step 3  
![image](https://user-images.githubusercontent.com/67695658/181903553-a2a092f5-0f1c-4797-a3c6-54841026755d.png)  
IF this , mean you sucess. Congratulation!
![image](https://user-images.githubusercontent.com/67695658/181903627-5d1c94ec-342c-4aa4-9035-0543d4ec7b3a.png)  

## 2. Use own file
### 2.1 Change the config
### Change your path the folder of the project in ```configure.py``` in ```extraAudio```  
![image](https://user-images.githubusercontent.com/67695658/181903873-ccec5ec2-608d-4ff3-a544-d0f62fbbb854.png)

![image](https://user-images.githubusercontent.com/67695658/181903054-fca80df5-c363-475d-b25a-c21ea63a0bdc.png)

 ### In extractAudio open folder and put as path 
``` wavs->voxceleb1->dev(train)/test(test/enroll)->wav->name(ex:tuananh)->name(ex:tuananh)->putfilehere```  
 
 ![image](https://user-images.githubusercontent.com/67695658/181903762-0ad7ba73-3759-4bff-9545-6ca2358c20d6.png)

### 2.2 For the test
  you only need 2 file wav name it "enroll" and "test" .The path will be above
  
 example path for 2 file enrole PREPARE for extract : ```extractAudio\wavs\voxceleb1\test\wav\TA ```
example path for 2 file enroll AFTER extarct :``` extractAudio\wavs\voxceleb1\test\feat\test_logfbank_nfilt40```
# Run Authentication (RUN ONLY ON WINDOWS)

## 1. Setup Enviroment
### Step 1. Change python interepter to anaconda ![image](https://user-images.githubusercontent.com/67695658/181905230-e7516a70-7be9-4f7b-9427-3e7714667516.png)   
## ```train.py```

Put train file ```.p``` in feat_logfbank_nfilt40/train/yourfoldername/files.p  
then run  ```train.py```
These can be changed
![image](https://user-images.githubusercontent.com/67695658/181888344-4d58e8a1-4a87-4624-b102-aedf236b3c35.png)




## ```enroll.py```

Put enroll file ```.p``` in feat_logfbank_nfilt40/test/yourfoldername/enroll.p (must name enroll)  
then run  ```enroll.py```

![image](https://user-images.githubusercontent.com/67695658/181884579-4573ba22-d9af-4ea4-b66b-fd49528c0e0f.png)
- n_classes is num of files trainning
- cp_num is checkpoint to be use
other no need to config


## ``` identification.py```

### MUST RUN ```enroll.py``` before identi
Put enroll file ```.p``` in feat_logfbank_nfilt40/test/yourfoldername/test.p (must name test)  
then run  ```enroll.py```
![image](https://user-images.githubusercontent.com/67695658/181879091-d2c2b6c2-7829-45b1-9343-8f1fb6100c8a.png)  

Change the test to the test file have enroll and put the list of person have been train into the list

These can be change

![image](https://user-images.githubusercontent.com/67695658/181885297-2cb1b864-9955-4995-9675-132aff2db85c.png)

--> Result will be   
![image](https://user-images.githubusercontent.com/67695658/181885813-f5162ee6-8463-4cde-9ab7-8f2bc1db282c.png)


## 2. Voice controller part 

### 1. Install 
  - Install numpy package from interpreter settings 
  - Install librosa libray version 0.9.2, numpy library version 1.22.4 , and numba version 0.56.0

### 2. Run order
  - Run the process_dataset.py
  - Run the build_model.py
  - Run the prediction.py




# How to install on Mac OS M1

install this python: https://www.python.org/ftp/python/3.10.6/python-3.10.6-macos11.pkg  

Use this pycharm : https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=macM1   

Choose interepter like this :    
![image](https://user-images.githubusercontent.com/67695658/188409083-d163986b-ffd2-4607-be14-7b89709df576.png)


install all in requirements.txt in voice_authetication :  
![image](https://user-images.githubusercontent.com/67695658/188408656-ed4c41b8-8364-43b6-a2c8-6107d97165e8.png). 

Run these command inside terminal of pycharm :  

```
pip3 install customtkinter
pip install playsound
pip install sounddevice
pip install tensorflow-metal
pip install tensorflow-macos
pip install python_speech_features
pip3 install torch torchvision torchaudio
```
If any error with tensorflow try this command   
```pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl```   
<h1 style="color:yellow; background-color:blue;">FAQ</h1>
## Limit

![image](https://user-images.githubusercontent.com/67695658/184615459-2e788a13-2fbf-42f9-847b-360ac395f041.png)

If see this, make sure the "VATOSA\feat_logfbank_nfilt40\train" is 200 folder , if out of range, delete some korean voices folder
Otherwise train and enroll will not work
## sndfile error
![image](https://user-images.githubusercontent.com/67695658/188459892-b34a63e7-da7c-4480-af35-1539cce7bea1.png)

1. go to finder press COMMAND+ SHIFT + G   
![image](https://user-images.githubusercontent.com/67695658/188459643-516c91b5-8620-4e69-9119-bf7ac6fc8c6b.png)
2. type ```~/.zshrc ``` press Enter   
![image](https://user-images.githubusercontent.com/67695658/188461413-20118e3f-2ab7-4bf5-8ccf-c5f2cc036c04.png)

3. add this line ```export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"```   
![image](https://user-images.githubusercontent.com/67695658/188459449-fc053325-eddf-4c5c-b8d1-9f7bd746c512.png)
4. save the file and reopen Pycharm


## 👑 Credit
Nguyen Tuan Anh – s3864077  
Tran Nguyen Ha Khanh – s3877707   
Tran Mai Nhung – s3879954   
Vo Quoc Huy – s3823236   
Youngmoon Jung (dudans@kaist.ac.kr) at KAIST, South Korea
