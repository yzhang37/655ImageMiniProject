# 655 Simple Image Recognition Mini Project

## Preparation
1. Use **mini-project.xml** rspec file to create GENI nodes    
2. Log in node **manager**:
	
3. Log in nodes **worker-1**, **worker-2**, and **worker-3**:   
		use these commands to download code and install packages by the automated script:    
		`wget https://raw.githubusercontent.com/yzhang37/655ImageMiniProject/main/worker/worker_prerequisite.sh`    
		`chmod +x ./worker_prerequisite.sh`    
		`./worker_prerequisite.sh`    



## Run the project	
4. In **manager**:	

5. In **worker-1**:    
	`python3 -m worker.py 0 10.10.1.1 2888`	    
   In **worker-2**:    
	`python3 -m worker.py 0 10.10.2.1 2889`	    
   In **worker-3**:    
	`python3 -m worker.py 0 10.10.3.1 2890`	    


