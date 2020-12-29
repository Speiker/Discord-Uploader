# Discord-Uploader

This script can be used to upload files directly to a Discord channel using a channel's webhook address. A quick guide on how to create a webhook for use with this script can be found on the Discord support page on their [Intro to Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) page.

## Installation

This script requires python to be installed. A good walkthrough on how to do this can be found on [Real Python](https://realpython.com/installing-python/) and it includes instructions on how to install python on various operating systems.

This script makes use of the discord and python-dotenv python libraries. To install these, open a command prompt and enter the following command:
```
pip install discord python-dotenv
```

Once python and the required libraries are installed, either clone the repo or download the project as a zip and extract it to where you would like to run it from.

## Run the script

Now all that is needed is to run the script. This can be done either directly from file explorer or via command line (`python path\to\script\file_uploader.py`). When run initially the script will prompt for the webhook id and token, as well as the location of the file you wish to upload. Upon successful upload, these values will be stored in a .env file in the same directory as the script. The script can be run manually at this point without user input or can be scheduled to run automatically using Windows Task Scheduler.
