#!/bin/bash

if [ -z "$1" ]
	then
		echo "No argument supplied"
        exit 1
fi

directory=$1

rm $directory/*.xhtml
