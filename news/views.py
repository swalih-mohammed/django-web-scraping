from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from BBC Arabic

bbc_r = requests.get("https://www.bbc.com/arabic")
bbc_soup = BeautifulSoup(bbc_r.content, 'html5lib')
bbc_headings = bbc_soup.find_all('h3')
bbc_news = []
for th in bbc_headings:
    bbc_news.append(th.text)
bbc_news = bbc_news[:5]

# GEtting news from BBC Arabic

cnn_r = requests.get("https://arabic.cnn.com/")
cnn_soup = BeautifulSoup(cnn_r.content, 'html5lib')
cnn_headings = cnn_soup.find_all('h3')
cnn_news = []
for th in cnn_headings:
    cnn_news.append(th.text)
cnn_news = cnn_news[:5]

# GEtting news from aljazeera Arabic

aj_r = requests.get("https://www.aljazeera.net/")
aj_soup = BeautifulSoup(aj_r.content, 'html5lib')
aj_headings = aj_soup.find_all('h3')
aj_news = []
for th in aj_headings:
    aj_news.append(th.text)
aj_news = aj_news[:5]

# GEtting arabic jobs

nk_r = requests.get("https://www.monsterindia.com")
nk_soup = BeautifulSoup(nk_r.content, 'html5lib')
nk_headings = nk_soup.find_all('div')
print(nk_headings)
# nk_jobs = []
# for th in nk_headings:
#     nk_jobs.append(th.text)
# nk_jobs = nk_jobs[:5]
nk_jobs = nk_headings

# root > div.search-result-container > div.content > section.listContainer.fleft > div.list > article:nth-child(4) > div.jobTupleHeader > div.info.fleft > a
# root > div.search-result-container > div.content > section.listContainer.fleft > div.list > article:nth-child(4) > div.jobTupleHeader

# <a class="title fw500 ellipsis" href="https://www.naukri.com/job-listings-hr-service-center-specialist-arabic-language-expert-halliburton-off-shore-services-inc-pune-0-to-5-years-071220001528?src=seo_srp&amp;sid=1603563323094445_1&amp;xp=3&amp;px=1" title="HR Service Center Specialist - Arabic Language Expert" target="_blank">HR Service Center Specialist - Arabic Language Expert</a>


def index(req):
    return render(req, 'news/index1.html', {'bbc_news': bbc_news, 'cnn_news': cnn_news, 'aj_news': aj_news, 'nk_jobs': nk_jobs})
