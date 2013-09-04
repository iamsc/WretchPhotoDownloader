import urllib2
import glob
import os

if (os.name == "posix"):
    relativePath = "."
elif (os.name == "nt"):
    relativePath = ".."

albumLists = glob.glob(os.path.join(relativePath, '*.txt'))
errorURLLists = []
correctURLLists = []

for album in albumLists:

    directoryName = os.path.join(relativePath, os.path.basename(album).split('.')[0])
    print "\nCreating the new folder: " + directoryName
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)

    print "To prepare the photo lists of album: " + directoryName
    with open(album) as f:
        lines = f.readlines()
        photoLength = len(lines)
        i = 0
        for url in lines:
            i = i + 1
            print "Progress: " + str(i) + " / " + str(photoLength)
            if (url.find("http") > -1):
                try:
                    urlContent = urllib2.urlopen(url)
                    urlName = url.split('/')[-1].split('?')[0]
                    data = urlContent.read()
                    with open(os.path.join(directoryName, urlName), "wb") as code:
                        code.write(data)
                    correctURLLists.append(url)
                except urllib2.URLError:
                    print "Download failed: " + url
                    errorURLLists.append(url)


correntNumber = len(correctURLLists)
errorNumber = len(errorURLLists)
print "\n***** The photos are downloaded. *****"
print "The total number of photos: " + str(correntNumber + errorNumber) + " photos."
print "Succeeded: " + str(correntNumber) + " photos."
print "Failed: " + str(errorNumber) + " photos."
print "\nThe failed URLs are listed below:"
for errorURL in errorURLLists:
    print errorURL

os.system("pause")