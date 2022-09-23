#Creates text file letter using ./Input/Letters/starting_letter.txt
#for each name in ./Input/Names/invited_names.txt
#Replaces the [name] placeholder at letter with the actual name from invited_names.txt
#Save the letters in the folder Ouput /  "ReadyToSend".
    


with open('./Input/Letters/starting_letter.txt','r') as file:
    s_letter = file.read()

print(s_letter)

with open('./Input/Names/invited_names.txt','r') as file:
    name_list_raw = file.readlines()

print(name_list_raw)
name_list = []
for item in name_list_raw:
    name_list.append(item.strip('\n'))
print(name_list)

for name in name_list:
    final_letter = s_letter.replace('[name]',name)
    print(final_letter)
    path_name = f"./Output/ReadyToSend/{name}"
    print(path_name)
    with open(path_name,'w') as file:
        file.write(final_letter)

