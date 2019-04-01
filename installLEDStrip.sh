sudo apt-get install build-essential python-dev python-pip unzip wget scons swig

cd /tmp
wget https://github.com/jgarff/rpi_ws281x/archive/master.zip && \
     unzip master.zip && \
     cd rpi_ws281x-master && \
     sudo scons

pip install rpi_ws281x

