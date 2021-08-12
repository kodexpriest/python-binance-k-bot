import psycopg2
import sys
from time import time
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from math import floor, ceil
import datetime
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
import copy

conn_string = "host='localhost' dbname='bittrex' user='rhan' password='[REDACTED]'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()