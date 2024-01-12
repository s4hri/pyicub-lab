![PYICUB logo](media/pyicublab-logo.png?raw=true)
====

Requirements
------------

- make
- docker

```
sudo apt-get install build-essential
```

Introduction
------------

[PYICUB-LAB](https://github.com/s4hri/pyicub-lab) is a development platform
for coding iCub applications in minutes!

```
git clone https://github.com/s4hri/pyicub-lab
cd pyicub-lab
bash go
```

How to start developing (VSCode)
---------------

Using VSCode and the devcontainer extension you can simply start code from the main directory

```
cd pyicub-lab
code .
```
From the VSCode IDE you can run: F1 -> "Dev Containers: Rebuild and reopen in container"
and the entire ecosystem (YARP->PyiCub) will be executed. The VSCode workspace will be 
set automatically to the pyicub repository, from where you can start developing.
If you want to develop on front-end container you can run F1 -> "Dev Containers: Attach to Running Container ..." attaching to the front-end pyicub container.


Acknowledgments
---------------

- pyicub logo inspired by [iCubArtwork](https://github.com/alecive/iCubArtwork)
