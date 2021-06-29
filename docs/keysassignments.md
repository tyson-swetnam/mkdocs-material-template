# Keys Assignments 

## Assignment 1: Introduction to Your Research

### Purpose of the Research 

To create a **"Research Object"** where anyone can reproduce their research using a living workflow that includes cyberinfrastructure (hardware, orchestration software), containers (specific research software libraries, algorithms, and code), and data. 

### Previous Research

n/a -- this is the bleeding edge!

### Describe The Need For The Study

> ![alt text](https://learning.cyverse.org/projects/foss-2020/en/latest/_images/reproducibility-spectrum.png)
>
> **Figure credit**: [Peng 2011](https://science.sciencemag.org/content/334/6060/1226) described in the journal [Science](https://science.sciencemag.org) how reproducible research can be accomplished.

Doing reproducible research is hard! 

By providing a templated development environment, using GitHub, GitPod, Docker, and common data science programming languages (R, Python, Java, etc), researchers can use CyVerse to work together more seamlessly and interactively, and students can work asynchronously following easy to follow materials. 

### Problem Statement

> How can a researcher or a student get started with these platforms and tools if they've never seen or heard of them them before?
>> Solution: Develop my own personal profile on GitHub, and add these resources as repositories where others can clone my templates and do their own research.

### Helpful Images (Photographs, Tables, Charts, etc)

add more here

## Assignment 2: Materials and Methods

### Methods

[Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration)(CI) requires a platform from which to test software. [Continuous Delivery](https://en.wikipedia.org/wiki/Continuous_delivery)(CD) allows software to be released quickly and reliably. These two continous frameworks are frequently used together as 'CI/CD'.  

I am using [GitHub](https://github.com/shrutir11) as the resource for hosting the software CyVerse are working on. GitHub provides "version control" for the code, in case there are any mistakes, they can be reversed. GitHub also supports "[Actions](https://github.com/features/actions" which run software as part of the CI/CD life cycle

I am building software containers with [Docker](https://docker.com) and hosting them on the [DockerHub](https://hub.docker.com) registry. A Docker container has its own operating system, and the specific software I want to run. Docker is an easy way to quickly write code and then run it. When run on the cloud, Docker allows researchers to run whatever they want in the container without having to download the application itself on the host. Containers can be shared so that everyone can have the same copy of the container. Docker can be used to push researchers' applications into a test environment where they can run automated/manual tests. During this research project it will be used to push containers and open them in GitPod and on CyVerse.

> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/methods%20to%20push%20container%20from%20github%20to%20docker.JPG)
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/methods%20to%20launch%20rstudio%20from%20github%20using%20gitpod.JPG)


### Materials

 - Docker: allows it's users to create containers and run an application such as RStudio Markdown Notebooks or Jupyter Notebooks. 
 
 - DockerHub: a registry of public Docker containers. We will host our public images on DockerHub

 - GitHub Actions: allows for the automation of tasks within your software development life cycle. Through GitHub Actions users can automatically run their software testing scripts. During this intenrship GitHub Actions will be used to push the code from GitHub to DockerHub and open containers such as rstudio-cyverse in Docker.
  
 - GitPod: GitPod is a fully working environment that can be launched from GitHub. Setting up local dev environments is often very time consuming, but GitPod can do this within a couple of seconds. GitPod includes all the tools and binaries that are available on Linux. During this internship GitPod will be used to help launch RStudio, Jupyter, Java8, and more applications directly from GitHub. 
 
 - Scientific Programming languages: Python, R, Java. Will be used in this internship as an application that will be opened using GitPod from a specific repository.

 - GitHub: Will be used to store repository and code.


