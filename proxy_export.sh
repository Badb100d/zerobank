#!/bin/bash

proxy_str="$1"
echo $proxy_str
export http_proxy=$proxy_str
export https_proxy=$proxy_str
export all_proxy=$proxy_str
export HTTP_PROXY=$proxy_str
export HTTPS_PROXY=$proxy_str
export ALL_PROXY=$proxy_str
