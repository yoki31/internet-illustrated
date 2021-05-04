import hashlib, io, signal, time, os
from glob import glob
import requests

from PIL import Image
from selenium import webdriver

number_of_images = 400
GET_IMAGE_TIMEOUT = 2
SLEEP_BETWEEN_INTERACTIONS = 0.1
SLEEP_BEFORE_MORE = 5
IMAGE_QUALITY = 90

output_path = ""
