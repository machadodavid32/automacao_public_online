# Com vender acesso ao meu software
# 1. Desenvolvendo o software
# 2. Fornecer o download do software
# 3. Solicitar informações de acesso(licença)

import random, os

fonte = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
licencas_geradas = 0
quantas_licencas = int(input('Quantas licenças devem ser geradas?'))
licencas = []

while licencas_geradas <= quantas_licencas:
    licenca = f'{random.choices(fonte,k=5)}-{random.choices(fonte,k=5)}-{random.choices(fonte,k=5)}-{random.choices(fonte,k=5)}-{random.choices(fonte,k=5)}'
    licenca_limpa = licenca.replace('[', '').replace("'", "").replace(',', '').replace(']', '').replace(' ', '')
    licencas_geradas += 1
    licencas.append(licenca_limpa)
    
    with open('licenças.txt','w', newline='') as arquivo:
        arquivo.writelines(os.linesep.join(licencas))
        
    print('Finalizado')
    
    
    