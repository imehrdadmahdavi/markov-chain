"""
Retrieve the text, store and clean data
"""
import urllib2

def retr():
    base_url = "http://www.gutenberg.org/cache/epub/13060/pg13060.html"
    file_name_raw = "gulistan-raw.txt"
    response = urllib2.urlopen(base_url)
    html = response.read()

    words = html.split(' ')

    print "Retrieving data from %s ..." % base_url
    f = open(file_name_raw, "w+")
    print "Writing raw data to %s ..." % file_name_raw
    for item in words:
        f.write(str(item) + "\n")
    f.close()
    print "Raw data was written in %s successfully!" % file_name_raw