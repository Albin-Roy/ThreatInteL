from bs4 import BeautifulSoup
from lxml import etree
import requests, urllib3, re
from rich import print
from rich.table import Table
from rich.console import Console
from datetime import date




def clean(value):
    rep = []
    list_of_char = ['\n', '\t', '\r']
    pattern = '[' + ''.join(list_of_char) + ']'
    for x in value:
        rep = re.sub("|".join(list_of_char), "", x)
    # rep = list(filter(None, rep))
    return rep



def rm_n(value):
    rep = []
    for x in value:
        rep.append(x.replace("\n", ""))
    rep = list(filter(None, rep))
    return rep

def rm_t(value):
    rep = []
    for x in value:
        rep.append(x.replace("\t", ""))
    rep = list(filter(None, rep))
    return rep

def rm_r(value):
    rep = []
    for x in value:
        rep.append(x.replace("\r", ""))
    rep = list(filter(None, rep))
    return rep

def rm_space(value):
    rep = []
    for x in value:
        rep.append(x.replace("  ", ""))
    return rep







def Circl():
    webpage = requests.get('https://cve.circl.lu/')
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))

    id = dom.xpath('//table[@id="CVEs"]/tbody/tr/td[2]//text()')
    cvss = dom.xpath('//table[@id="CVEs"]/tbody/tr/td[3]//text()')
    summary = dom.xpath('//table[@id="CVEs"]/tbody/tr/td[4]//text()')
    last_update = dom.xpath('//table[@id="CVEs"]/tbody/tr/td[5]//text()')
    published = dom.xpath('//table[@id="CVEs"]/tbody/tr/td[6]//text()')

    id=rm_n(id)
    cvss=rm_n(cvss)
    summary=rm_n(summary)
    summary=rm_space(summary)
    last_update=rm_n(last_update)
    published=rm_n(published)

    table = Table(title="cve.circl.lu",title_style="red", show_header=True,show_lines=True, header_style="bold magenta")
    table.add_column("NO.", style="dim")
    table.add_column("ID", style="dim")
    table.add_column("CVSS")
    table.add_column("Summary", justify="left")
    table.add_column("Last (major) update", justify="left")
    table.add_column("Published", justify="left") 

    h = 1
    for (i,j,k,l,m) in zip(id,cvss,summary,last_update,published):
        table.add_row("[cyan]"+str(h)+"[/cyan]", "[red]"+i+"[/red]", j, k, l, m)
        h+=1

    console = Console()
    console.print(table)
    print("\n \n \n")

    #to export csv file
    # dict = { 'ID':id, 'CVSS':cvss, 'Summary':summary, 'Last (major) update':last_update, 'Published':published }
    # df = pd.DataFrame(dict)
    # df.to_csv('CVEs.csv')



def Nist():
    webpage = requests.get('https://nvd.nist.gov/')
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))

    id = dom.xpath('//ul[@id="latestVulns"]/li/div/p/strong/a//text()')
    summary = dom.xpath('//ul[@id="latestVulns"]/li/div[1]/p//text()')
    cvss_1 = dom.xpath('//ul[@id="latestVulns"]/li/div[2]/p/span[1]/a//text()')
    cvss_2 = dom.xpath('//ul[@id="latestVulns"]/li/div[2]/p/span[2]/a//text()')

    clean(summary)
    print(summary)

    table = Table(title="nvd.nist.gov",title_style="red",show_header=True,show_lines=True, header_style="bold magenta")
    table.add_column("NO.", style="dim")
    table.add_column("ID", style="dim")
    table.add_column("Summary", justify="left")
    table.add_column("CVSS_v3.1")
    table.add_column("CVSS_v2.0")
    
    h = 1
    for (i,j,k,l) in zip(id,summary,cvss_1,cvss_2):
        table.add_row("[cyan]"+str(h)+"[/cyan]", "[red]"+i+"[/red]", j, k, l)
        h+=1
    
    console = Console()
    console.print(table)
    print("\n \n \n")




def CertInVuln():
    urllib3.disable_warnings()
    todays_date = date.today()
    year = (str(todays_date.year))
    webpage = requests.get("https://cert-in.org.in/s2cMainServlet?pageid=VLNLIST02&year=" +year+"",verify=False)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))

    id = dom.xpath('//td[@class="contentTD"]/li/a/span//text()')
    summary = dom.xpath('//td[@class="contentTD"]/div/span//text()')
    published = dom.xpath('//td[@class="contentTD"]/span//text()')

    table = Table(title="cert-in.org.in - VULNERABILITIES",title_style="red",show_header=True,show_lines=True, header_style="bold magenta")
    table.add_column("NO.", style="dim")
    table.add_column("ID", style="dim")
    table.add_column("Summary", justify="left")
    table.add_column("Published", justify="left") 
    
    h = 1
    for (i,j,k) in zip(id,summary,published):
        table.add_row("[cyan]"+str(h)+"[/cyan]", "[red]"+i+"[/red]", j, k)
        h+=1
    
    console = Console()
    console.print(table)
    print("\n \n \n")

def CertInAdv():
    urllib3.disable_warnings()
    todays_date = date.today()
    year = (str(todays_date.year))
    webpage = requests.get("https://cert-in.org.in/s2cMainServlet?pageid=PUBADVLIST02",verify=False)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))

    id = dom.xpath('//span[@class="verblue2"]//text()')
    summary = dom.xpath('//td[@class="content"]//text()')
    published = dom.xpath('//span[@class="contentTD,DateContent"]//text()')

    summary = rm_n(summary)

    table = Table(title="cert-in.org.in - ADVISORIES",title_style="red",show_header=True,show_lines=True, header_style="bold magenta")
    table.add_column("NO.", style="dim")
    table.add_column("ID", style="dim")
    table.add_column("Summary", justify="left")
    table.add_column("Published", justify="left") 
    
    h = 1
    for (i,j,k) in zip(id,summary,published):
        table.add_row("[cyan]"+str(h)+"[/cyan]", "[red]"+i+"[/red]", j, k)
        h+=1
    
    console = Console()
    console.print(table)

Circl()
Nist()
CertInVuln()
CertInAdv()