import os
import random
import string

def delete_bin_files(data_folder):
    for filename in os.listdir(data_folder):
        if filename.endswith('.bin'):
            os.remove(os.path.join(data_folder, filename))

def create_random_bin_files(data_folder, count=100, max_size_mb=2):
    chars = string.ascii_letters + string.digits
    for i in range(count):
        rand_name = ''.join(random.choices(chars, k=8))
        file_path = os.path.join(data_folder, f"{rand_name}.bin")
        size = random.randint(1, max_size_mb * 1024 * 1024)
        with open(file_path, 'wb') as f:
            f.write(os.urandom(size))

data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

if __name__ == "__main__":
    delete_bin_files(data_folder)
    create_random_bin_files(data_folder)
