#import pandas as pd
import numpy as np
import json
import os
import sys

#
# use to debug json_file dict iteration
#

json_file='QA_CustomSignature_MULTI.json'

with open(str(json_file)) as f:
    resp_dict = json.load(f)

#
zipsize=[]
zipCode=[]
stbProject=[]
#
