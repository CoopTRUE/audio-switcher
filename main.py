import sounddevice as sd
import os
import zipfile
import requests
import subprocess
from tqdm import tqdm

TOGGLE = ["Headphones", "Speakers"]


def download_and_extract_nircmdc():
    if os.path.exists("nircmdc.exe"):
        return
    response = requests.get("https://www.nirsoft.net/utils/nircmd-x64.zip", stream=True)
    total_size = int(response.headers.get("content-length", 0))

    with open("nircmd-x64.zip", "wb") as f, tqdm(
        desc="Downloading nircmdc.exe",
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            bar.update(len(data))
            f.write(data)

    with zipfile.ZipFile("nircmd-x64.zip", "r") as zip_ref:
        zip_ref.extract("nircmdc.exe")
    os.remove("nircmd-x64.zip")


def get_devices():
    devices = sd.query_devices()
    return [
        device
        for device in devices
        if device["max_output_channels"] > 0 and device["hostapi"] == 0
    ]


def get_current_device_name():
    devices = get_devices()
    current_device_index = sd.default.device[1]
    for device in devices:
        if device["index"] == current_device_index:
            return device["name"].split(" ")[0]
    raise Exception("Current device not found")


def get_other_device_name():
    current_device_name = get_current_device_name()
    return TOGGLE[0] if current_device_name == TOGGLE[1] else TOGGLE[1]


def set_device(device_name):
    subprocess.run(["nircmdc.exe", "setdefaultsounddevice", device_name])


def toggle_device():
    current_device_name = get_current_device_name()
    other_device_name = get_other_device_name()
    set_device(other_device_name)
    print(f"[{current_device_name}] -> [{other_device_name}]")


if __name__ == "__main__":
    download_and_extract_nircmdc()
    toggle_device()
