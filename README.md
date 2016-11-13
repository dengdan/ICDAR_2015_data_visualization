# ICDAR_2015_data_visualization
Visualize the dataset of ICDAR 2015. Only challenge 4 task 1 is available currently.
1. add pylib/src to PYTHONPATH
For example, add line to `~/.bashrc`, 
```
export PYTHONPATH=YOUR_PATH/pylib/src':$PYTHONPATH
```
1. config the directory in src/config.py
2. execute
```
python vis.py --idx=300 --color=white --show-text=1 --show-origin=1

```

See doc:
```
help vis.py
```

Examples:
--show-text=0 --show-origin=0
![](https://raw.githubusercontent.com/dengdan/ICDAR_2015_data_visualization/master/example1.png)
--show-text=1 --show-origin=0
![](https://raw.githubusercontent.com/dengdan/ICDAR_2015_data_visualization/master/example2.png)
--show-text=1 --show-origin=1
![](https://raw.githubusercontent.com/dengdan/ICDAR_2015_data_visualization/master/example3.png)

