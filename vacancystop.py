import re

vacancies = []
patternTypeID = 'vacancy_id":"\d*'
patternID = 'vacancy_id":"'

for line in open('error1.log'):
	L = str(line)
	forVac = re.search(patternTypeID,L)
	if forVac != None:
	    rowVacID = str(forVac.group())
	vacID = rowVacID.replace(patternID, '')
	if vacID != '':
	    vacancies.append(vacID)
	
uniqVacancies = list(set(vacancies)) # убираем неуникальные номера вакансий

output = open(r'todel.html', 'w')
for line in uniqVacancies:
    #print(line)
	output.write('<a href="http://rdw.ru/partner/manager/vacancy/'+line+'" target="_blank">'+line+'</a> ')

