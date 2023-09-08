import os
import pandas as pd

path = os.listdir('/home/thais/Área de Trabalho/Doc/cemitool/cemitool_results/')


development_cardiac_tissue = ['Go_muscle_structure_development', 'Go_trabecula_formation', 'Go_cariocyte_differentiation', 'Go_cardiac_cell_development', 
'Go_blood_vessel_morphogenesis', 'Go_angiogenesis', 'Go_vasculature_development', 'Go_vasculogenesis', 'Go_cardiac_muscle_cell_differentiation','Go_ventricular_cardiac_muscle_cell_differentiation']

mitochondrial_processes = ['Go_mitochondrial_matrix', 'Go_mitochondrial_protein_complex', 'Go_mitochondrial_translation']

cardiac_functioning = ['Go_heart_contraction', 'Go_blood_circulation', 'Go_cardiac_conduction', 'Go_response_to_cadmium_ion', 'Go_heart_process', 'Go_regulation_of_muscle_contraction', 'Go_muscle_contraction']

circulatory_functioning = ['Go_platelet_alpha_granule', 'Go_negative_regulation_of_response_to_wounding', 'Go_positive_regulation_of_response_to_wounding','Go_regulation_of_response_to_wounding', 'Go_circulatory_system_process']

df_circulatory_functioning = pd.DataFrame(columns=['File', 'Module', 'ID', 'Description', 'GeneRatio', 'BgRatio', 'pvalue', 'p.adjust', 'qvalue', 'geneID', 'Count'])
df_cardiac_functioning = pd.DataFrame(columns=['File', 'Module', 'ID', 'Description', 'GeneRatio', 'BgRatio', 'pvalue', 'p.adjust', 'qvalue', 'geneID', 'Count'])
df_mitochondrial_processes = pd.DataFrame(columns=['File', 'Module', 'ID', 'Description', 'GeneRatio', 'BgRatio', 'pvalue', 'p.adjust', 'qvalue', 'geneID', 'Count'])
df_development_cardiac_tissue = pd.DataFrame(columns=['File', 'Module', 'ID', 'Description', 'GeneRatio', 'BgRatio', 'pvalue', 'p.adjust', 'qvalue', 'geneID', 'Count'])


for i in path:
	
	arquivo = open('/home/thais/Área de Trabalho/Doc/cemitool/cemitool_results/'+ i + '/ora.tsv', 'r')

	for line in arquivo:
		line = line[:-1]
		linha = line.replace('"', "").split('\t')
		
		if(linha[1] in circulatory_functioning):

			df_circulatory_functioning = df_circulatory_functioning.append({'File': i, 'Module': linha[0], 'ID': linha[1], 'Description' : linha[2], 'GeneRatio' : linha[3],
			 'BgRatio': linha[4], 'pvalue': linha[5], 'p.adjust': linha[6], 'qvalue': linha[7], 'geneID': linha[8], 'Count': linha[9]}, ignore_index=True)

		elif(linha[1] in cardiac_functioning):
			
			df_cardiac_functioning = df_cardiac_functioning.append({'File': i, 'Module': linha[0], 'ID': linha[1], 'Description' : linha[2], 'GeneRatio' : linha[3],
			 'BgRatio': linha[4], 'pvalue': linha[5], 'p.adjust': linha[6], 'qvalue': linha[7], 'geneID': linha[8], 'Count': linha[9]}, ignore_index=True)


		elif(linha[1] in mitochondrial_processes):
			
			df_mitochondrial_processes = df_mitochondrial_processes.append({'File': i, 'Module': linha[0], 'ID': linha[1], 'Description' : linha[2], 'GeneRatio' : linha[3],
			 'BgRatio': linha[4], 'pvalue': linha[5], 'p.adjust': linha[6], 'qvalue': linha[7], 'geneID': linha[8], 'Count': linha[9]}, ignore_index=True)


		elif(linha[1] in development_cardiac_tissue):

			df_development_cardiac_tissue = df_development_cardiac_tissue.append({'File': i, 'Module': linha[0], 'ID': linha[1], 'Description' : linha[2], 'GeneRatio' : linha[3],
			 'BgRatio': linha[4], 'pvalue': linha[5], 'p.adjust': linha[6], 'qvalue': linha[7], 'geneID': linha[8], 'Count': linha[9]}, ignore_index=True)
		



PATH = '/home/thais/Área de Trabalho/Doc/cemitool/'

#df_circulatory_functioning.drop_duplicates(keep='first', inplace = True)
df_circulatory_functioning.to_csv(PATH + 'df_circulatory_functioning.tsv', index = False, quoting=None)
print(len(df_circulatory_functioning))

#df_cardiac_functioning.drop_duplicates(keep='first', inplace = True)
df_cardiac_functioning.to_csv(PATH + 'df_cardiac_functioning.tsv', index = False, quoting=None)
print(len(df_cardiac_functioning))

#df_mitochondrial_processes.drop_duplicates(keep='first', inplace = True)
df_mitochondrial_processes.to_csv(PATH + 'df_mitochondrial_processes.tsv', index = False, quoting=None)
print(len(df_mitochondrial_processes))

#df_development_cardiac_tissue.drop_duplicates(keep='first', inplace = True)
df_development_cardiac_tissue.to_csv(PATH + 'df_development_cardiac_tissue.tsv', index = False, quoting=None)
print(len(df_development_cardiac_tissue))