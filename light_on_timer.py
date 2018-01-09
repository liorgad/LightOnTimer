from infiniteTimer import InfiniteTimer
import sys
import httplib
import urllib
import time


url = "192.168.10.15"
port = "8081"
name_parameter = "on"

class URL:

    def __init__(self, host, port=None, path=None, params=None):
        self.host = host
        self.port = port
        self.path = path
        self.params = params

    def __str__(self):
        url = "http://" + self.host
        if self.port is not None:
            url += ":" + self.port
        url += "/"
        if self.path is not None:
            url += self.path
        if self.params is not None:
            url += "?"
            url += urllib.urlencode(self.params)
        return url

def turn_light_on():

    try:
        conn = httplib.HTTPConnection(url+':'+port)

        conn.request('GET','/?light='+name_parameter)

        r1 = conn.getresponse()
        print r1.status, r1.reason
        print r1.msg
        response_body =  r1.read()
        print  response_body
        return response_body

    except Exception as e:
        print e

def print_time():
    print "From print_time", time.time()


timer = InfiniteTimer(10, turn_light_on)

def start_pollingTimer():
    try:
        print "starting polling timer..."
        timer.start()
        print "polling timer started"
    except Exception as e:
        print e

def stop_polling_timer():
    print "stopping polling timer"
    timer.cancel()


def main(argv):
    # My code here
    try:

        start_pollingTimer()

        input = raw_input("Press any key to stop...")

        stop_polling_timer()



    except Exception as e:
        print e


if __name__ == "__main__":
    main(sys.argv)