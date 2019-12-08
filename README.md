# PwdCrackerPerformance

This Repository consists of the files required to run performance tests in the comparison of CPU vs GPU Password cracking.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Download HashCat binaries found here:

```
https://hashcat.net/hashcat/
```

### Installing

To set up the environment, you only need the installation of HashCat as well as the provided hash files provided in the repository.

For this tests we will be using HashCat Version 5.1.0
First, download and unzip the HashCat binaries folder.


```
hashcat-5.1.0
```

Then, download and unzip this repository.

```
PwdCrackerPerformance-master
```

From here, you have two options to perform the tests.
The first option is to run the provided python code:

```
HashingProgram.py
```
This will create new hashes and store them in text files correctly named by the length of the password and hashing used.

The second option is to copy the text files provided in the repo and paste them into the HashCat binaries folder.

After this, the environment is set-up for the tests.

## Running the tests

To run the tests, very specific commands have to be used.

First open the windows command line and navigate to the HashCat binaries folder where you have the hash text files.

To start, we will run the first text file provided called:

```
MD5hashes6.txt
```

To do this, first write the following command:

```
.\hashcat64.exe -a 3 -m 0 md5hashes6.txt ?l?l?l?l?l?l --force
```

After the run completed, run the following command:

```
.\hashcat64.exe -a 3 -m 0 -1 ?l?d?u md5hashes6.txt ?1?1?1?1?1?1 --force
```

You'll notice that the first hashes are ignored since they have already been cracked and cached in the program.

Similarly, after the second test is compleated, run the following command:

```
.\hashcat64.exe -a 3 -m 0 md5hashes6.txt ?a?a?a?a?a?a --force
```

To gather the complete results from the project, those 3 steps were repeated for all the different lengths and hashing algorithms. 




## Authors

* **Daniel Alfaro R.** - *ReadMe* - [Daniel Alfaro R.](https://github.com/danyalfaro)



