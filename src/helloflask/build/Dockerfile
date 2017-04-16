FROM python:2.7

## make a local directory
RUN mkdir /opt/helloflask

# set as the working directory from which CMD, RUN, ADD references
WORKDIR /opt/helloflask

# copy the local requirements.txt to the directory
ADD requirements.txt .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# now copy all the files in this directory to /helloflask directory
ADD . .

# Listen to port 5000 at runtime
EXPOSE 5000

# Define our command to be run when launching the container
CMD ["python", "helloflask.py"]
