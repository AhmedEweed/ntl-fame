from lxml import html
import requests
import re, os, glob, shutil
import pandas as pd


page = requests.get('http://techleaders.eg/wall-of-fame/')
tree = html.fromstring(page.content)

tracks = [re.sub('[\t|\r|/|\n]', '', n) for n in tree.xpath('//span[@class="ac_title_class"]/text()')]

numbers = [re.sub('[^0-9]','', i) for i in tree.xpath('//table/@id')]

track_dict = dict(zip(numbers, tracks))
ids = []
names = []
govs = []
trks = []

try:
    os.mkdir('data')
    os.chdir('data')
except:
    os.chdir('data')

for k, v in track_dict.items():
    ids = tree.xpath("//table[@id='tablepress-"+str(k)+"']//tr"+"/td[@class='column-1']/text()")
    names = tree.xpath("//table[@id='tablepress-"+str(k)+"']//tr"+"/td[@class='column-2']/text()")
    govs = tree.xpath("//table[@id='tablepress-"+str(k)+"']//tr"+"/td[@class='column-3']/text()")
    trks = [v] * len(ids)
    df = pd.DataFrame(list(zip(ids, names, govs, trks)), columns=['InterviewId', 'Name', 'Governorate', 'Track'])
    df.to_csv(v+'.csv', index = False)

allfiles = [i for i in glob.glob('*.csv')]
pd.concat(pd.read_csv(f) for f in allfiles).to_csv('ntl_data.csv', index=False, encoding='utf-8')

shutil.copy2('ntl_data.csv', '..')

os.chdir('..')

shutil.rmtree('data')

print('Scraping done perfectly!')