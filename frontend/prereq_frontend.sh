echo -e "🧩🧩🧩 \e[32mInstalling Nodejs 16...\e[0m"
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install nodejs 16.\e[0m"
  exit $ret
fi
sudo apt-get update
sudo apt-get remove -y --purge man-db
sudo apt-get install -y nodejs
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install nodejs 16.\e[0m"
  exit $ret
fi

echo -e "🧩🧩🧩 \e[32mUpdating npm...\e[0m"
sudo npm install -g npm
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install npm.\e[0m"
  exit $ret
fi

echo -e "🧩🧩🧩 \e[32mInstalling yarn...\e[0m"
sudo npm install -g yarn
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install yarn.\e[0m"
  exit $ret
fi

echo -e "🧩🧩🧩 \e[32mInstalling vue...\e[0m"
sudo npm install -g vue
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install vue.\e[0m"
  exit $ret
fi

echo -e "🧩🧩🧩 \e[32mInstalling vue client service...\e[0m"
sudo npm install -g @vue/cli
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install @vue/cli.\e[0m"
  exit $ret
fi
