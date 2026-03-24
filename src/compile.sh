#!/bin/bash
qcc -fopenmp -Wall -O2 testcase-3p.c -o a.out  -L$BASILISK/gl -lglutils -lfb_glx -lGLU -lGLEW -lGL -lX11 -lm

