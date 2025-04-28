# liberateAI_test

Hey, these are the instructions and notes on how to get the script up and running.

# Conda and script
I got it to run just now by doing these instructions:
Open a new conda environment and install everything in requirements.txt.
Install ffmpeg (using sudo apt)
Running dg.py

# Some other notes:
You may need to set up Docker first before it runs (should be an error message that says "docker isn't found" for this). I used these instructions to open that up: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository 
It uses these instructions to set up docker (copy and pasted from the official documentation):

sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

Then, you may need to give Docker some permissions using:
sudo usermod -aG docker $USER 
If you do that, you would likely need to restart whatever machine you're on (I was on the Windows Linux Subsystem, so I just did "exit" and "wsl", but I'm not too sure what it's like with EC2 instances)

I also remember that the original files may have gotten nested somewhere an additional numbers of time (if you see an error message like /gb-hilab-suite/some-file not found), so you may need to extract the inner files to its immediate parent's directory using a mv command.

And yeah! That's generally it. Lmk if I can help with any issues that may arise.
