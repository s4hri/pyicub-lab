
PYICUB-LAB
====

[PYICUB-LAB](https://github.com/s4hri/pyicub-lab) is a development platform
for coding iCub applications in minutes!

Requirements
------------

- make
- docker

```
sudo apt-get install build-essential
```

Build the environment
------------
In order to build the entire ecosystem is enough to run the build script, that will take care of managing permissions between your host machine and the container.

```
git clone https://github.com/s4hri/pyicub-lab
cd pyicub-lab
./build.sh
```

Run the environment
------------
Once built succesfully the container, you will be able to run the compose file and start developing [PYICUB](https://github.com/s4hri/pyicub) applications.

```
cd pyicub-lab
./run.sh
```