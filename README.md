# 655 Image Recognition Mini Project
#### Team members: Yanchong Peng, Jinghao Ye, Zhenghang Yin, Yuhang Sun   
## Preparation
1. Use **mini-project.xml** rspec file to create GENI nodes    
2. Log in node **manager**:    
	use these commands to **download everything** and **start server directly** by the automated script:    
		`curl -o manager.zip https://codeload.github.com/yzhang37/655ImageMiniProject/legacy.zip/main`    
		`unzip manager.zip`    
		use `ls` to check the yzhang37-655ImageMiniProject folder name, and then    
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

## Note   
1. Video url: https://drive.google.com/file/d/1gxDpU1c7R3iOMCqg6Ax7R07Aj2Mx05kb/view?usp=sharing    
2. You can use server url to log in our project directly because we use TMUX to keep running our project on GENI.    
3. Recommand upload images of small size and don't upload too much images(e.g. no more than 3 images) because GENI nodes cannot handle too much work.    
4. We provide a sample image(download.jpeg) for you to test.
