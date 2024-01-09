import os
import sys
sys.path.append(os.environ.get('ARTEX'))
print(os.environ.get('ARTEX'))
from Admin.Trainer import TrainAI

TrainAI()