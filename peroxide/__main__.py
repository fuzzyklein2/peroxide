from .startup import *
from .peroxide import Peroxide

if __name__ == '__main__':
    print(PROGRAM)
    log.info(f'Executing {PROGRAM} ...')
    
    p = Peroxide()
    p.run()
    
    log.info(f'Execution complete.')
