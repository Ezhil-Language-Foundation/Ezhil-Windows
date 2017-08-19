#!/bin/bash -x
if [ $# -ne 1 ]; then
    echo "Usage: build.sh {{source dir path}}"
    exit -1
fi

EZHILSRC=$1
STARTDIR=`pwd`
cp $EZHILSRC/editor/res -ar ./
cp $EZHILSRC/editor/examples -ar ./
cp $EZHILSRC/editor/xmlbook -ar ./
cp $EZHILSRC/editor/*.ico ./
cp $EZHILSRC/editor/*.py ./

cd cli && pyinstaller --log-level=DEBUG --icon=ezhil.ico ezhili.py
cd $STARTDIR
pyinstaller --windowed --log-level=DEBUG --icon=ezhil16.ico ../ezhuthi.spec
cp -ar res/ ./examples ./xmlbook ./dist/ezhuthi/
cd dist/
BDIR=ezhil-`date +'%m%d%y'`
mkdir $BDIR
mv ezhuthi $BDIR
