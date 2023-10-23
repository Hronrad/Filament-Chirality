import os
time, label =[], []
folder = 'D:/train/data/2'
# with open(folder+'data.txt','r') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.split()

#         time.append(line[0][:14])
#         label.append(line[3][0])


# for filename in os.listdir(folder):
#     filepath = os.path.join(folder,filename)
#     filetime = filename[:14]
#     if filetime in time:
#         index = time.index(filetime)
#         l = label[index]
#         os.rename(filepath,os.path.join(folder,l,filename))
#         print(filepath,'ok')

for filename in os.listdir(folder):
    filepath = os.path.join(folder,filename)
    if filename.endswith('hmi.png'):
        os.rename(filepath,os.path.join(folder,'hmi',filename))
    elif filename.endswith('ha.png'):
        os.rename(filepath,os.path.join(folder,'ha',filename))