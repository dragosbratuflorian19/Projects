import random

gk = ['De gea', 'Ederson', 'Alison', 'Kepa', 'Leno', 'Lloris', 'Schmeichel',
      'Courtois', 'Ter Stegen', 'Oblak',
      'Neuer', 'Burki',
      'Buffon', 'Handanovic', 'Ospina',
      'Navas'
      ]

lb = ['Shaw', 'Mendy', 'Robertson', 'Emerson', 'Kolasinac', 'Rose', 'Chilwell',
      'Marcelo', 'Alba', 'Saul',
      'Alaba', 'Schulz',
      'Alex Sandro', 'Biraghi', 'Rui Mario',
      'Bernat'
      ]

rb = ['Wan Bissaka', 'Walker', 'Arnold', 'Azpilicueta', 'M. Niles', 'Aurier', 'Ricardo',
      'Carvajal', 'Semedo', 'Trippier',
      'Kimmich', 'Hakimi',
      'Cuadrado', "D'Ambrosio", 'Di Lorenzo',
      'Meunier'
      ]
cb = ['Maguire', 'Lindelof',
      'Stones', 'Laporte',
      'Van Dijk', 'Matip',
      'Rudiger', 'Zouma',
      'Chambers', 'Sokratis',
      'Alderweireld', 'Vertonghen',
      'Soyuncu', 'Evans',
      'Ramos', 'Varane',
      'Pique', 'Langlet',
      'Felipe', 'Gimenez',
      'Sule', 'Boateng',
      'Hummels', 'Akanji',
      'De Ligt', 'Bonucci',
      'Godin', 'De Vrij',
      'Koulibaly', 'Manolas',
      'Silva', 'Marquinhos'
      ]
df = lb + cb + rb

mf = ['Pogba', 'McTominay', 'Fred',
      'De Bruyne', 'Gundogan', 'Bernardo',
      'Henderson', 'Fabinho', 'Wijnaldum',
      'Kovacic', 'Jorginho', 'Kante',
      'Ozil', 'Torreira', 'Guendouzi',
      'Lucas', 'Eriksen', 'Dier',
      'Madison', 'Barnes', 'Ayoze',
      'Casemiro', 'Kross', 'Modric',
      'De Jong', 'Rakitic', 'Busquets',
      'Koke', 'Correa', 'Thomas',
      'Coman', 'Coutinho', 'Alcantara',
      'Gotze', 'Witsel', 'Brandt',
      'Pjanic', 'Ramsey', 'Matuidi',
      'Brozovic', 'Sensi', 'Borja Valero',
      'Zielinski', 'Allan', 'Fabian Ruiz',
      'Di Maria', 'Verratti', 'Draxler'
      ]

fw = ['Rashford', 'Martial', 'Dan James',
      'Aguero', 'Sterling', 'Mahrez',
      'Salah', 'Mane', 'Firmino',
      'Pulisic', 'Abraham', 'Willian',
      'Pepe', 'Lacazette', 'Aubameyang',
      'Alli', 'Son', 'Kane',
      'Tielemans', 'Vardy', 'Iheanacho',
      'Benzema', 'Bale', 'Hazard',
      'Suarez', 'Messi', 'Griezmann',
      'Morata', 'Costa', 'J. Felix',
      'Lewandowski', 'Gnabry', 'Muller',
      'Sancho', 'Reus', 'T. Hazard',
      'Ronaldo', 'Dybala', 'Higuain',
      'Lautaro', 'Lukaku', 'Sanchez',
      'Mertens', 'Milik', 'Insigne',
      'Mbappe', 'Neymar', 'Icardi'
      ]

teams = ['Manchester United', 'Manchester City', 'Liverpool', 'Chelsea', 'Arsenal', 'Tottenham', 'Leicester',
         'Real Madrid', 'Barcelona', 'Atletico Madrid',
         'Bayern Munchen', 'Dortmund',
         'Juventus', 'Inter Milan', 'Napoli',
         'PSG']

list_of_positions = [gk, lb, cb, rb, mf, fw]
for i in list_of_positions:
      random.shuffle(i)

# for team in teams:
#     squad = {'gk':[gk.pop()],
#              'rb':[rb.pop()],
#              'cb':[cb.pop(), cb.pop()],
#              'lb':[lb.pop()],
#              'cm':[mf.pop(), mf.pop(),mf.pop()],
#              'fw':[fw.pop(), fw.pop(), fw.pop()],
#              }
#     print(f'{team:>25}')
#     print(*squad['gk'])
#     print(*squad['rb'],*squad['cb'],*squad['lb'])
#     print(*squad['cm'])
#     print(*squad['fw'])
#     print('-'*40)

# 1,Ronaldo,Juventus,95,3500000


with open('football_players.txt', 'w') as file:
      for player in df:
            file.write(f'{random.randint(80,99)},{random.randint(40,65)},{random.randint(30,55)},defender,{player}\n')
      for player in mf:
            file.write(f'{random.randint(40,83)},{random.randint(80,99)},{random.randint(50,83)},midfielder,{player}\n')
      for player in fw:
            file.write(f'{random.randint(30,45)},{random.randint(55,82)},{random.randint(80,99)},striker,{player}\n')
with open('football_players.txt', 'r') as w:
      print(w.read())
