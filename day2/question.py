__author__ = "tremor"

list1 = ["dog", "cat", "got", "toe"]
input_string = "dogotoe"
output_string = ""

# for i in list1:
# 	if i in input_string:
# 		output_string += str(i + " ")
		
	
# print(output_string)

# 
for i in range(len(input_string)):
	for j in range(i+1, len(input_string) + 1):
		if input_string[i:j] in list1:
			output_string += input_string[i:j] + " "


print(output_string)


