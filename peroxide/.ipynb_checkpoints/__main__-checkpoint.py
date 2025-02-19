from .startup import *
from .filter import Filter

if __name__ == '__main__':
    print(PROGRAM)
    log.info(f'Executing {PROGRAM} ...')
    
    p = Filter()
    p.process_files()
    
    log.info(f'Execution complete.')
