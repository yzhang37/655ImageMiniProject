work_path=$(dirname $(readlink -f $0))
cd ${work_path}

# code for backend prerequisite
echo "Updating Ubuntu software distribution..."
sudo apt-get update -y
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to update software distribution.\e[0m"
  exit $ret
fi

echo "Installing python3 with pip3..."
sudo apt-get install -y python3-pip
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install python3 with pip3.\e[0m"
  exit $ret
fi

echo "Installing library used to handle JPEG..."
sudo apt-get install -y libjpeg-dev zlib1g-dev
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install libjpeg-dev.\e[0m"
  exit $ret
fi

echo "Installing torch and torch visions..."
pip3 --no-cache-dir install torch==1.10.0+cpu torchvision==0.11.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install torchvision.\e[0m"
  exit $ret
fi

echo "Installing remaining python environments..."
pip3 install -r requirements.txt
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to python environments.\e[0m"
  exit $ret
fi
