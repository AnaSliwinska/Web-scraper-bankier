from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv
import time


def parse_page(page_url):
    print(f'Pracuje nad stroną: {page_url}.')
    page_response = get(page_url)
    bs = BeautifulSoup(page_response.content, 'html.parser')
    articles = bs.find_all('div', class_='article')
    print(f"\tFound {len(articles)} articles.")
    for article in articles:
        date = article.find('div', class_='entry-meta').get_text().strip()
        text = article.find('span', class_='entry-title').get_text().strip()

        cursor.execute('INSERT INTO bankier2 VALUES (?, ?, ?)', (text, name, date))
        #time.sleep(40)

    db.commit()

db = sqlite3.connect('dane.db')
cursor = db.cursor()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE bankier2 (content TEXT, company_name TEXT, publication_date DATE)''')

names = ['BAHOLDING', 'BBIDEV', 'BOOMBIT', 'BETACOM', 'BEDZIN', 'BENEFIT', 'HANDLOWY', 'BIK', 'BIOTON', 'PBKM', 'BUMECH',
         'BIOMEDLUB', 'BNPPPL', 'BOWIM', 'BRASTER', 'BERLING', 'BORYSZEW', 'BEST', 'INTERCARS', 'CCENERGY', 'CDRL',
          'CEZ', 'CFI', 'CIGAMES', 'COALENERG', 'CLNPHARMA', 'COMP', 'NOWAGALA', 'CNT',
         'COGNOR', 'CAPITAL', 'CELTIC', 'CPGROUP', 'COMPERIA', 'CORMAY', 'CITYSERV', 'CZTOREBKA', 'DADELO-PDA',
         'DATAWALK', 'DEBICA', 'DECORA', 'DEKPOL', 'DELKO', 'DGA', 'DINOPL', 'DOMDEV', 'DROZAPOL', 'DREWEX', 'DIGITREE', 'DEVELIA',
         'ESOTIQ', 'AMREST', 'EDINVEST', 'EKOEXPORT', 'EFEKT', 'EUROHOLD', 'ELKOP', 'ELBUDOWA', 'ELEKTROTI', 'ELZAB',
         'EMCINSMED', 'ELEMENTAL', 'ENELMED', 'ENERGOINS', 'ENAP', 'ENTER', 'ERG', 'ESTAR', 'EUROTEL',
         'EUCO', 'FEERUM', 'FERRUM', 'FASTFIN', 'FENGHUA', 'FAMUR', 'FMG', 'FON', 'FERRO', 'FASING', 'FORTE', 'GETBACK',
         'GROCLIN', 'GAMFACTOR', 'IMMOBILE', 'GLCOSMED', 'GOBARTO', 'GAMEOPS', 'GOVENA', 'GRODNO',
         'HYDROTOR', 'HELIO', 'HOLLYWOOD', 'HMINWEST', 'HARPER', 'HERKULES', 'I2DEV', 'IALBGR', 'IBSM', 'MEDINICE', 'INDYGO', 'IDMSA',
         'IFCAPITAL', 'IFIRMA', 'IFSA', 'IIAAV', 'IMCOMPANY', 'IMPERA', 'IMS', 'INC', 'INTERFERI', 'INSTALKRK', 'INTROL',
         'INPRO', 'INVISTA', 'IPOPEMA', 'PROVIDENT', 'IMPEL', 'INTERSPPL', 'INTERAOLT', 'INTERBUD', 'ITMTRADE', 'IZOBLOK', 'IZOLACJA',
         'IZOSTAL', 'JJAUTO', 'JWCONSTR', 'JWWINVEST', 'K2INTERNT', 'KANIA', 'KBDOM', 'KRAKCHEM', 'KCI', 'KDMSHIPNG', 'KERNEL',
          'KGL', 'KOGENERA', 'KOMPAP', 'KOMPUTRON', 'KPPD', 'KINOPOL', 'KREC', 'KREDYTIN', 'KRKA', 'KSGAGRO', 'KRUSZWICA',
          'KRVITAMIN', 'LABOPRINT', 'LIBET', 'LUBAWA', 'LENA', 'LOKUM', 'LARK', 'LARQ', 'LSISOFT', 'LENTEX',
         'LIVECHAT', 'BOGDANKA', 'MABION', 'MAKARONPL', 'MOBRUK', 'MBWS', 'MCI', 'MEDIACAP', 'MERCOR', 'MEDICALG', 'MDIENERGIA',
         'MEGARON', 'MEXPOLSKA', 'MFO', 'MANGATA', 'MIRACULUM', 'MLPGROUP', 'MILKILAND', 'MLSYSTEM', 'MENNICA', 'MOJ',
         'MOL', 'MONNARI', 'MASTERPHA', 'MIRBUD', 'MERCATOR', 'MOSTALPLC', 'MOSTALWAR', 'MOSTALZAB', 'MARVIPOL', 'MWTRADE',
         'MAXCOM', 'MUZA', 'NETIA', 'NEUCA', 'NANOGROUP', 'NTTSYSTEM', 'NOVATURAS', 'PANOVA', 'NOVAVISGR', 'NOVITA', 'NEWAG',
         'NEXITY', 'OAT', 'ORZBIALY', 'ODLEWNIE', 'OEX', 'OPENFIN', 'ORCOGROUP', 'OPTEAM', 'OPONEO.PL', 'OTMUCHOW',
         'OTLOG', 'OVOSTAR', 'PATENTUS', 'PBSFINANSE', 'PBG', 'PEKABEX', 'POLICE', 'PCFGROUP', 'PCGUARD', 'PCCROKITA', 'PCCEXOL',
         'PRAIRIE', 'PEMANAGER', 'PHOTON', 'PEP', 'PEIXIN', 'PMPG', 'PGO', 'PHN', 'PHARMENA', 'PLATYNINW',
         'PROJPRZEM', 'PLAYWAY', 'PLASTBOX', 'PLAZACNTR', 'PRIMAMODA', 'PAMAPOL',
         'POZBUD', 'PEPEES', 'PROCAD', 'PRAGMAFA', 'PRAGMAINK', 'PROCHEM', 'PROTEKTOR', 'PGSSOFT', 'PRIMETECH', 'ZPUE', 'PUNKPIRAT',
         'PURE', 'POLWAX','QUANTUM', 'QUERCUS', 'R22', 'RAFAMET', 'RAINBOW', 'RADPOL', 'REDAN', 'REGNON',
         'RESBUD', 'RAFAKO', 'REINHOLD', 'RELPOL', 'REMAK', 'REINO', 'RANKPROGR', 'RONSON', 'ROPCZYCE', 'RYVU', 'RAWLPLUG',
          'SEKO', 'SELENAFM', 'SERINUS', 'SESCOM', 'SILVANO', 'SFINKS', 'SYGNITY', 'SADOVAYA', 'SOHODEV', 'STARHEDGE',
         'SNIEZKA', 'SKARBIEC', 'SKYLINE', 'SKOTAN', 'SELVITA', 'SLEEPZAG', 'SIMPLE', 'SANOK', 'SYNEKTIK', 'SANWIL', 'SUNEX',
         'SOLAR', 'SONEL', 'SOPHARMA', 'SANPL', 'STALPROFI', 'STALPROD', 'STALEXP', 'SUWARY', 'SILVAIR-REGS', 'SWISSMED',
         'SECOGROUP', 'TARCZYNSKI', 'TBULL', 'TSGAMES', 'TIM', 'TALEX', 'TATRY', 'TALANX', 'TOYA', 'TORPOL', 'TOWERINVT',
         'TRITON', 'TRAKCJA', 'TRANSPOL', 'TERMOREX', 'TESGAS', 'TXM', 'UNIMA', 'UNICREDIT', 'ULTGAMES', 'ULMA', 'UNIBEP', 'UNIMOT',
         'URSUS', 'VIGOSYS', 'VINDEXUS', 'VOTUM', 'VOXEL', 'VRG', 'VENTUREIN', 'VISTAL', 'VIVID', 'WASKO', 'WIKANA', 'WINVEST',
         'WIELTON', 'WOJAS', 'WIRTUALNA', 'WORKSERV', 'WITTCHEN', 'WAWEL', 'WARIMPEX', 'XTB', 'XTPL', 'YOLO', 'PULAWY', 'ZEPAK',
         'ZAMET', 'ZREMB', 'ZASTAL', 'ZUE', 'STAPORKOW', 'ZYWIEC']

for name in names:
    URL = f'https://www.bankier.pl/gielda/notowania/akcje/{name}/wiadomosci/'

    for page_number in range(1, 24):
        page_url = f'{URL}{page_number}'
        parse_page(page_url)
        time.sleep(4)



db.close()
