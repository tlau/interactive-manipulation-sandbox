#! /bin/bash

###
# Allow dry-runs.
# Set to 'false' if you want the script to take any effect. Otherwise it will
# only echo the lines it would otherwise execute
#
DEBUG=false

# Parse arguments:
#  -r release_number
while getopts ":r:" opt; do
  case $opt in
    r)
      RELEASE_NUMBER=$OPTARG
      echo "Release number provided: $RELEASE_NUMBER"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires the release number as argument." >&2
      exit 1
      ;;
  esac
done

# If no release number specified, use default 'unk' (unknown)
if [ -z $RELEASE_NUMBER ]; then
    RELEASE_NUMBER = "unk"
fi

runthis () {
    command_message=$1
    command_line=$2
    echo
    echo "--- ${command_message}... ---"
    if ${DEBUG} ; then
        echo ${command_line}
    else
        eval ${command_line}
    fi
    echo "--- ...done ---"
}

###
# Script variables.
#
# Auto-discover location of deploy script to calculate location of other files from there
DEPLOYDIR="`dirname \"$0\"`"
DEPLOYDIR="`( cd \"$DEPLOYDIR\" && pwd )`"
APPDIR="${DEPLOYDIR}/../../django"
PYTHON="python"
SERVER_PID_FILE="${APPDIR}/server.pid"
#
###


###
# Instance variables.
CURRENT_SERVER_PID="$(cat ${SERVER_PID_FILE})"
DUMP_DIR="${APPDIR}/dumps"
DUMP_FILE="continuousop.${RELEASE_NUMBER}.$(date +'%Y%m%d').json"

###
# Tasks
#

run_server () {
    ${PYTHON} manage.py runserver &>/dev/null &
    CURRENT_SERVER_PID=$!
    echo ${CURRENT_SERVER_PID} > ${SERVER_PID_FILE}
}


###
# Move to the APPDIR
runthis "cd'ing into the target directory" "cd ${APPDIR}"

###
# Step 1:
#
# Kill the running server.
runthis "Killing the server" "kill ${CURRENT_SERVER_PID}"
# TODO: Wait for server to die and make sure it's dead before continuing
sleep 3

###
# Step 2:
#
# Run all migrations.
runthis "Running migrations" "${PYTHON} manage.py migrate --all"

###
# Step 3:
#
# Dump the "world" data to a known location for others to load.
runthis "Dumping today's world' data." "mkdir -p ${DUMP_DIR}; ${PYTHON} manage.py dumpdata --all | tail -n 1 > ${DUMP_DIR}/${DUMP_FILE}"

###
# Step 4:
#
# Bring the server back up.
runthis "Get the server back online" "run_server"

