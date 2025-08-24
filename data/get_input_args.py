
import argparse


def get_input_args():
   
    parser = argparse.ArgumentParser()

  
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to folder of images')
    parser.add_argument('--arch', type=str, default='vgg',
                        help='CNN model architecture to use: resnet, alexnet, or vgg')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='text file containing dog breed names')

    
    return parser.parse_args()
