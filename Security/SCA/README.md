# Installing the OWASP SCA Tool

``` wget -O dependency-check.zip https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0267EN-SkillsNetwork/labs/module2/data/dependency-check.zip && unzip dependency-check.zip && chmod +x dependency-check/bin/dependency-check.sh && sudo echo "alias dependency-check=$(pwd)/dependency-check/bin/dependency-check.sh" >> ~/.bashrc && source ~/.bashrc ```

Now you'll be able to run the OWASP SCA tool using ``` dependency-check  ``` on the command line.

# Source code

``` git clone https://github.com/juice-shop/juice-shop.git ```

# Run SCA on Juice Shop Components

``` dependency-check -f JSON --prettyPrint --scan juice-shop ```

The command will produce a file called dependency-check-report.json which may contain information about any vulnerable components found by the OWASP SCA Tool.

# Creating an HTML report

``` dependency-check --scan juice-shop ```