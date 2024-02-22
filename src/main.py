import asyncio
import os
import sys
from queries.core import SyncCore
from queries.orm import SyncOrm

sys.path.insert(1, os.path.join(sys.path[0], '..'))

SyncOrm.select_resumes_avg_compensation()
