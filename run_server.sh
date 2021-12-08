work_path=$(dirname $(readlink -f $0))
cd ${work_path}/manager
pip install -r requirements.txt
ret=$?
if [ $ret -ne 0 ]; then
  echo -e "\e[31mFailed to install required python requirements.\e[0m"
  exit
fi
clear
python -m main --hostname 0.0.0.0 --port 80
