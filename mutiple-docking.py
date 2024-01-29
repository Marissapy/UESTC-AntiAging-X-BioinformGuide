import glob
import os
import subprocess

# 获取当前目录下的所有pdbqt文件
pdbqt_files = glob.glob('*.pdbqt')

# 确保结果文件夹存在
results_folder = 'results'
if not os.path.exists(results_folder):
	os.makedirs(results_folder)

# Vina命令的基本部分
vina_command_base = "vina --ligand={} --config=config.txt"

# 追踪当前处理的文件编号
file_number = 0

for file in pdbqt_files:
	file_number += 1  # 增加文件编号
	print(f"Processing file {file_number}/{len(pdbqt_files)}: {file}")
	# 构建结果文件的路径
	output_file = os.path.join(results_folder, file + '_result.txt')
	# 检查结果文件是否已存在
	if not os.path.exists(output_file):
		# 构建完整的Vina命令
		vina_command = vina_command_base.format(file)
		# 运行Vina命令并捕获输出
		results = subprocess.run(vina_command.split(), capture_output=True, text=True)
		# 将输出保存到文件
		with open(output_file, 'w') as f:
		f.write(results.stdout)
	else:
		print(f"Results already exist for {file}, skipping...")
		
print("Processing complete.")
