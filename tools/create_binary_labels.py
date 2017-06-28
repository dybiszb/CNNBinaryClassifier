# Directory structure must be as follows:
# []- root_path
# |------ type_0_dir
# |------ type_1_dir
#
import argparse
import os, os.path
from os import listdir
from os.path import isfile, join

# ------------------------------------------------------------------------------
# Parse the arguments
# ------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("type_0_dir", help="Directory relative to the root_path with images of type 0", type=str)
parser.add_argument("type_1_dir", help="Directory relative to the root_path with images of type 1", type=str)
parser.add_argument("root_path", help="Root for relative path.", type=str)
args = parser.parse_args()
type_0_path = args.root_path + '/' + args.type_0_dir
type_1_path = args.root_path + '/' + args.type_1_dir
print '[-] Path to images of type 0:', type_0_path
print '[-] Path to images of type 1:', type_1_path
print '[-] Root path:', args.root_path

# ------------------------------------------------------------------------------
# Calculate Train-Test Division
# ------------------------------------------------------------------------------
percentage_of_train=0.9
num_files_type_0 = len([name for name in os.listdir(type_0_path) if os.path.isfile(os.path.join(type_0_path, name))])
num_files_type_1 = len([name for name in os.listdir(type_1_path) if os.path.isfile(os.path.join(type_1_path, name))])
num_train_type_0 = int(num_files_type_0 * percentage_of_train)
num_train_type_1 = int(num_files_type_1 * percentage_of_train)

# ------------------------------------------------------------------------------
# Get files names
# -----------------------------------------------------------------------------
type_0_files = [os.path.abspath(type_0_path + '/' + f) for f in listdir(type_0_path) if isfile(join(type_0_path, f))]
type_1_files = [os.path.abspath(type_1_path + '/' + f) for f in listdir(type_1_path) if isfile(join(type_1_path, f))]
type_0_train_files = type_0_files[:num_train_type_0]
type_1_train_files = type_1_files[:num_train_type_1]
type_0_test_files = type_0_files[num_train_type_0:]
type_1_test_files = type_1_files[num_train_type_1:]

# ------------------------------------------------------------------------------
# Spawn train_files.txt
# ------------------------------------------------------------------------------
train_txt_path = args.root_path + '/train_files.txt'
with open(train_txt_path, 'w') as train_txt_path:
    for file_name in type_0_train_files:
        train_txt_path.write(file_name + ' 0\n')
    for file_name in type_1_train_files:
        train_txt_path.write(file_name + ' 1\n')

# ------------------------------------------------------------------------------
# Spawn test_files.txt
# ------------------------------------------------------------------------------
test_txt_path = args.root_path + '/test_files.txt'
with open(test_txt_path, 'w') as test_txt_path:
    for file_name in type_0_test_files:
        test_txt_path.write(file_name + ' 0\n')
    for file_name in type_1_test_files:
        test_txt_path.write(file_name + ' 1\n')

print 'Finished'
