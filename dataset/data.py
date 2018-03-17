import os
import shutil

for i in range(17):
    idx = i + 1
    if not os.path.exists('train/'+ str(idx)):
        os.makedirs('train/' + str(idx))

if not os.path.exists('test'):
    os.makedirs('test')


f = open('files.txt', 'r')
line = f.read()
line = line.split('\n')
count = 0
test_count = 0
for i in range (17):
    for j in range(70):
        shutil.move(line[count], 'train/' + str(i+1) + '/image_' + format(j+1, '04d') + '.jpg')
        count += 1
    for k in range(10):
        test_count += 1
        shutil.move(line[count], 'test/image_' + format(test_count, '04d') + '.jpg')
        count += 1
