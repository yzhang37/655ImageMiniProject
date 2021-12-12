# 655 Image Recognition Mini Project
#### Team members: Yanchong Peng, Jinghao Ye, Zhenghang Yin, Yuhang Sun   
## Preparation
1. Use **mini-project.xml** rspec file to create GENI nodes    
2. Log in node **manager**:    
	use these commands to **download everything** and **start server directly** by the automated script:    
		`curl -o manager.zip https://codeload.github.com/yzhang37/655ImageMiniProject/legacy.zip/main`    
		`unzip manager.zip`    
		`cd ./yzhang37-655ImageMiniProject-edb461f`    
		`chmod +x ./oobe.sh`    
		`./oobe.sh`    
3. Log in nodes **worker-1**, **worker-2**, and **worker-3**:   
		use these commands to **download code and install packages** by the automated script:    
		`wget https://raw.githubusercontent.com/yzhang37/655ImageMiniProject/main/worker/worker_prerequisite.sh`    
		`chmod +x ./worker_prerequisite.sh`    
		`./worker_prerequisite.sh`    



## Run workers    	
4. In **manager**:    
	if the manager is not running, use this command:    
	`./manager/run_server.sh`    
5. In **worker-1**:    
	`python3 -m worker.py 0 10.10.1.1 2888`	    
   In **worker-2**:    
	`python3 -m worker.py 0 10.10.2.1 2889`	    
   In **worker-3**:    
	`python3 -m worker.py 0 10.10.3.1 2890`	    

6. After the manager and the workers are running, open a browser and use the url given in the manager to upload images.    
