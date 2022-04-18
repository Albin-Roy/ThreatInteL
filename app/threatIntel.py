from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from rich import print
from rich.table import Table
from rich.console import Console
from datetime import date



def circl():
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    driver.get("https://cve.circl.lu/")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)

    id = driver.find_elements_by_xpath('//table[@id="CVEs"]/tbody/tr/td[2]')
    cvss = driver.find_elements_by_xpath('//table[@id="CVEs"]/tbody/tr/td[3]')
    summary = driver.find_elements_by_xpath('//table[@id="CVEs"]/tbody/tr/td[4]')
    last_update = driver.find_elements_by_xpath('//table[@id="CVEs"]/tbody/tr/td[5]')
    published = driver.find_elements_by_xpath('//table[@id="CVEs"]/tbody/tr/td[6]')
    
    table = Table(title="cve.circl.lu",title_style="red", show_header=True,show_lines=True, header_style="bold magenta")
    table.add_column("NO.", style="dim")
    table.add_column("ID", style="dim")
    table.add_column("CVSS")
    table.add_column("Summary", justify="left")
    table.add_column("Last (major) update", justify="left")
    table.add_column("Published", justify="left") 
    
    h = 1
    for (i,j,k,l,m) in zip(id,cvss,summary,last_update,published):
        table.add_row("[cyan]"+str(h)+"[/cyan]", "[red]"+i.text+"[/red]", j.text, k.text, l.text, m.text)
        h+=1
    
    console = Console()
    console.print(table)
    print("\n \n \n")
    driver.quit()



def nist():
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    driver.get("https://nvd.nist.gov/")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)

    id = driver.find_elements_by_xpath('//ul[@id="latestVulns"]/li/div/p/strong/a')
    summary = driver.find_elements_by_xpath('//ul[@id="latestVulns"]/li/div[1]/p')
    cvss_1 = driver.find_elements_by_xpath('//ul[@id="latestVulns"]/li/div[2]/p/span[1]/a')
    cvss_2 = driver.find_elements_by_xpath('//ul[@id="latestVulns"]/li/div[2]/p/span[2]/a')
    
    table = Table(title="nvd.nist.gov",title_style="red",show_header=True,show_lines=True, header_style="bold magenta")
    table.add_column("NO.", style="dim")
    table.add_column("ID", style="dim")
    table.add_column("Summary", justify="left")
    table.add_column("CVSS_v3.1")
    table.add_column("CVSS_v2.0")
    
    h = 1
    for (i,j,k,l) in zip(id,summary,cvss_1,cvss_2):
        table.add_row("[cyan]"+str(h)+"[/cyan]", "[red]"+i.text+"[/red]", j.text, k.text, l.text)
        h+=1
    
    console = Console()
    console.print(table)
    print("\n \n \n")
    driver.quit()


def CertInVuln():
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    todays_date = date.today()
    year = (str(todays_date.year))
    driver.get("https://cert-in.org.in/s2cMainServlet?pageid=VLNLIST02&year=" +year+"")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)

    id = driver.find_elements_by_xpath('//td[@class="contentTD"]/li/a/span')
    summary = driver.find_elements_by_xpath('//td[@class="contentTD"]/div/span')
    published = driver.find_elements_by_xpath('//td[@class="contentTD"]/span')

    table = Table(title="cert-in.org.in - VULNERABILITIES",title_style="red",show_header=True,show_lines=True, header_style="bold magenta")
    table.add_column("NO.", style="dim")
    table.add_column("ID", style="dim")
    table.add_column("Summary", justify="left")
    table.add_column("Published", justify="left") 
    
    h = 1
    for (i,j,k) in zip(id,summary,published):
        table.add_row("[cyan]"+str(h)+"[/cyan]", "[red]"+i.text+"[/red]", j.text, k.text)
        h+=1
    
    console = Console()
    console.print(table)
    print("\n \n \n")

    driver.quit()


def CertInAdv():
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    todays_date = date.today()
    year = (str(todays_date.year))
    driver.get("https://cert-in.org.in/s2cMainServlet?pageid=PUBADVLIST02&year=" +year+"")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)

    id = driver.find_elements_by_xpath('//span[@class="verblue2"]')
    summary = driver.find_elements_by_xpath('//td[@class="content"]')
    published = driver.find_elements_by_xpath('//span[@class="contentTD,DateContent"]')

    table = Table(title="cert-in.org.in - ADVISORIES",title_style="red",show_header=True,show_lines=True, header_style="bold magenta")
    table.add_column("NO.", style="dim")
    table.add_column("ID", style="dim")
    table.add_column("Summary", justify="left")
    table.add_column("Published", justify="left") 
    
    h = 1
    for (i,j,k) in zip(id,summary,published):
        table.add_row("[cyan]"+str(h)+"[/cyan]", "[red]"+i.text+"[/red]", j.text, k.text)
        h+=1

    element1 = driver.find_element_by_xpath('//a[@href="/Advisories.jsp?next=15"]')
    element1.click()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)

    id = driver.find_elements_by_xpath('//span[@class="verblue2"]')
    summary = driver.find_elements_by_xpath('//td[@class="content"]')
    published = driver.find_elements_by_xpath('//span[@class="contentTD,DateContent"]')

    for (i,j,k) in zip(id,summary,published):
        table.add_row("[cyan]"+str(h)+"[/cyan]", "[red]"+i.text+"[/red]", j.text, k.text)
        h+=1
    
    console = Console()
    console.print(table)


    driver.quit()



circl()
nist()
CertInVuln()
CertInAdv()

