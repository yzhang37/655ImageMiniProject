echo "Installing Nodejs 16..."
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install nodejs 16.\e[0m"
  exit $ret
fi

sudo apt-get install -y nodejs
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install nodejs 16.\e[0m"
  exit $ret
fi

echo "Installing npm and yarn for nodejs..."
sudo apt-get install -y npm
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install npm.\e[0m"
  exit $ret
fi

sudo npm install -g npm
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install npm.\e[0m"
  exit $ret
fi

sudo npm install -g yarn
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install yarn.\e[0m"
  exit $ret
fi

echo "Installing vue..."
sudo npm install -g vue
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install vue.\e[0m"
  exit $ret
fi

echo "Installing vue client service..."
sudo npm install -g @vue/cli
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install @vue/cli.\e[0m"
  exit $ret
fi