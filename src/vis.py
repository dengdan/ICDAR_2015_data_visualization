#encoding utf-8
import matplotlib.pyplot as plt
import logging

import sys
sys.path.insert(0, '../pylib/src')

import util.io
#import util.log
import util.img
from config import training_image_name_pattern, training_gt_name_pattern

#util.log.init_logger()
GREEN = 'green'
def read_data(idx):
    image = util.img.imread(training_image_name_pattern%(idx), rgb = True)
    gt = util.io.readlines(training_gt_name_pattern%(idx))
    return image, gt

def parse_gt_line(line):
    points = [None] * 4
    word = None
    data = line.split(',')
    
    data[0] = data[0].replace('\xef\xbb\xbf', '')
    
    for idx, d in enumerate(data):
        if idx < 8:
            data[idx] = int(d.strip())
       
    word = data[-1].strip()    
    
    for i in xrange(4):
        p = [0] * 2
        p[0] = data[i * 2]
        p[1] = data[i * 2 + 1]
        points[i] = p
        
    return points, word
        
                    

def show(idx, color, show_text, show_origin):
    image, gt = read_data(idx)
    
    
    if show_origin:
        axes = (1, 2)
        ax  = plt.subplot2grid(axes, (0,1))
        ax_image = plt.subplot2grid(axes, (0,0), sharex = ax, sharey = ax)
        ax_image.imshow(image)
    else:
        ax = plt.subplot(111)
    
    ax.imshow(image)
    # draw bounding box
        
    for line in gt:
        points, word = parse_gt_line(line)
        for i in xrange(4):
            start = i
            end = (i + 1) % 4
            util.img.line(axis = ax, xy_start = points[start], xy_end = points[end], color = color)
        if show_text:
            x, y = points[1]
            ax.text(x, y, word, verticalalignment='top', horizontalalignment='left', color = color, fontsize=10)
    plt.show()      
        

import argparse
parser = argparse.ArgumentParser(description='show ICDAR 2015 images of task 4.1')
parser.add_argument('--idx', type=int, required = True,help='the index of the image to be showed, for example: --idx=1 to show img_1.jpg')
parser.add_argument('--show-text', type=int, default=0,help='show ground truth text or not, default not, i.e.,0')
parser.add_argument('--color', type=str, default=GREEN, help='the color of bounding box borders. Use the color strings of matplotlib, for example: white, green, red, etc.')
parser.add_argument('--show-origin', type=int, default=0, help='show original image or not, default not.')
args = parser.parse_args().__dict__
logging.info('**************Arguments*****************')
logging.info(args)
logging.info('****************************************')
show(**args)
