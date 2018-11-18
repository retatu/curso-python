import re

def find_all(string, patterns):
    for pattern in patterns:
        print("Pattern %s" % (pattern))
        todos_matches = re.findall(pattern, string)
        print(todos_matches)
    print()

patterns = ['termo1', 'termo2']
string = 'Esta string tem dois termos. termo1 e termo3'
r = re.search(patterns[0], string)
print(r)
find_all(string, patterns)

match = re.search(patterns[0], string)
#start e fim do match
print('Start: ', match.start(), ' Fim ', match.end())

string = 'sdsds...sd.sd.sdds.ds.dss.s.dd.sdd..sd.sd.sd.sddd.'
patterns = ['sd', 'sd*', 'sd+', 'sd?', 'sd{3}', 'sd{2,3}']
find_all(string, patterns)

string = 'sdds..sddsd.sd.ds.dsds.dsd.dssd'
patterns = ['[sd]', 's[sd]+']
find_all(string, patterns)

string = 'Texto com pontuações! Como nós removemo-as? Ponto . Virgulas,'
patterns = ['[^!.? ]+']
find_all(string, patterns)

string = 'Texto aleatório com letras minusculas e MAIUSCULAS'
patterns = ['[a-z]+', '[A-Z]+', '[a-zA-Z]+', '[A-Z][a-z]+']
find_all(string, patterns)