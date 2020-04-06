from bs4 import BeautifulSoup

def beautify(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def getTable(soup):
    table = soup.find(id="main_table_countries_today")
    return table


colNames = ["place", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_recovered", "active_cases", "serious_critical", "total_cases_per_million", "deaths_per_millon", "total_tests", "tests_per_million"]

def parseCell(text):
    if(type(text) == type(None)): return None
    try:
        stripped = text.replace(",","").replace("+","").replace(" ", "")
    except TypeError as e:
        print(text)
        raise e
    if (stripped == ""):
        return None
    if (stripped.isdigit()):
        return int(stripped)
    else:
        return stripped


def getValuesFromRows(tr):
    cells = tr.findAll("td")
    obj = {}
    for i in range(1, 12):
        cellVal = parseCell(cells[i].text)
        if (cellVal != None): obj[colNames[i]] = cellVal
    return (cells[0].text, obj)

def parseTable(table):
    [headers, total_row, *rows, total] = table.findAll("tr")
    cells = rows[-1].findAll("td")
    allData = {}
    for row in rows:
        [place, data] = getValuesFromRows(row)
        allData[place] = data
    return allData
