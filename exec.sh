#!/usr/bin/bash
# makes the py file executable and creates a symbolic link to PATH
name=$1

sudo chmod a+x $name
echo "Changed permissions! "
sudo ln -s $name /usr/local/bin/$name
echo "done! "