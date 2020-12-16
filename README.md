# Discord-Uploader

This script can be used to upload files directly to a Discord channel using a channel's webhook address. A quick guide on how to create a webhook for use with this script can be found on the Discord support page on their [Intro to Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) page.

## Installation

This script requires python to be installed. A good walkthrough on how to do this can be found on [Real Python](https://realpython.com/installing-python/) and it includes instructions on how to install python on various operating systems.

Once python is installed, either clone the repo or download the project as a zip and extract it to where you would like to run it from. Make a copy of `sample_env` and rename this new file to `.env`. Update the variables in this file to match your configuration (e.g. webhook id, webhook token, and the location of the file you wish to upload).

This script requires the use of the discord python library. To install this library, open a command prompt and navigate to where you have the script located and use the `requirements.txt` file to install the needed library (for this example, we have this script located in our user folder).

```
cd %userprofile%\Discord-Uploader
pip install -r requirements.txt
```

## Run the script

Now all that is needed is to run the script. This can be done manually either directly from file explorer or via command line (`python %userprofile%\Discord_Uploader\file_uploader.py`). This can also be scheduled to run automatically using Windows Task Scheduler.
