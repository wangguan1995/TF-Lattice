#!/bin/bash

export CUDA_VISIBLE_DEVICES=6

timestamp=$(date +"%Y%m%d_%H%M%S")

tfl_automobile tfl_config.json >"log_$timestamp.txt" 2>&1
