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

# Run Authentication (RUN ONLY ON WINDOWS)

## 1. Setup Enviroment
### Step 1. Change python interepter to anaconda ![image](https://user-images.githubusercontent.com/67695658/181905230-e7516a70-7be9-4f7b-9427-3e7714667516.png)   
## ```train.py```

These can be changed

![image](https://user-images.githubusercontent.com/67695658/181888344-4d58e8a1-4a87-4624-b102-aedf236b3c35.png)




## ```enroll.py```

![image](https://user-images.githubusercontent.com/67695658/181884579-4573ba22-d9af-4ea4-b66b-fd49528c0e0f.png)
- n_classes is num of files trainning
- cp_num is checkpoint to be use
other no need to config


## ``` identification.py```
### MUST RUN ```enroll.py``` before identi

![image](https://user-images.githubusercontent.com/67695658/181879091-d2c2b6c2-7829-45b1-9343-8f1fb6100c8a.png)  

Change the test to the test file have enroll and put the list of person have been train into the list

These can be change

![image](https://user-images.githubusercontent.com/67695658/181885297-2cb1b864-9955-4995-9675-132aff2db85c.png)

--> Result will be   
![image](https://user-images.githubusercontent.com/67695658/181885813-f5162ee6-8463-4cde-9ab7-8f2bc1db282c.png)


## Credit
Youngmoon Jung (dudans@kaist.ac.kr) at KAIST, South Korea
