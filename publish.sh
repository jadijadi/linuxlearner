#!/bin/bash 

pelican content
ghp-import output
git push origin gh-pages
