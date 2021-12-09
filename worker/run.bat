SET PATH=C:\Users\lacus\anaconda3;%PATH%

start cmd /k python -m worker 0 localhost 2888
start cmd /k python -m worker 0 localhost 2889
start cmd /k python -m worker 0 localhost 2890