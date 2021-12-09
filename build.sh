#!/bin/zsh
work_path=$(dirname $(readlink -f $0))
cd ${work_path}

target_path="$work_path/manager/static"
if [ -d "$target_path" ]; then
  echo -e "\e[33mClearing previous target directory $target_path...\e[0m"
  rm -r $target_path
fi

cd frontend
echo -e "\e[34mUpdating node_modules...\e[0m"
yarn

ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to update node_modules.\e[0m"
  exit
fi

echo -e "\e[34mBuilding frontend files...\e[0m"
npm run build

ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mBuilding frontend files failed.\e[0m"
  exit
fi

mv dist $target_path
touch $target_path/.gitkeep
echo -e "\e[32mDeploy completed!\e[0m"
echo -e "Please run \e[32mstart.sh\e[0m to start the server."
