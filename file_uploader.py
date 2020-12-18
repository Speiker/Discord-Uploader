#!/usr/bin/python

import os
from pathlib import Path
from discord import Webhook, RequestsWebhookAdapter, File
from dotenv import load_dotenv


def main():
    # Load variables from .env. If file doesn't exist query user.
    options_file = Path(".env")
    if options_file.is_file():
        load_dotenv()
        WEBHOOK_ID = os.getenv("WEBHOOK_ID")
        WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN")
        UPLOAD_FILE = os.getenv("UPLOAD_FILE")
    else:
        WEBHOOK_ID, WEBHOOK_TOKEN, UPLOAD_FILE = define_options()

    # Upload file to server. Use a try for error handling of input errors
    try:
        webhook = Webhook.partial(
            WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter()
        )

        webhook.send(file=File(Path(UPLOAD_FILE)))

        # If .env doesn't exist write it for use on next run
        if not options_file.exists():
            with open(".env", "w") as f:
                f.write(
                    f'# .env\n\nWEBHOOK_ID="{WEBHOOK_ID}"\n'
                    f'WEBHOOK_TOKEN="{WEBHOOK_TOKEN}"\n'
                    f'UPLOAD_FILE="{UPLOAD_FILE}"'
                )
    except ValueError:
        print("\nInvalid Webhook ID. Try again.\n\n\n")
        main()
    except FileNotFoundError:
        print(
            "\nNo such file to upload. Please check the path and filename.\n\n\n"
        )
        main()
    except Exception as e:
        print(f"\n{e}\n\n\n")
        main()


def define_options():
    response = (
        "ID and Token values are pulled from the webhook URL for a discord channel\n"
        "Example URL - discordapp.com/api/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN"
    )
    print(response)
    WEBHOOK_ID = input("Webhook ID: ")
    WEBHOOK_TOKEN = input("Webhook token: ")

    UPLOAD_FILE = Path(input("\nPath to file you wish to upload: "))

    return WEBHOOK_ID, WEBHOOK_TOKEN, UPLOAD_FILE


if __name__ == "__main__":
    main()
