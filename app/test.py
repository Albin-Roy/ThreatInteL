from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from rich import print
from rich.table import Table
from rich.console import Console
from datetime import date




def CertIn():
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


CertIn()

