# HW 0

* Assigned: Sep 9
* Due: 9/14 10AM
Oh hi



The goal of this assignment is for you to set up Microsoft Azure.

Many of the assignments in this class will use Microsoft's cloud computing
infrastructure.  Using a cloud service like Microsoft (or Amazon, etc) makes it easy to
share data sets, and quickly run any number of virtual machines that are
identical for all students in the class.  We have credits from Azure,
which we will use for this class (in this homework, we will use a free
"micro" instance.)


<span style="color:#ff5511">**Caution: allocating and running services (e.g., virtual machines) on any cloud provider
  costs money or credits.  It can be _very_ easy to spend more than you anticipated by leaving your services
  running.  Make it a habit to stop your services when not in use.  If you run out of credits,
  there's not much we (the staff) can do.**</span>

## Sign up and setup the OS

**Signup**

[register for an account](http://azure.microsoft.com/en-us/offers/ms-azr-0044p/)

You may be asked to submit your credit card information for screening purposes, however _you will not be charged_ as
the service will stop your account if your trial credits are used up.
Once the class registration has settled down, we can provide you with information to use the class's Azure credits.


**Launch an instance**

1. Go to [https://manage.windowsazure.com/](https://manage.windowsazure.com)
2. Click "NEW" in the bottom left of the screen
3. Click "Compute", then "Virtual Machine", then "Quick Create"
4. In DNS Name, provide a name for your new machine/website
5. In Image, pick **Ubuntu Server 14.04 LTS**
6. In Size, pick **D1 (1 core, 3.5 GB Memory)**
7. Pick a username and password and remember them
8. In Region, you can optionally pick East US or East US 2.  It will allocate your machine in a data center on the East Coast, so latency to the VM should be faster.
9. Click "Create Virtual Machine" and wait a couple minutes for it to launch.
1. Click on "Virtual Machines" in the main left panel to see your VMs
2. Once the VM has started, click on it, then click on the "Dashboard" tab
3. You should see your machine's DNS Name as <name you picked>.cloudapp.net.  **this is your public address**


**SSH to Your Instance**

Using a terminal program (e.g, MacOS Terminal, or an xterm on Athena, or a Cygwin terminal under windows), type:

    ssh <username>@<vm name>.cloudapp.net

It will ask for your password, once you enter you should see something like:

    Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.19.0-25-generic x86_64)

    * Documentation:  https://help.ubuntu.com/

    System information as of Wed Aug 19 04:28:23 UTC 2015

    System load:  0.27              Processes:           107
    Usage of /:   4.1% of 28.80GB   Users logged in:     0
    Memory usage: 4%                IP address for eth0: 10.0.0.4
    Swap usage:   0%

    Graph this data and manage this system at:
    https://landscape.canonical.com/

    Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud


    Last login: Wed Aug 19 04:28:23 2015 from columbia.edu
    eugenewu@ewutest:~$

**Setup the OS**

Ensure the following packages are available using the Ubuntu package management tool _apt-get_.  

To install a package, type:

    sudo apt-get install <packagename1 packagename2 ...>

Make sure you have the following packages:

* python2.7
* python-pip
* postgresql-9.3
* postgresql-client-9.3
* postgresql-server-dev-9.3
* libpq-dev
* python-dev
* sqlite3
* git


**Setup Python**: 

Python uses its own package manager to install/update/remove packages.  In general, the following installs python packages:

    pip install <packagename>
    
Typically the package manager will require `sudo` and install the packages in a global folder that affects everyone using your machine.  This is bad hygiene because different python applications may use different versions of packages and it's easy to step on each other's toes.  

We will use `virtualenv` to create virtual environments that contain their own copies of `python` and packages.  When we work in a virtual environment, pip will install packages local to the environment rather than globbaly.  You can read [a detailed tutorial](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
    
Lets setup your environment

1. Install `virtualenv` and convenience libraries in `virtualenvwrapper` (this is the one time you should install globally)

        sudo pip install virtualenv virtualenvwrapper
2. add the wrapper commands (you may add this line in ~/.bashrc so it runs when you create a bash shell)

        source /usr/local/bin/virtualenvwrapper.sh
3. create a new environment (will create a folder `test/` in `~/.virtualenvs/`)

        mkvirtualenv test
4. switch (activate) an environment by using `workon`

        workon test
        
5. switch out of an environment:
        
        deactivate


Now let's install a set of useful packages into your environment:
   
1. Activate your environment (see above)
2. install the following packages using `pip` (see above)
    * flask
    * psycopg2
    * sqlalchemy
    * click
3. Deactivate and you're done
      
  

**Sign up for GitHub**

GitHub is a source control repository website that many in industry use to manage their projects.
In fact, this class is organized as repositories under the organization 4111: http://www.github.com/w4111.  
Each assignment is managed as a separate repository. 
As the course progresses, more repositories will be made available. 

[Go sign up for an account](https://help.github.com/articles/signing-up-for-a-new-github-account)

**Checkout the homework 0 repository**

To work on an assignment, it's a good idea to "fork" the repository into your own
GitHub account and complete the assignment there.  Let's try this with the homework
0 repository at https://github.com/w4111/hw0

1. To start, [fork the repository](https://guides.github.com/activities/forking/)
1. [Clone](http://gitref.org/creating/#clone) the repository to your Azure VM
1. Once you modify your files, [commit](http://gitref.org/basic/#commit) the changes.
1. If you want to share it with a teammate, or just want to make sure GitHub has a copy of your files in case
   the VM crashes, [Push](http://gitref.org/remotes/#push) the changes to GitHub.
1. If your teammate pushed to the same repository on GitHub, pull the changes from GitHub by typing within the repository:

        git pull


## Test that things worked

Let's make sure you have access to Python, sqlite3, and the git repository.

**Python**

Type `python` and ensure that you see the following like (the Python version may be slightly different 2.7.X):

    Python 2.7.4 (default, Apr 19 2013, 18:28:01) 
    [GCC 4.7.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Then try importing some modules from the packages we installed

    >>> import flask
    >>> import psycopg2
    >>> import sqlalchemy
    >>> import click

If that worked, push `ctrl+d` to exit the prompt.

**sqlite3**

SQLite is an "embedded" SQL database (it doesn't depend on a dedicated server process;  instead the client just manipulated a stored
datbase file directly.)

To ensure it is installed, type `sqlite3` and verify that you see the following:

    SQLite version 3.7.15.2 2013-01-09 11:53:05
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite>

If you do, push `ctrl+d` to exit the prompt.

**PostgreSQL**

We will use the PostgreSQL DBMS in this class.  Check that the client program works:

    psql --version

If it prints something like the following then it works
   
    psql (PostgreSQL) 9.3.9
    

**git repository**

Type `cat hw0/README.md` 

You should see the instructions for this hw fly by.


    

<!--
**(Optional) PostgreSQL using Amazon RDS**

PostgreSQL is an open source standalone database server (a DBMS!)  
Amazon provides a **cloud database service** that makes it easy to 
start and access a PostgreSQL (or MySQL, etc) database without the hassle
of installation.  If you have an Amazon AWS account or a trial account, you can setup your own database on Amazon.  **This is compeletly optional because Amazon asks for your credit card information**

Set it up by logging into your [aws.amazon.com](http://aws.amazon.com) account and following
[**the instructions**](./rdssetup.pdf).  

If you can run `psql` and access your RDS database, then push `ctrl+d` to exit the `psql` prompt.
-->


## Perform some data analysis

To complete this homework, go into your `hw0/` directory.  There should be a file called
`iowa-liquor-sample.csv`.  The state of Iowa [released](https://data.iowa.gov/Economy/Iowa-Liquor-Sales/m3tr-qhgy)
a dataset containing all sales transactions at alcoholic beverage stores during 2014.    We will use
this dataset for many assignments in this course.  Since it contains over 3 million records, this is
a small sample.

**Disclaimer: this course does not condone drinking, we are using this dataset because it is a common format
  for a sales transaction log in a silghtly more accessible domain than typical bank transactions**

Write a python script that reads the file and computes the number of records 
(in this file, each line is a record) that contain the exact case insensitive phrase "single malt scotch".
Ignore upper and lower casing, so "Single Malt Scotch", and "SINGLE Malt Scotch" all match, whereas
"Single's Malty Scootch" does not.



## Submitting your work

Submit your assignment at http://goo.gl/forms/YzQ1DwHzMy

**Note that you must be logged in to Columbia's lionmail to submit, and we will only consider your _first_ submission**.


<!--You should create a text (.txt) file with the following format:

    <YOURNAME>
    <Student UNI>
    <# of single malt scotch records>
    <your python program>

For example:

    Eugene Wu
    ew2493
    9
    import sys
    num_whiskies = 0
    num_whiskies += 9
    print num_whiskies

Upload it to the [coureworks website](http://courseworks.columbia.edu/) as the "hw0" assignment.
-->

Whew, you're almost done!  Go read the assigned readings.

You can always send us questions on [Piazza](https://piazza.com/class/id26ml2f2m0ju)!




## Stop your virtual machine

While your free trial is pretty good,  it's very easy to accidentally use up all of your credits (including those the course will provide you).
To conserve your hours (and avoid wasting energy), make sure to turn off your machine **whenever you are not using it**. 

1. Go to the [Azure Console](https://manage.windowsazure.com/).
1. In the left panel, click on "Virtual Machines"
2. Select your VM
3. Click "Shut Down" in the menu at the bottom of the screen
4. To resume the VM,  click "Start" in the menu
5. Before doing future assignments, you'll have to follow these instructions and choose "Start" to restart your instance.  Note that Shutting down and Starting the instance will potentially change the "Public DNS" value for that instance, however the URL <name>.cloudapp.net will stay the same.

