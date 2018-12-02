from TwitterAPI import TwitterAPI
from random import randint
import time
import sys


def AutoPostPics(nb_pics):
        #Incrementation of the pics
        nb_pics += 1

        if nb_pics > 334:
                sys.exit(1)

        #Directory of your bank of pics/gif
        fichier = '/home/pi/Desktop/PICS/'

        #Random post at any time of the journey between 7200 = 2H and 86400 = 24H
        rand = randint(7200, 86400)
        print(rand)

        #Shell Display
        i = 1
        for i in range(rand):
                print(str(i) + "/" + str(rand), end='\r')
                time.sleep(1)

        #Selection of the pics
        file = open(fichier + 'pics(' + str(nb_pics) + ').jpg', 'rb')
        data = file.read()

        #Post the pics : You can change status:'Your text before the pictures'
        r = api.request('statuses/update_with_media', {'status':''}, {'media[]':data})

        #State(200 = ok)
        print(r.status_code)

        #ReCall of the function
        AutoPostPics(nb_pics)

#end AutoPostPics


### MAIN ###
if __name__=='__main__':

        #Variables Fixe
        CONSUMER_KEY = '<YOUR_CONSUMER_KEY>'
        CONSUMER_SECRET = '<YOUR_CONSUMER_SECRET>'
        ACCESS_TOKEN_KEY = '<YOUR_ACCES_TOKEN_KEY>'
        ACCESS_TOKEN_SECRET = '<YOUR_ACCES_TOKEN_SECRET>'

        api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

        nb_pics = 0

        #Call of the function
        AutoPostPics(nb_pics)

#end MAIN
