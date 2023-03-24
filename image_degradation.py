import cv2
import numpy as np
import os
from random import shuffle
import random
from tqdm  import tqdm



def poisson_noise(img, ratio = 0.8, randomv=False):
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if randomv:
        ratio = random.uniform(0, 1)
        if ratio == 0:
            ratio = 0.1
        
    # Add Poisson noise to the image between 0 and 1
    noisy_img = np.random.poisson(ratio * gray_img)

    # Convert the image back to BGR format
    noisy_img = cv2.cvtColor(noisy_img.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    
    return noisy_img

def gaussian_noise(img, variance=0.5, randomv=False):
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Add Gaussian noise to the image
    mean = 0
    if randomv:
        variance = random.randint(1, 20) / 10
    sigma = variance ** 0.5 #max 5
    noise = np.random.normal(mean, sigma, gray_img.shape)
    noisy_img = gray_img + noise

    # Convert the image back to BGR format
    noisy_img = cv2.cvtColor(noisy_img.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    
    return noisy_img

def gaussian_blur(img, k_size = 5):
    return cv2.GaussianBlur(img, (k_size, k_size), 0)
        
def skew_image(image):
    skew_angle = random.randint(-3, 3)
    height, width = image.shape[:2]

    # Define the skew transformation matrix
    skew_matrix = np.float32([[1, 0, 0], [np.tan(np.deg2rad(skew_angle)), 1, 0]])

    # Find the coordinates of the four corners of the image
    corners = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

    # Apply the skew transformation to the corners of the image
    skewed_corners = cv2.transform(np.array([corners]), skew_matrix)[0]

    # Find the minimum and maximum x and y coordinates of the skewed image
    min_x, max_x = np.min(skewed_corners[:, 0]), np.max(skewed_corners[:, 0])
    min_y, max_y = np.min(skewed_corners[:, 1]), np.max(skewed_corners[:, 1])

    # Calculate the translation needed to move the image within the bounds of the canvas
    tx, ty = -min_x, -min_y
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

    # Apply the translation to the skew transformation matrix
    final_matrix = skew_matrix.copy()
    final_matrix[:, 2] += np.dot(translation_matrix, np.array([[0], [0], [1]]))[:, 0]

    # Apply the final transformation to the image
    warped_image = cv2.warpAffine(image, final_matrix, (int(max_x - min_x), int(max_y - min_y)), borderMode=cv2.BORDER_REPLICATE)

    return warped_image


# Define the folder path
folder_path = 'images'

# Get a list of all files in the folder
files = os.listdir(folder_path)

files = np.array(files)

# Define proportions for train, validation, test, and additional set
clean_prop = 0.5
gauss_prop = 0.2
poisson_prop = 0.2
blur_prop = 0.1

# Get the total number of samples in the files
n_samples = len(files)

# Calculate the number of samples for each set
clean_samples = int(clean_prop * n_samples)
gauss_samples = int(gauss_prop * n_samples)
poisson_samples = int(poisson_prop * n_samples)
blur_samples = n_samples - clean_samples - gauss_samples - poisson_samples

# Shuffle the files
np.random.shuffle(files)

# Split the files into train, validation, test, and additional sets
clean_data = files[:clean_samples]
gauss_data = files[clean_samples:clean_samples+gauss_samples]
poisson_data = files[clean_samples+gauss_samples:clean_samples+gauss_samples+poisson_samples]
blur_data = files[clean_samples+gauss_samples+poisson_samples:]

print('Adding gaussian noise')
for i in tqdm(gauss_data):
    img = cv2.imread(folder_path + '/' + i)
    noisy_img = gaussian_noise(img, randomv=True)
    cv2.imwrite(folder_path + '/' + i, noisy_img)

print('Adding poisson noise')
for i in tqdm(poisson_data):
    img = cv2.imread(folder_path + '/' + i)
    noisy_img = poisson_noise(img, randomv=True)
    cv2.imwrite(folder_path + '/' + i, noisy_img)
    
print('Adding blurr')
for i in tqdm(blur_data):
    img = cv2.imread(folder_path + '/' + i)
    noisy_img = gaussian_blur(img)
    cv2.imwrite(folder_path + '/' + i, noisy_img)
    

files = os.listdir(folder_path)
files = np.array(files)
np.random.shuffle(files)

random_files = np.random.choice(files, size=int(len(files) * 0.2), replace=False)

print('Adding skew')
for i in tqdm(random_files):
    img = cv2.imread(folder_path + '/' + i)
    skewed_img = skew_image(img)
    cv2.imwrite(folder_path + '/' + i, skewed_img)


