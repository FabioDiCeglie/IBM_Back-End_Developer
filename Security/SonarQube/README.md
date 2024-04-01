# STATIC CODE ANALYSIS

We will use the PostgreSQL database by pulling its docker image. Before we do that, we will need a Docker network to connect the database to SonarQube and, later, the SonarScanner. This will be your first task.

``` docker network create mynet ```

``` docker run --name postgres  -e POSTGRES_USER=root -e POSTGRES_PASSWORD=Test12345  -p 5432:5432 --network mynet -d postgres ```


Now that we have the PostgreSQL database running, we can create the SonarCube server and attach it to the database. To avoid having to install SonarQube and have the proper Java environment to run it, you will use a Docker container for running your SonarQube server. Luckily, SonarQube provides one that you can use.

``` docker run -d --name sonarqube -p 9000:9000 -e sonar.jdbc.url=jdbc:postgresql://postgres/postgres -e sonar.jdbc.username=root -e sonar.jdbc.password=Test12345 --network mynet sonarqube ```

# Check

``` docker ps ```

# Lunch SonarQube

# Login

username: admin
password: admin

# Create a SonarQube Project ( Manually )

 - Project: temp
 - Project key: temp
 - Main branch name: main

# Use gobal setting

# Use Locally

# Generate SonarQube Scanner Token

# Ready the SonarQube Scanner

It is important to understand that the SonarQube server that stores the results of scans is separate and distinct from the SonarQube scanner which performs the actual scanning. Up until now, we’ve created a database for storing the analysis results and provisioned a SonarQube server for serving the UI.

To get the SonarQube scanner to work in the Cloud IDE, you can either install it locally or pull its docker image and run its docker container.

``` docker pull sonarsource/sonar-scanner-cli ```

Run the following bash alias command in the terminal, which creates an alias sonar-scanner for running the scanner later using the scanner-cli docker container:

``` alias sonar-scanner='docker run --rm -v "$(pwd):/usr/src" sonarsource/sonar-scanner-cli' ```

Note: This command is mounting the current working directory as a volume at /usr/src inside the container, which is where sonar-scanner is looking for the source code. You can set this up on your own computer as well.

Any arguments that you pass into the sonar-scanner command will be passed into the container version as well. This is how you can easily run commands in Docker containers as if they were actually installed on your computer.

# Test project

``` git clone https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git ```

``` cd wtecc-CICD_PracticeCode ```

# SCAN

``` 
sonar-scanner
  -Dsonar.projectKey=temp 
  -Dsonar.sources=. 
  -Dsonar.host.url=https://dcfabio96-9000.theiadocker-2-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai 
  -Dsonar.token=sqp_5c0de4a6694602ee6cd7be3353424f951948c700

```

# Check the scan results and fix the issues