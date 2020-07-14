import ROOT, subprocess
import os
import sys
program_name = sys.argv[0]
DIR = sys.argv[1]
print "status of  ", DIR
def checkFilesWithTracks():
  temp=subprocess.check_output('ls '+DIR,shell=True)
  for file in temp.split('\n'):
    if file.rfind('RT')>-1:
      try:
        f=ROOT.TFile(DIR+file)
        sTree=f.cbmsim
        rc=sTree.GetBranchStatus("FitTracks")
        dest=DIR+file
        if not rc :print dest
      except:
        print DIR+file
