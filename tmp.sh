#!/bin/bash

#tmp support 2 cmd
rawCmds=$1
buildCMD=`echo $rawCmds | cut -d ";" -f1`
cpCMD=`echo $rawCmds | cut -d ";" -f2`
echo $buildCMD
echo $cpCMD
$buildCMD
$cpCMD
