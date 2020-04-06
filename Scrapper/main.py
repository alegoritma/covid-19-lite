from fetcher import fetch
from worldo_parser import parseTable, getTable, beautify
from UpdateData import updateData

if __name__ == "__main__":
    print("Fetching...")
    res = fetch()
    print("Fetched!")
    print("Parsing data...")
    soup = beautify(res)
    table = getTable(soup)
    tableArr = parseTable(table)
    print("Parsed!")
    print("Updating database...")
    doc_id = updateData(u"main", tableArr, u"total")
    print("Done!")
