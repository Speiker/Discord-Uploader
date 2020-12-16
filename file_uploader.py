#!/usr/bin/python

import os
from discord import Webhook, RequestsWebhookAdapter, File
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()
WEBHOOK_ID = os.getenv("WEBHOOK_ID")
WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN")
UPLOAD_FILE = os.getenv("UPLOAD_FILE")

webhook = Webhook.partial(
    WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter()
)

webhook.send(file=File(UPLOAD_FILE))
