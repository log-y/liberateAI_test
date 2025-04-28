# liberateAI_test

Hey, these are the instructions and notes on how to get the script up and running.

# Conda and script
I got it to run just now by doing these instructions:
Open a new conda environment and install everything in requirements.txt. Install ffmpeg (using sudo apt). Running dg.py

# Some other notes:
You may need to set up Docker first before it runs (should be an error message that says "docker isn't found" for this). I used these instructions to open that up: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository. It uses these instructions to set up docker (I copy and pasted from the official documentation).

# Docker
Then, you may need to give Docker some permissions using: "sudo usermod -aG docker $USER". If you do that, you would likely need to restart whatever machine you're on (I was on the Windows Linux Subsystem, so I just did "exit" and "wsl", but I'm not too sure what it's like with EC2 instances)

# Misc
I also remember that the original files may have gotten nested somewhere an additional numbers of time (if you see an error message like /gb-hilab-suite/some-file not found), so you may need to extract the inner files to its immediate parent's directory using a mv command. You may also encounter a WORK_PATH undefined error, in which case, you can set that path to really anywhere (I used my Desktop) using something like "export WORK_PATH=/mnt/c/Users/logan/Desktop".

# End
And yeah! That's generally it. Lmk if I can help with any issues that may arise. The first time it runs, it will take a while to run (~10 mins on my computer). But after that, it should be much faster.
