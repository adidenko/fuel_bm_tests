#!/bin/bash
export PYTHONPATH="./pylibs:./03_setup/environments"

PYTHON_BIN="/usr/bin/python"
FUEL_MASTER_NODE='10.20.0.2'
OS_NODES="fuel1 fuel2 fuel3 fuel4"
arg="$1"
SLEEP="sleep 30"
ARGS="--separate-provisioning"
ts=`date +"%Y-%m-%d_%H-%M-%S"`
LOG="/tmp/logs/$env-$ts"
TOTAL_OS_NODES=`echo $OS_NODES | wc -w`

# wipe nodes
function wipe_nodes {
	for node in $OS_NODES; do
		if virsh vcpuinfo $node &>/dev/null ; then
			virsh destroy $node &>/dev/null
			sleep 1
			for file in `virsh dumpxml $node | awk '/<disk /{f=1} /\/disk>/{f=0} f' | grep 'source file' | grep -o "/.*'" | sed -e "s#'##g"` ; do
				if `echo $file | grep -q 'disk0'`; then
					echo dd if=/dev/zero of=$file bs=1M count=1
				else
					echo "PANIC!!! Almost tried to destory '$file' file which does not match our security pattern"
					exit 1
				fi
			done
			sleep 1
			virsh start $node
		else
			echo $node not found
		fi
	done
}

# wipe and exit if requested
if `echo "$@" | grep -q 'reset'`; then
	wipe_nodes
	exit 0
fi

# check/wipe/wait for nodes
DISCOVERED_NODES=`curl -s -X GET http://$FUEL_MASTER_NODE:8000/api/nodes | python -mjson.tool | grep discover | wc -l`
if [ "$DISCOVERED_NODES" != "$TOTAL_OS_NODES" ] ; then
	echo -n "Discovered nodes: $DISCOVERED_NODES, but should be $TOTAL_OS_NODES. Rebooting nodes ."
	wipe_nodes &>/dev/null
	for i in {1..30} ; do
		DISCOVERED_NODES=`curl -s -X GET http://$FUEL_MASTER_NODE:8000/api/nodes | python -mjson.tool | grep discover | wc -l`
		if [ "$DISCOVERED_NODES" != "$TOTAL_OS_NODES" ] ; then
			echo -n "."
			sleep 10
		else
			echo "DONE"
			break
		fi
	done
fi

DISCOVERED_NODES=`curl -s -X GET http://$FUEL_MASTER_NODE:8000/api/nodes | python -mjson.tool | grep discover | wc -l`
if [ "$DISCOVERED_NODES" != "$TOTAL_OS_NODES" ] ; then
	echo "TIMEOUT. Discovered only $DISCOVERED_NODES of $TOTAL_OS_NODES nodes. Exiting"
	exit 1
fi


# create env
if [ -f "$arg" ] ; then
	env=`basename $arg | sed -e 's#\.py$##'`
else   
	env="$arg"
fi


####################
        # Let's rock-n-roll
        DEPLOY="no"
        if `echo "$@" | egrep -q 'create_only|create-only'`; then
                $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env remove $LOG
                $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env create $LOG
        else
                $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env remove $LOG
                $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env create $LOG && \
                $SLEEP && \
                $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env netverify $LOG && \
                $SLEEP && \
                $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env deploy $LOG && \
                (
                        DEPLOY="done"
                        $SLEEP && \
                        $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env netverify $LOG 
                        $SLEEP && \
                        $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env ostf $LOG
                ) || DEPLOY="failed"
        fi

        $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env snapshot $LOG

        if `echo "$@" | egrep -qv 'keep_env|keep-env|create_only|create-only'`; then
                $PYTHON_BIN manage_env.py $ARGS $FUEL_MASTER_NODE $env --dont-wait remove $LOG
		sleep 10
		wipe_nodes &>/dev/null
        fi
 
####################
