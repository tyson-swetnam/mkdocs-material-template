### Introduction
[Docker](https://www.docker.com/) allows it's users to create containers and run an application such as RStudio or Jupyter Notebooks in this environment. This open platform is an easy way to quickly write code and then run it. It allows researchers to run whatever they want in the container without having to download the application itself on the host. Containers can be shared so that everyone can have the same copy of the container. Docker can be used to push researchers' applications into a test environment where they can run automated/manual tests. 

### Key Vocabulary

#### Images
Images are used to create Docker containers. These are typically created in GitHub using the file name .gitpod.Dockerfile. The Dockerfile outlines the steps needed to create the image and then run it as well. When more instructions are added to the Dockerfile this creates layers in the image. If more instructions are added to the Dockerfile, when it is rebuilt only the layers which are changed are rebuilt. This is one of the reasons why images are lightweight, fast, and small when compared to other virtualization technologies. 
> ![alt text](https://miro.medium.com/max/3600/0*CP98BIIBgMG2K3u5.png)  
> **Figure credit**: [Chen 2020](https://medium.com/swlh/understand-dockerfile-dd11746ed183) described in [Medium](https://medium.com/) basic concept of Docker

#### Containers
A container is considered as a package that stores all the libraries, files, and binaries necessary to run an application. Using containers software can be moved from different environments and still run reliably. A container is typically only around 10 megabytes in size meaning that a host could run more than one container whereas they only be able to run one virtual machine. Containers can run across all systems(Windows, Mac, and Linux) making them easily accessible. 
![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/container.JPG) 
> **Figure credit**: Shruti Ramkumar 2021
![alt text](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.docker.com%2F&psig=AOvVaw3W10Yte7b3emiw12k3q6lo&ust=1624665846031000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCLiR1oe-sfECFQAAAAAdAAAAABAD)
> **Figure credit**: [Docker](https://www.docker.com/) 

