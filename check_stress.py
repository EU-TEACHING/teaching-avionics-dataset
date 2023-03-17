#!/usr/bin/env python3

import os
import sys
import subprocess
import glob

if len(sys.argv) > 2:
  print(f"Error: Syntax: {os.path.basename(sys.argv[0])} <foldername>")
  exit(1)

nb_rows = 10503

if len(sys.argv) == 2:
  folders = [sys.argv[1]]
else:
  folders = glob.glob("*/????.??")

for folder in folders:
  summary = {}
  for i in range(0,50):
    path = f"{folder}/raw_{i}.csv"

    proc = subprocess.Popen(["/bin/grep","-c","NOSTRESS",path],stdout=subprocess.PIPE,text=True)
    (out, err) = proc.communicate()
    out = out.strip()
    ratio = 100 * int(out) // nb_rows
    #print(f"raw_{i} {ratio}% NOSTRESS")
    try:
      summary[ratio].append(i)
    except KeyError:
      summary[ratio] = [i]

  print(f"\033[1;33m{folder}\033[0m")
  col = 32
  if len(summary) != 1:
    col = 31
  for percent,ids in summary.items():
    per = f"{percent}%"
    print(f"  \033[1;{col}m{per:<5} of NOSTRESS: {len(ids)} files\033[0m")