import shutil
import time

file_time = time.strftime("%d-%m-%Y-%H;%M;%S")
file_name = "person." + file_time
original = "C:\SSIS\Integration_Services_Project3\person.txt"

copied = f"C:\SSIS\Integration_Services_Project3\{file_name}.txt"

shutil.copy(original, copied)