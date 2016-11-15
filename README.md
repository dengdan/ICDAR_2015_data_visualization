# ICDAR_2015_data_visualization
Visualize the dataset of ICDAR 2015. Only challenge 4 task 1 is available currently.

Requirements:
1. Matplotlib
2. ICDAR2015 Challenge 4 dataset. Register and download it from http://rrc.cvc.uab.es/?com=introduction.

Steps:
step 1. config the directory in src/config.py

step 1. execute in src
```
python vis.py --idx=300 --color=white --show-text=1 --show-origin=1

```

See doc:
```
python vis.py -h
```

Examples:
--show-text=0 --show-origin=0
![](https://raw.githubusercontent.com/dengdan/ICDAR_2015_data_visualization/master/example1.png)
--show-text=1 --show-origin=0
![](https://raw.githubusercontent.com/dengdan/ICDAR_2015_data_visualization/master/example2.png)
--show-text=1 --show-origin=1
![](https://raw.githubusercontent.com/dengdan/ICDAR_2015_data_visualization/master/example3.png)

