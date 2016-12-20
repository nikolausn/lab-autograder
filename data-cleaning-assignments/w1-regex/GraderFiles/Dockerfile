# Fetch python docker image
FROM python:latest

# Make a directory where your files will be stored
RUN mkdir /grader
RUN mkdir /grader/01_email

# Below commands copy the files that you need to put in your docker image

COPY executeGrader.sh /grader/executeGrader.sh
#COPY Grader.java /grader/Grader.java

# Copy files for Regex Grader
COPY 01_email/* /grader/01_email/

# Copy files for OpenRefine Grader
#COPY OpenRefineGrader/* /grader/OpenRefineGrader/

# Important: Docker images are run without root access on our platforms. Its important to setup permissions accordingly.
# Executable permissions: Required to execute executeGrader.sh
# Read permissions: Required to read testCases.txt, solution.txt, Grader.java
# Write permissions: Required to store the compiled java files
RUN chmod a+rwx -R /grader/

# Setup the command that will be invoked when your docker image is run.
ENTRYPOINT ["./grader/executeGrader.sh"]

# While running the graders in production, Coursera passes several command line arguments to the ENTRYPOINT command
# in no particular order. For local testing, the below commands can be used in place of the above ENTRYPOINT command 
# to simulate passing command line arguments to executeGrader.sh.
# More details about these Coursera supplied command line parameters can be found in executeGrader.sh.

# Command to simulate Factoring Grader:
# ENTRYPOINT ["./grader/executeGrader.sh", "partId", "HxbKF"]
# Command to simulate Prime Grader:
# ENTRYPOINT ["./grader/executeGrader.sh", "partId", "ov8KA"] 
