#!/bin/bash
exe() { echo "\$ $@" ; "$@" ; }
exe sudo systemctl restart testedmondsonline
exe sudo systemctl status testedmondsonline
