import os
import sys
from urllib.request import urlretrieve

# Load documents
os.makedirs("data", exist_ok=True)
files = [
    "https://docs.aws.amazon.com/bedrock/latest/studio-ug/bedrock-studio-user-guide.pdf"
]
for url in files:
    file_path = os.path.join("data", url.rpartition("/")[2])
    urlretrieve(url, file_path)
