import zipfile

total= 0

with zipfile.ZipFile("sample.zip", 'r') as zip_file:
    file_list = zip_file.namelist()

    for file_name in file_list:
       
        if file_name.endswith("_kgu.txt") and int(file_name.split("_")[1]) % 2 != 0:
         
            with zip_file.open(file_name) as file:
                numbers = int(file.readline())
                total += numbers

print("Answer:", total)