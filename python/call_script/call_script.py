#============================================#
#            CALL SCRIPT FROM GIT            #
#                                            #
#                For Example                 #
#     I will call the 'commit' function      # 
#         from this repo located in          #
#     "python/git_commit/git_commit.py"      #
#============================================#


import sys

# Append the path to the external repository that you cloned on your system
sys.path.append('/Users/parisakhaleghi/Desktop/Coding/assist_projects/python/git_commit')

# Import the specific function from the script in the external repository
from git_commit import commit

print(commit())
