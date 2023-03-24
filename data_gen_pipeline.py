import subprocess
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--n_samples',type=int)
args=parser.parse_args()

print('pre processing data')
subprocess.call(['python', 'Preprocessing.py'])
print('generating name combs')
subprocess.call(['python', 'generating_name_combs.py'])
print('mrz generation')
subprocess.call(['python', 'mrz_gen.py'])
print('image generation')
subprocess.call(['python', 'generating_images.py', '--n_samples', str(args.n_samples)])
print("adding noise")
subprocess.call(['python', 'image_degradation.py'])
