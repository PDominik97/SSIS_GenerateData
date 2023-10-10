import shutil
import time

file_time = time.strftime("%d-%m-%Y-%H;%M;%S")
file_name = "person." + file_time
original = "C:\\SSIS\\SSIS_GenerateData\\person.txt"

copied = f"C:\\SSIS\\SSIS_GenerateData\\{file_name}.txt"

shutil.copy(original, copied)