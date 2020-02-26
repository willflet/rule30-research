#!/bin/sh

set -e

echo y | sudo pip uninstall grayfractal
sudo python3 setup.py install
sudo rm -rf docs/source/grayfractal.*.rst
sudo rm -rf docs/source/modules.rst
sphinx-apidoc -feM -d 1 -o docs/source .
#sed -i "s/.. toctree::/.. toctree::\n   :maxdepth: 1/g" doc/source/grayfractal.*
sed -i "s/    /   /g" docs/source/grayfractal.*
sphinx-build -b html docs/source/ ../../../../Websites/docpages/rule30-research/grayfractal
