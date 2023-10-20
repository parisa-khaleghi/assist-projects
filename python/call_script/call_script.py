#============================================#
#            CALL SCRIPT FROM GIT            #
#                                            #
#                For Example                 #
#     I will call the 'commit' function      # 
#         from this repo located in          #
#     "python/git_commit/git_commit.py"      #
#============================================#


import sys
import datetime

# Append the path to the external repository that you cloned on your system
sys.path.append('/Users/parisakhaleghi/Desktop/Coding/assist_projects/python/git_commit')

# Import the specific function from the script in the external repository
from git_commit import commit

# The required arguments (in order):   
#           'project_path', 
#           'file_path', 
#           'message', 
#           'year', 'month', 'day', 
#           'hour', and 'minute'
print(commit('/Users/parisakhaleghi/Desktop/Coding/assist_projects',
             '/Users/parisakhaleghi/Desktop/Coding/assist_projects/python/call_script/call_script.py',
             'update: call the function from madule',
             datetime.datetime.now().year,
             datetime.datetime.now().month-1,
             datetime.datetime.now().day,
             datetime.datetime.now().hour,
             datetime.datetime.now().minute
             ))
