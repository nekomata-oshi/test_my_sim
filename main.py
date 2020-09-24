from cosinesimilaraty import CoSim
from sys import argv

script, filename_1, filename_2, filename_in = argv
file_1 = open(filename_1, encoding = 'utf_8')
file_2 = open(filename_2, encoding = 'utf_8')
file_in = open(filename_in, 'w')

str_1 = file_1.read()
str_2 = file_2.read()
test_cosim = CoSim(str_1, str_2)
print(test_cosim)
file_in.write(str(test_cosim))

file_1.close()
file_2.close()
file_in.close()
