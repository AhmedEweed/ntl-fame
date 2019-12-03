# import required libraries
from lxml import html
import requests
import re, os, glob, shutil
import pandas as pd

# get the page content and convert it into a tree of html
page = requests.get('http://techleaders.eg/wall-of-fame/')
tree = html.fromstring(page.content)

# get the track names
tracks = [re.sub('[\t|\r|/|\n]', '', n) for n in tree.xpath('//span[@class="ac_title_class"]/text()')]

# get the tracks corresponding table ids to use it in extracting the rest of the data
numbers = [re.sub('[^0-9]','', i) for i in tree.xpath('//table/@id')]

# make the data dictionary with tracks and correspondig class ids to make the data file 
track_dict = dict(zip(numbers, tracks))

# create empty lists to contain each column data
ids = []
names = []
govs = []
trks = []

# make a directory named `data` to contain our temporarily data file and make it the current active directory
# if the file already exists, make it the current active directory
try:
    os.mkdir('data')
    os.chdir('data')
except:
    os.chdir('data')

# loop through the data dictionary and make a file for each track name with its data
# we will acquire the data using the class id of the track name
# name the files after the track name and save them to the current directory `data`
for k, v in track_dict.items():
    ids = tree.xpath("//table[@id='tablepress-"+str(k)+"']//tr"+"/td[@class='column-1']/text()")
    names = tree.xpath("//table[@id='tablepress-"+str(k)+"']//tr"+"/td[@class='column-2']/text()")
    govs = tree.xpath("//table[@id='tablepress-"+str(k)+"']//tr"+"/td[@class='column-3']/text()")
    trks = [v] * len(ids)
    df = pd.DataFrame(list(zip(ids, names, govs, trks)), columns=['InterviewId', 'Name', 'Governorate', 'Track'])
    df.to_csv(v+'.csv', index = False)

# make a list of all csv file names
# merge all the files into one file and name it `ntl_data`
allfiles = [i for i in glob.glob('*.csv')]
pd.concat(pd.read_csv(f) for f in allfiles).to_csv('ntl_data.csv', index=False, encoding='utf-8')

# copy the newly created file `ntl_data.csv` to the parent directory
shutil.copy2('ntl_data.csv', '..')

# change directory to the parent directory
os.chdir('..')

# delete `data` folder and its contents
shutil.rmtree('data')

# print a message to signal the successful completion of the script 
print('Scraping done perfectly!')