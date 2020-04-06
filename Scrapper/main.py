import time, signal
from datetime import timedelta
from fetcher import fetch
from worldo_parser import parseTable, getTable, beautify
from UpdateData import updateData
from Job import signal_handler, Job, ProgramKilled




WAIT_TIME_SECONDS = 60*5



def main():
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
    print(time.ctime())

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=main)
    job.start()

    while True:
      try:
          time.sleep(1)
      except ProgramKilled:
          print("Program killed: running cleanup code")
          job.stop()
          break
