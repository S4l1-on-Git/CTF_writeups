import base64
import json
import os

import requests
from PIL import ImageChops,Image
import PIL
import cv2
import imutils
import numpy as np
import imagehash
#from math import abs

eps=1000


token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkX2F0IjoiMjAyNi0wNC0yNFQxNjowNjoyNC42NzA5NTQrMDA6MDAiLCJlbWFpbCI6InNlaWZhcnNlbGFuQGdtYWlsLmNvbSIsImV4cCI6MTc3NzEzMzQwMCwiaWF0IjoxNzc3MDQ3MDAwLCJzdWIiOiI0In0.7_y7kIdOWCgl-FqH-97Q5tRPSjmnga7SX590tqSI7OM"

height = 320
def compare(image1, image2) :
    
    rotated = image2
    pixels = image1.load()
    pixels2 = rotated.load()

    #
    currMax = 10000000000000
    curr = 0
    diff = 0
    for i in range(height):
        for j in range(height):
            diff += ((pixels[i,j][0]-pixels2[i,j][0])**2) + ((pixels[i,j][1]-pixels2[i,j][1])**2) + ((pixels[i,j][2]-pixels2[i,j][2])**2)
    
    if (diff<=currMax) :
        curr = 0
        currMax = diff
    
    
    rotated = image2.transpose(PIL.Image.ROTATE_90)
    pixels2 = rotated.load()
    diff = 0
    for i in range(height):
        for j in range(height):
            diff += ((pixels[i,j][0]-pixels2[i,j][0])**2) + ((pixels[i,j][1]-pixels2[i,j][1])**2) + ((pixels[i,j][2]-pixels2[i,j][2])**2)
    
    if (diff<=currMax) :
        curr = 270
        currMax = diff
    
    
    
    rotated = image2.transpose(PIL.Image.ROTATE_180)
    pixels2 = rotated.load()
    diff = 0
    for i in range(height):
        for j in range(height):
            diff += ((pixels[i,j][0]-pixels2[i,j][0])**2) + ((pixels[i,j][1]-pixels2[i,j][1])**2) + ((pixels[i,j][2]-pixels2[i,j][2])**2)
    
    if (diff<=currMax) :
        curr = 180
        currMax = diff
    
    
    rotated = image2.transpose(PIL.Image.ROTATE_270)
    pixels2 = rotated.load()
    diff = 0
    for i in range(height):
        for j in range(height):
            diff += ((pixels[i,j][0]-pixels2[i,j][0])**2) + ((pixels[i,j][1]-pixels2[i,j][1])**2) + ((pixels[i,j][2]-pixels2[i,j][2])**2)
    
    if (diff<=currMax) :
        curr = 90
        currMax = diff
    
    
    return curr



"""def compare(image1, image2,j):
    path = "/home/s4l1/ingeHack/Board_Puzzle/test/"
    rotated = image2
    rotated.save("/home/s4l1/ingeHack/Board_Puzzle/test/test" +str(j) +"0.jpeg")
    
    rotated = image2.transpose(PIL.Image.ROTATE_180)
    rotated = rotated.transpose(PIL.Image.ROTATE_180)
    hash1 = imagehash.average_hash(image1)
    hash2 = imagehash.average_hash(rotated)
    print(hash1)
    print(hash2)
    print()
    
    minHash = 360
    minimum = 1111
    minimum = min(minimum,abs(hash1-hash2))
    if (abs(hash1-hash2)<=minimum) :
        minHash = 0;
    rotated = image2.transpose(PIL.Image.ROTATE_90)
    rotated.save("/home/s4l1/ingeHack/Board_Puzzle/test/test" +str(j) +"1.jpeg")
    hash1 = imagehash.average_hash(image1)
    hash2 = imagehash.average_hash(rotated)
    print(hash1)
    print(hash2)
    print()
    minimum = min(minimum,abs(hash1-hash2))
    if (abs(hash1-hash2)<=minimum) :
        minHash = 90;
    rotated = image2.transpose(PIL.Image.ROTATE_180)
    rotated.save("/home/s4l1/ingeHack/Board_Puzzle/test/test" +str(j) +"2.jpeg")
    hash1 = imagehash.average_hash(image1)
    hash2 = imagehash.average_hash(rotated)
    print(hash1)
    print(hash2)
    print()
    minimum = min(minimum,abs(hash1-hash2))
    if (abs(hash1-hash2)<=minimum) :
        minHash = 180;
    rotated = image2.transpose(PIL.Image.ROTATE_270)
    rotated.save("/home/s4l1/ingeHack/Board_Puzzle/test/test" +str(j) +"3.jpeg")
    hash1 = imagehash.average_hash(image1)
    hash2 = imagehash.average_hash(rotated)
    print(hash1)
    print(hash2)
    print()
    minimum = min(minimum,abs(hash1-hash2))
    if (abs(hash1-hash2)<=minimum) :
        minHash = 270;
    return minHash"""


def objecttoimages(qq,name):
    

    D = qq["puzzle"]["tiles"]

    for i in range(len(D)) :
        D[i] = D[i].replace("data:image/jpeg;base64,","")
        filename = "/home/s4l1/ingeHack/Board_Puzzle/" + name + str(i) + ".jpeg"
        D[i] = base64.b64decode(D[i])
        f = open(filename,"wb")
        f.write(D[i])
        f.close()

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
    
response = requests.post('https://board-puzzles.ctf.ingeniums.club/api/levels/2/start', auth=BearerAuth('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkX2F0IjoiMjAyNi0wNC0yNFQxNjowNjoyNC42NzA5NTQrMDA6MDAiLCJlbWFpbCI6InNlaWZhcnNlbGFuQGdtYWlsLmNvbSIsImV4cCI6MTc3NzEzMzQwMCwiaWF0IjoxNzc3MDQ3MDAwLCJzdWIiOiI0In0.7_y7kIdOWCgl-FqH-97Q5tRPSjmnga7SX590tqSI7OM'))
#print(response)

response_dict = json.loads(response.text)
objecttoimages(response_dict,"tmp/tmp")

np.bitwise_xor
"""check part"""
path1 = "/home/s4l1/ingeHack/Board_Puzzle/pumpkin"
path2 = "/home/s4l1/ingeHack/Board_Puzzle/tmp"

list = []
for i in range(36):
    image1 = Image.open(path1 + "/tmp" + str(i) + ".jpeg")
    image2 = Image.open(path2 + "/tmp" + str(i) + ".jpeg")
    #print((360-compare(image1,image2))%360)
    list.append((compare(image1,image2))%360)

print(str(list).replace(' ',''))