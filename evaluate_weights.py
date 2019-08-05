# ----------------------Parameters to modify----------------------
t_file = open("./data/news.test", "r")
w_file = open("./output/test_results.tsv", "r")
o_file = open("./output/weights_result.txt", "w")
seq_length = 128

# ----------------------Run----------------------

text_list = []

for line in t_file.readlines():
    s_data = line.strip().split("\t")
    text = s_data[1].strip().replace(" ", "").replace("\t", "").replace("　", "")
    temp = []
    temp.append(["[CLS]"])
    for char in text[0:(seq_length-2)]:
        temp.append([char])
    temp.append(["[SEP]"])
    text_list.append(temp)

n = 0

for line in w_file.readlines():
    s_data = line.strip().split("|")
    weights = s_data[-1].strip().split(",")
    for each, w in zip(text_list[n], weights):
        each.append(float(w))
    n += 1

for item in text_list:
    item = sorted(item, key=lambda x: x[1], reverse=True)
    for char in item:
        o_file.write("{}\t{}\n".format(char[0], char[1]))
    o_file.write("--------------------------\n")

