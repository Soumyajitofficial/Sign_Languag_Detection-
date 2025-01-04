import logging
import os
from datetime import datetime
from from_root import from_root


LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
Log_path = os.path.join(from_root(),"log",LOG_FILE)

os.makedirs(Log_path, exist_ok=True)

logging.basicConfig(filename=Log_path, 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )