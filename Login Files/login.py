# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:33:19 2020

@author: benhawk1
"""
#This tool provides a login loop for users. An individual will enter their username and password.
#The program will search a csv file of users for the specified username. If it is found,
#It will hash the given password and compare it to the password on record. If it is identical,
#The user is accepted into the program. If not, the user is asked to enter new information
import pandas as pd
import numpy as np
from pymongo import MongoClient
import hashlib
import os

#Function that checks if the user's login information is accurate
def loginValidation(username, password, df):
    valid = False
    userExists = df['Username'].isin([username]).any()
    if userExists == True:
        rowNum = int(df[df['Username'] == username].index[0])
        valid = hashing(password,rowNum,df)
    return valid

#All passwords use the same salt, may want to change
#Hashes the specified password and checks if it is on file
def hashing(password,row,df):
    salt = b'1\xcc\xf09V\x1b\xed\xf5\x87\x13p\xe7/3ZA\x80\xdfN\t\xd1P\xa1\xf9\x95\xc7T\xfe\x19\xa0\xd4\x0b'
    key = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000,dklen=128)
    if str(key) == df.at[row,'Key']:
        return True
    else:
        return False
    
    
    
#Reads in a csv file of users, replace the string with the desired path
loginInfo = pd.read_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv")

#Receives an initial set of login information from the user.
username = input("Hello User. Please Enter Username: ")
password = input("Please enter password: ")
check = loginValidation(username,password,loginInfo)

#Loops user input while incorrect information is provided
while check != True:
    username = input("Incorrect login information. Please enter a new username: ")
    password = input("Please enter password: ")
    check = loginValidation(username,password,loginInfo)
print("Welcome " + username + "!")

#Sets variables for the user once they are logged in
password = 0
rowNum = int(loginInfo[loginInfo['Username'] == username].index[0])
role = loginInfo.at[rowNum,'Role']

if role == 'S':
    print('You are a student.')













    
