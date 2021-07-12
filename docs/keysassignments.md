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

I am using [GitHub](https://github.com/shrutir11) as the resource for hosting the software CyVerse are working on. GitHub provides "version control" for the code, in case there are any mistakes, they can be reversed. GitHub also supports "[Actions](https://github.com/features/actions)" which run software as part of the CI/CD life cycle

I am building software containers with [Docker](https://docker.com) and hosting them on the [DockerHub](https://hub.docker.com) registry. A Docker container has its own operating system, and the specific software I want to run. Docker is an easy way to quickly write code and then run it. When run on the cloud, Docker allows researchers to run whatever they want in the container without having to download the application itself on the host. Containers can be shared so that everyone can have the same copy of the container. Docker can be used to push researchers' applications into a test environment where they can run automated/manual tests. During this research project it will be used to push containers and open them in GitPod and on CyVerse.

> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/code%20from%20.yml%20file.JPG)

Line 1: This is the name of workflow when the action is running(optional line) 
Line 3-5: Establishes the event that triggers the workflow 
Line 6-7: The workflow will automatically build and push every Saturday at 12:00 UTC time 
Line 9: 

> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/methods%20to%20push%20container%20from%20github%20to%20docker.JPG)
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/methods%20to%20launch%20rstudio%20from%20github%20using%20gitpod.JPG)


### Materials

 - Docker: allows it's users to create containers and run an application such as RStudio Markdown Notebooks or Jupyter Notebooks. 
 
 - DockerHub: a registry of public Docker containers. We will host our public images on DockerHub

 - GitHub Actions: allows for the automation of tasks within your software development life cycle. Through GitHub Actions users can automatically run their software testing scripts. During this intenrship GitHub Actions will be used to push the code from GitHub to DockerHub and open containers such as rstudio-cyverse in Docker.
  
 - GitPod: GitPod is a fully working environment that can be launched from GitHub. Setting up local dev environments is often very time consuming, but GitPod can do this within a couple of seconds. GitPod includes all the tools and binaries that are available on Linux. During this internship GitPod will be used to help launch RStudio, Jupyter, Java8, and more applications directly from GitHub. 
 
 - Scientific Programming languages: Python, R, Java. Will be used in this internship as an application that will be opened using GitPod from a specific repository.

 - GitHub: Will be used to store repository and code.

### Long Abstract
Reproducible science is hard. It is defined as the fact that any result obtained from an experiment should be able to be obtained again with a high-level degree of accuracy using the exact same method used in the original experiment. However currently much of the research scientists are doing is unable to be replicated by other fellow peers. This leads to the concern that the results scientists are producing may be flawed or may be left unchecked. As the world shifts to using technology to further research it’s important that scientists begin to use it to help with reproducible science. The purpose of this project was to create living workflows using version control to help scientists with their research. Living workflows such as containers help scientists open applications like RStudio and JupyterLab in a virtual machine where they can instantly share and save their work with others. During this project repositories were created in GitHub in order to build and push containers carrying RStudio and JupyterLab to Docker, Cyverse, and GitPod. The repositories contained Dockerfiles(contain images of the container) and .yml files. The .yml files in the repositories were created using GitHub Actions which created commands to help build and push the containers to the various platforms mentioned previously. Scientists will now be able to click on the repositories in my GitHub and launch containers that have RStudio and JuptyerLab already installed. They then can work in these containers and share their research with peers furthering reproducible science. 
