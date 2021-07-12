# Logbook


*Day 1 (6/14)*: Completed the [Python](https://swcarpentry.github.io/python-novice-inflammation/) tutorial using [carpentries](https://carpentries.org/). Learned how to create/utilize variables, process tabular data files, visualize tabular data files, store values in lists, repeat actions using loops, analyze data from multiple files, and debug programs. 

*Day 2 (6/15)*: Completed the [Version Control with Git](http://swcarpentry.github.io/git-novice/) tutorials using [carpentries](https://carpentries.org/). Learned how to create a repository in Git, record changes in Git, read tabular data, modify and commit files, utilize the HEAD and CAT commands, and push/pull/clone a remote repository.

*Day 3 (6/16)*: Completed the [Unix](http://swcarpentry.github.io/shell-novice/) tutorial using [carpentries](https://carpentries.org/). Learned how to create files and directories, navigate files and directories, construct command pipelines, process files, write loops and shell sripts, and utilize the commands grep and find.

*Day 4 (6/17)*: Read ["The iPlant Collaborative: Cyberinfrastructure for Enabling Data to Discovery for the Life Sciences"](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002342) and ["Ten Simple Rules to Cultivate Transdisciplinary Collaboration in Data Science"](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008879). Learned about the origins of [CyVerse](https://cyverse.org/) and how it was initially used to support life science communities in their search for a proper tool for data management. Understood the importance of following ten simple rules to help with furthering the culture of collaboration.

*Day 5 (6/18)*: Met with Dr.Swetnam and discussed my tasks for the day.Created this website in order to track progress during KEYS and comply with reproducible science. Added hyperlinks to the introduction page and logbook, created each of the pages using GitHub, and added descriptions to the introduction and logbook pages.

*Day 6 (6/21)*: Added descriptions and hyperlinks to the CyVerse, R, and Python pages. Completed my logbook with more detail. Learned how to launch [GitPod](https://linuxtut.com/en/dbb64871480cf1a06acf/) and then opened a Jupyter Notebook using GitPod.
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/Launching%20GitPod.JPG)
> **Launching GitPod for the first time!**

> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/Launching%20Jupyter%20Notebook%20Using%20GitPod.JPG)
> **Launching Jupyter Notebook using GitPod**

*Day 7(6/22)*: With the help of Dr.Swetnam learned how to access Docker from GitPod and run [GodLoveD/lolcow](https://github.com/GodloveD/lolcow) container using Docker.
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/First%20Container%20lolcow.JPG)  
**Output from my first container on GitPod**
  
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/Manipulating%20various%20entry%20points%20of%20the%20container.JPG)  
**Manipulating the various entry points of the container using GitPod**

*Day 8(6/23)*: Attended the KEYS Science Literacy Seminar in the morning where the deans of several of the colleges at the University of Arizona talked. During the seminar also discussed the need to present our projects in layman terms so that the average person can understand what is happening. In the afternoon met with Dr.Swetnam and discussed the tasks for the upcoming two days. Tried to build container using [GodLoveD/lolcow](https://github.com/GodloveD/lolcow) as an example, but came across this error. 
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/error%20in%20gitpod.JPG)  
> **Error while attempting to build and push first container**

*Day 9(6/24)* Attempted to launch Rstudio using the GitPod extension, but was unable to due to errors. Researched about these errors on the GitPod community, but was not able to find any solutions. Used [KasperBrink's GitHub](https://github.com/kasperbrink/gitpodR/) repository as an outline for this attempt. Created pages on the website for Docker, GitPod, GitHub Actions, and Java. Added information + pictures to the Docker page. 
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/rstudio%20error.JPG)  
> **Error while attempting to launch RStudio using GitPod**

*Day 10(6/25)* Added descriptions and pictures to the GitPod, GitHub Actions, and Java pages. With the help of Dr.Swetnam was able to build and push first container to DockerHub. 
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/pushing%20first%20container%20to%20dockerhub.JPG)  
> **Pushing first container to DockerHub**

*Day 11(6/28)* Added the materials and methods page to the website and added descriptions to these pages. Tried to push container from GitHub to DockerHub. Faced several problems along the way two of the problems are shown below.
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/error%20while%20pushing%20to%20github.JPG)  
> **Error while pushing container to DockerHub/ Solved the error by creating an access token through DockerHub**
> > ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/error%20during%20build%20and%20push.JPG)  
> **Error while attempting to build the container**

*Day 12(6/29)* Met with Dr.Swetnam and he recommended I try creating a seperate repository to try and push a container to DockerHub to see if that works first before attempting this with the rstudio-verse repository. Created a seperate repository using a [tutorial](https://docs.docker.com/ci-cd/github-actions/) and was able to push my first container from GitHub to Docker using GitHub Actions. Hope to replicate this in the upcoming days for the rstudio-verse repository. 
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/first%20checkmark!.JPG)  
> **First checkmark in GitHub Actions indicating my container was pushed to DockerHub!! Took probably over 25-30 tries**
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/first%20time%20pushing%20container%20to%20Docker%20directly%20from%20GitHub%20using%20GitHub%20Actions.JPG)  
> **Container appearing in DockerHub after it was pushed from GitHub using GitHub Actions**

*Day 14(7/6)* Opened new project in RStudio and played around with the dataset [PalmerPenguins](https://github.com/allisonhorst/palmerpenguins). Followed the instructions to explore the dataset on this [website](https://towardsdatascience.com/penguins-dataset-overview-iris-alternative-9453bb8c8d95) Had trouble at first installing package in the RStudio library. Solved the problem with the help of Dr. Swetnam and this [article](https://www.displayr.com/installing-r-packages-from-github/)
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/error%20installing%20package%20in%20rstudio.JPG)  
> **Error when trying to install palmer penguins package in RStudio**
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/installing%20palmerpenguins%20package.JPG)  
> **Palmer Peguins package was successfully installed**
> 
*Day 15(7/7)* Tried to push rstudio-verse container to Docker using GitHub Actions. Faced several problems along the way. One being that during the build and push stage GitHub was unable to locate the Dockerfile since there were no Dockerfiles in the root of the rstudio-verse folder. To solve this problem created a path and identified where the Dockerfile was. Took about 50+ tries to do this. Then faced another problem when GitHub was installing the rockerverse container because the code exited at step 14/26.
> ![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/error%20during%20build%20and%20push%20frontend%20docker.JPG)  
> **During Build and Push unable to locate Dockerfile**

*Day 16(7/8)* The most successful day of this internship!! Launched RStudio-verse:latest container to DockerHub. Proceeded to use GitHub Actions and launched the rest of the versions of rstudio-verse to DockerHub. Still facing problems with one of the versions of RStudio-verse(3.6.3). Think the problem might be in the Dockerfile and not the .yml file because the code exits at a certain step in the Dockerfile. Was also able to launch all three versions of JuptyerLab to Docker using GitHub Actions under one .yml file. 
![alt text](https://raw.githubusercontent.com/shrutir11/KEYS/main/images/all%20three%20versions%20in%20dockerhub.JPG)  
> **All three tagged versions of JupyterLab pushed to Docker using one .yml file**

*Day 17(7/9)* Read this [page] (https://docs.github.com/en/actions/reference/events-that-trigger-workflows) and learned how to schedule automatic workflow builds. Tested this by setting a time on Friday and seeing if it worked. It worked. Then scheduled the actual automatic build to take place every Saturday at 12:00 UTC time.
