with open("mean_ap.txt", "r", encoding='utf-8') as f:  # 打开文本
    mean_ap = f.read()  # 读取文本

with open("category_index_name.txt", "r", encoding='utf-8') as f:  # 打开文本
    data = f.read()  # 读取文本
    data = data.replace('[', '')  # 去掉[
    data = data.replace(']', '')  # 去掉]
    data = data.replace('\'', '')  # 去掉'
    data = data.replace(', ', ',')  # 去掉,后面的空格
    data = data.replace(' ', '_')  # 将所有空格替换为_，如open eyes变成open_eyes
    category_index_name = data.split(',')  # 以,分割

with open("num_gt_instances_per_class.txt", "r", encoding='utf-8') as f:  # 打开文本
    data = f.read()  # 读取文本
    data = data.replace('[', '')  # 去掉[
    data = data.replace(']', '')  # 去掉]
    data = data.replace('\n', '')  # 去掉回车
    num_gt_instances_per_class = data.split()  # 采用默认方式分割

with open("per_class_ap.txt", "r", encoding='utf-8') as f:  # 打开文本
    data = f.read()  # 读取文本
    data = data.replace('[', '')  # 去掉[
    data = data.replace(']', '')  # 去掉]
    data = data.replace('\n', '')  # 去掉回车
    per_class_ap = data.split()  # 采用默认方式分割

line1 = '类别 '
for i, e in enumerate(category_index_name):
    line1 = line1 + e + ' '


line2 = '类别数量 '
zero_arr = []  # 存放不应该有的类别的编号(如果训练时，自定义了类别，zero_arr就会存入没有选中的类别的编号)
for i, e in enumerate(num_gt_instances_per_class):
    # 去掉不应该有的类别(如果训练时，自定义了类别，就会进入下面的if)
    # if len(category_index_name) != len(num_gt_instances_per_class):
    #     if e == '0':  # 没有选中的类别的数量为0
    #         zero_arr.append(i)
    #         continue
    line2 = line2 + e + ' '

line3 = 'max(类别数量) '
num_gt_instances_per_class2 = list(map(int, num_gt_instances_per_class))
line3 = line3 + str(max(num_gt_instances_per_class2))

line4 = 'ap值, '
for i, e in enumerate(per_class_ap):
    line4 = line4 + e + ' '

line5 = '类别数量比max(类别数量) '
for i, e in enumerate(num_gt_instances_per_class2):
    if i in zero_arr:
        continue
    line5 = line5 + str(e / max(num_gt_instances_per_class2)) + ' '

all = line1 + '\n' + line2 + '\n' + line3 + '\n\n' + line1 + '\n' + line4 + '\n\n' + line1 + '\n' + line5 + '\n' + line4

with open("all.txt", "w") as f:
    f.write(all)
