#!/bin/bash
# chmod +x docs-generate.sh
# ./docs-generate.sh

function logging() {
  echo -e "\033[0;32m$1\033[0m"
}

function warnings() {
  echo -e "\033[31m$1\033[0m"
}

function whereIam() {
  echo -e "@ \033[07m`pwd`\033[0m"
}

# SCRIPT_DIR=$(cd $(dirname $0); pwd)
SRC_DIRNAME="src"
DOC_DIRNAME="docs"
MODULE_DIRNAME="{{ MODULE_NAME }}"
REBUILD_DIRNAMES=(
  "${DOC_DIRNAME}"
  "src/_build/plot_directive"
)
CREATED_DIRNAME="_build/html"
HERE=$(cd $(dirname $0);pwd)

logging "cd $HERE"
cd $HERE
whereIam

for DIRNAME in ${REBUILD_DIRNAMES[@]}
do
  echo "${DIRNAME}"
  if [ -d $DIRNAME ]; then
    warnings "Delete old $DIRNAME directory."
    rm -rf $DIRNAME
  fi
done

logging "$ sphinx-apidoc -f -e -o $SRC_DIRNAME $MODULE_DIRNAME"
poetry run sphinx-apidoc -f -e -o $SRC_DIRNAME $MODULE_DIRNAME

logging "cd $SRC_DIRNAME"
cd $SRC_DIRNAME
whereIam

logging "make html"
make html
logging "mv $CREATED_DIRNAME ../$DOC_DIRNAME"
mv $CREATED_DIRNAME ../$DOC_DIRNAME

cd $HERE
whereIam
for IMG in background.png not-found.png
do
  logging "cp $SRC_DIRNAME/_images/$IMG $DOC_DIRNAME/_images/$IMG"
  cp $SRC_DIRNAME/_images/$IMG $DOC_DIRNAME/_images/$IMG
done
