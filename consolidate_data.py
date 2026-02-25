#!/usr/bin/env python

import argparse
import glob
import csv
import os.path
from rich.pretty import pprint
from pathlib import Path

# ------------------------------------------------------------------------------

def extract_runinfos(folder):
  """retrieve the list of hardware event ids for CORE0 from run*.csv files"""
  runs = glob.glob(f"{folder}/run_*.csv")
  runinfos = {}
  for run in runs:
    runinfo = {}
    with open(run,"r") as fin:
      data = csv.reader(fin,delimiter=";")
      for d in data:
        if d[0].startswith("CORE0"):
          runinfo[d[0]] = d[1]
      runinfos[int(run.replace(f"{folder}/run_","").replace(".csv",""))] = runinfo
  # let's order by filename
  runinfos = dict(sorted(runinfos.items()))
  # simplify events data
  # from {'CORE0_PMC_EVENT0': '4', 'CORE0_PMC_EVENT1': '3', 'CORE0_PMC_EVENT2': '21', 'CORE0_PMC_EVENT3': '22', 'CORE0_PMC_EVENT4': '23', 'CORE0_PMC_EVENT5': '24', 'CORE0_RECORD_TOTAL': '0', 'CORE0_RECORD_COUNT': '0'}
  # to [4,3,21,22,24]
  for run,runinfo in runinfos.items():
    events = []
    for i in range(6):
      events.append(int(runinfo[f"CORE0_PMC_EVENT{i}"]))
    runinfos[run] = events
  return runinfos

# ------------------------------------------------------------------------------

def retrieve_configurations(runinfos):
  """retrieve PMC configurations and associated runs"""
  configuration_files = {}
  configurations = []
  i=-1
  for run,runinfo in runinfos.items():
    if not runinfo in configurations:
      i += 1
      configurations.append(runinfo)
      configuration_files[i] = [run]
    else:
      configuration_files[i].append(run)
  #returns configuration lists, list of files per configuration
  return configurations,configuration_files

# ------------------------------------------------------------------------------

def retrieve_event_names():
  # retreive event names
  events = {}
  with open("hw_events_arm64.csv","r") as fin:
    reader = csv.reader(fin,delimiter=";")
    first = True
    for row in reader:
      if first:
        #ignore first line (header)
        first = False
      else:
        eid = int(row[0],base=0)
        name = row[1]
        events[eid] = name
  return events

# ------------------------------------------------------------------------------

def convert_raws_to_eventid(infolder,outfolder,runinfos):
  # duplicate raw csv with updated header looking like "EVT24" instead of "PMC0"
  Path(f"{outfolder}/{infolder}").mkdir(parents=True, exist_ok=True)
  for run,runinfo in runinfos.items():
    rawname = f"{infolder}/raw_{run}.csv"
    outname = f"{outfolder}/{infolder}/raw_{run}.csv"
    with open(outname,"w") as fout:
      with open(rawname,"r") as fin:
        headers = fin.readline()
        for i in range(6):
          headers = headers.replace(f";PMC{i};",f";EVT{runinfo[i]};")
        fout.write(headers)
        for row in fin:
          fout.write(row)

# ------------------------------------------------------------------------------

def convert_raws_to_eventnames(infolder,outfolder,runinfos,events):
  # duplicate raw csv with updated header looking like "L1D_CACHE" instead of "PMC0"
  Path(f"{outfolder}/{infolder}").mkdir(parents=True, exist_ok=True)
  for run,runinfo in runinfos.items():
    rawname = f"{infolder}/raw_{run}.csv"
    outname = f"{outfolder}/{infolder}/raw_{run}.csv"
    with open(outname,"w") as fout:
      with open(rawname,"r") as fin:
        headers = fin.readline()
        for i in range(6):
          headers = headers.replace(f";PMC{i};",f";{events[runinfo[i]]};")
        fout.write(headers)
        for row in fin:
          fout.write(row)

# ------------------------------------------------------------------------------

def consolidate(infolder):
  pprint(infolder)
  runinfos = extract_runinfos(infolder)
  #c,f = retrieve_configurations(runinfos)
  events = retrieve_event_names()
  convert_raws_to_eventid(infolder,"consolidated_by_id",runinfos)
  convert_raws_to_eventnames(infolder,"consolidated_by_name",runinfos,events)

# ------------------------------------------------------------------------------


parser = argparse.ArgumentParser(
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('input_folder')
args = parser.parse_args()

infolder = args.input_folder

consolidate(infolder)

folders = ["bpred","cputheft","speculate","LFBT_LFBL"]
subfolders = []
for f in folders:
  subfolders.extend(glob.glob(f"{f}/*"))

for s in subfolders:
  if os.path.isdir(s):
    consolidate(s)
