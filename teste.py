import sys

if hasattr(sys, 'real_prefix') or hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
    print('Ambiente virtual')
else:
    print('Não é virtual')