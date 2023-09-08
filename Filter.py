from sys import argv
import os

itemList =  os.listdir("/home/thais/Área de Trabalho/Doc/Expression_Matrix/Cuffnorm_updated/")
#itemList.remove("Filter.py")
itemList.remove("Filtered_Expressions")
#itemList = ["277R_279R_Cuffnorm.txt"]

for item in itemList:
	arquivo = open("/home/thais/Área de Trabalho/Doc/Expression_Matrix/Cuffnorm_updated/" + str(item), "r")
	output = open("/home/thais/Área de Trabalho/Doc/Expression_Matrix/Cuffnorm_updated/Filtered_Expressions/Filtered_" + str(item), "w") 

	header = arquivo.readline()
	output.writelines(header)
	head = header.split("\t")
	length = (len(head) -2)
	cells_percent = ((length * 5) / 100)

	cells_counts = 0


	for line in arquivo:
		linha = line.strip().split("\t")
		expression = linha[2:]
		ids = linha[1]
		gene_expression = list(map(float, expression))
		#print(expression)
		for i in gene_expression:

			if(i > 0.001):
				cells_counts = cells_counts + 1
			else:
				continue;

		if (cells_counts >= cells_percent):
			output.writelines(line)
			cells_counts = 0
		else:
			cells_counts = 0

