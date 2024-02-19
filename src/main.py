import asyncio
import os
import sys
from queries.core import SyncCore
from queries.orm import SyncOrm

sys.path.insert(1, os.path.join(sys.path[0], '..'))


# SyncOrm.create_tables()
# SyncOrm.insert_workers()
# SyncCore.select_workers()
# SyncCore.update_worker()


SyncOrm.select_workers()
SyncOrm.update_workers()