#!/bin/bash

export PID=$$

if [ "$1" == "" ] ; then
    read -p "Are you sure you want to create libvirt env? (y/N):" rpl
else
    rpl="$1"
fi

if [ "$2" == "skip" ] ; then
	export SKIP="true"
else
	export SKIP="false"
fi

error=""

function error_exit {
	if [ "$SKIP" == "false" ]; then
		echo -e "\nERR: Errors found. Exiting."
		kill -s TERM $PID
	fi
}

if [ "$rpl" == "Y" ] || [ "$rpl" == "y" ] ; then

	echo "==== Basic check ===="
	if [ ! -e /dev/kvm ] ; then
		echo "ERR: /dev/kvm not found"
		exit 1
	fi
	virsh --version &>/dev/null || (
		echo "ERR: virsh not found"
		exit 1
	)
	if [ ! -e "/var/tmp/iso/fuel.iso" ] ; then
		echo "ERR: /var/tmp/iso/fuel.iso not found!"
		echo "Please put a Fuel ISO (or a symlink) into /var/tmp/iso/fuel.iso and restart"
		exit 1
	fi

	echo "==== Checking for network conflicts ===="
	pushd networks &>/dev/null
	for i in fuel_*xml; do 
		netip=`grep -o "ip address='.*' " $i | grep -o '[[:digit:]]\+.[[:digit:]]\+.[[:digit:]]\+.[[:digit:]]\+'`
		conflict=`ip ro ls | grep $netip` && (
			echo -e "\nConflict found for network '$i' - $netip already presents in your routing table:\n!!!!!! $conflict !!!!!!"
			echo "Please make sure you're using unique IPs/networks for the test lab to avoid problems with your routing"
			error_exit
		)
	done
	popd &>/dev/null

	echo "==== Creating virtual networks ===="
	pushd networks &>/dev/null
	for i in fuel_*xml; do
		virsh net-create --file $i || error_exit
	done
	popd &>/dev/null

	echo "==== Checking for guest names conflicts ===="
	pushd guests &>/dev/null
	for i in fuel*xml; do
		name=`grep -o '<name>.*</name>' $i | sed -e 's#<name>##' -e 's#</name>##'`
		conflict=`virsh list --all | grep "[[:space:]]$name[[:space:]]"` && (
			echo -e "\nConflict found for VM '$i' - guest with '$name' name already exists:\n!!!!!! $conflict !!!!!!"
			echo "Please make sure you're using unique VM names for the test lab to avoid problems"
			error_exit
		)

	done
	popd &>/dev/null

	echo "==== Creating virtual machines ===="
	pushd guests &>/dev/null
	for i in fuel*xml; do
		for disk in `awk '/<disk /{f=1} /\/disk>/{f=0} f' $i | grep 'source file' | grep disk0 | grep -o "/.*'" | sed -e "s#'##g"`; do
			mkdir -p `dirname $disk` || ( error="1" ; break )
			if [ -f "$disk" ] ; then
				echo "ERR: $disk already exists"
				error_exit
			fi
			fallocate -l 35G $disk || error_exit
		done
		virsh create $i || error_exit
	done
	popd &>/dev/null
	echo -e "\nDONE.\n"
fi
