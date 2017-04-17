# eburydevopsdocker
Repository for the Ebury's Docker test.

[![N|Solid](https://web-statics.ebury.com/wp-content/themes/ebury-master-v2/assets/img/ebury-logo.svg)](https://www.ebury.es/)

#  EBURY DEVOPS TESTS

  - DOCKER EXERCISE.
  - Working directory: docker_test folder
  - Docker Engine 1.11 or higher

1. Complete Dockerfile to build the application container with all requirement needed(set working dir, install dependencies, set config variables and propagate script to container).
2. Complete cmd.sh file where depending value of $ENV start development server, production (using user created on dockerfile, setting production port and visibility), or test mode.
3. Fill <<CONNECTION_VALUES>> and <<HOST_VALUE>> in ebury.py file application.

### How to run
1. Install Docker 1.11 or higher.
2. Clone EBURY DEVOPS DOCKER proyect.
3. Change the enviorement in docker-compose.yml.
4. Run:

```sh
docker-compose up --build
```

### Proyect tree

```sh
docker_test$ tree
.
├── Dockerfile
├── README.md
├── app
│   ├── ebury.py
│   └── tests.py
├── cmd.sh
└── docker-compose.yml
```

### OS version

```sh
docker_test$ uname -a
Darwin AlvaroRacero.local 15.6.0 Darwin Kernel Version 15.6.0: Fri Feb 17 10:21:18 PST 2017; root:xnu-3248.60.11.4.1~1/RELEASE_X86_64 x86_64
```

```sh
docker_test$ sw_vers
ProductName:  Mac OS X
ProductVersion: 10.11.6
BuildVersion: 15G1421
```

### Docker version

```sh
docker_test$ docker version
Client:
 Version:      17.03.1-ce
 API version:  1.27
 Go version:   go1.7.5
 Git commit:   c6d412e
 Built:        Tue Mar 28 00:40:02 2017
 OS/Arch:      darwin/amd64

Server:
 Version:      17.03.1-ce
 API version:  1.27 (minimum version 1.12)
 Go version:   go1.7.5
 Git commit:   c6d412e
 Built:        Fri Mar 24 00:00:50 2017
 OS/Arch:      linux/amd64
 Experimental: true
```

```sh
docker_test$ docker info
Containers: 3
 Running: 0
 Paused: 0
 Stopped: 3
Images: 13
Server Version: 17.03.1-ce
Storage Driver: overlay2
 Backing Filesystem: extfs
 Supports d_type: true
 Native Overlay Diff: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins: 
 Volume: local
 Network: bridge host ipvlan macvlan null overlay
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: 4ab9917febca54791c5f071a9d1f404867857fcc
runc version: 54296cf40ad8143b62dbcaa1d90e520a2136ddfe
init version: N/A (expected: 949e6facb77383876aeff8a6944dde66b3089574)
Security Options:
 seccomp
  Profile: default
Kernel Version: 4.9.13-moby
Operating System: Alpine Linux v3.5
OSType: linux
Architecture: x86_64
CPUs: 2
Total Memory: 1.952 GiB
Name: moby
ID: AZ3N:6GAH:EGXD:KZB7:IF66:ILWO:FFGN:SKQD:IPJF:TCMX:6OKK:TGNG
Docker Root Dir: /var/lib/docker
Debug Mode (client): false
Debug Mode (server): true
 File Descriptors: 30
 Goroutines: 29
 System Time: 2017-04-17T07:53:20.399308633Z
 EventsListeners: 1
No Proxy: *.local, 169.254/16
Registry: https://index.docker.io/v1/
Experimental: true
Insecure Registries:
 127.0.0.0/8
Live Restore Enabled: false
```