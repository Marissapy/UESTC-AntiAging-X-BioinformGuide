# -*- coding: utf-8-*-
import os
import pandas as pd
# 指定目录路径
dir_path = r"/results"
# 遍历目录及子目录下所有.log文件，并提取最小affinity值
affinities = []
for root, dirs, files in os.walk(dir_path):
	for file in files:
		if file.endswith(".txt"):
			with open(os.path.join(root, file), "r") as log_file:
				lines = log_file.readlines()
				affinity = None
				for line in lines:
					if line.startswith("   1"):
						affinity = float(line.split()[1])
						break
					if affinity is not None:
						ligand = file.split(".")[0]
						affinities.append((ligand, affinity))
# 将数据存储到Pandas数据框中
df = pd.DataFrame(affinities, columns=["Ligand", "Affinity"])

# 将数据框输出为CSV文件
df.to_csv("results/affinities.csv", index=False)
print("done")
