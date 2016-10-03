#!/bin/sh

OUTPUTDIR="static/css/pygments"

for style in manni igor xcode vim autumn vs rrt native perldoc borland tango emacs friendly monokai paraiso-dark colorful murphy bw pastie paraiso-light trac default fruity
do
    echo ${style}...
    pygmentize -S $style -f html -a ".highlight pre"> $OUTPUTDIR/$style.css
done