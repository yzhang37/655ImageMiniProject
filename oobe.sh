work_path=$(dirname $(readlink -f $0))
cd ${work_path}

chmod +x ./frontend/prereq_frontend.sh
chmod +x ./build.sh
chmod +x ./manager/prereq_backend.sh
chmod +x ./manager/run_server.sh

./frontend/prereq_frontend.sh
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install frontend files.\e[0m"
  exit $ret
fi

./manager/prereq_backend.sh
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install python backend files.\e[0m"
  exit $ret
fi

./build.sh
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to build frontend stuffs.\e[0m"
  exit $ret
fi

./manager/run_server.sh
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to run python server.\e[0m"
  exit $ret
fi
