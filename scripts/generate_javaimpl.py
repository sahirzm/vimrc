#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    sys.exit("USAGE: python3 generate_javaimpl.py <FILENAME>")
f = open(sys.argv[1], 'r')

for l in f:
    l = l.split('.')[0]
    n = l.split('/')
    print(n[len(n) - 1] + ' ' + l.replace('/', '.'))

f.close()


# jar tf $JAVA_HOME/src.jar | sed -e 's#^src/##' > $HOME/.vim/temp_dirs/JavaImp/jdk.jmplst
