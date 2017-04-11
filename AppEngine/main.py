from flask import Flask, render_template, request

from google.appengine.api import memcache
from google.appengine.api import users

app = Flask(__name__)
app.config['DEBUG'] = True

primeNums = []

@app.route('/')
def isprime():

    user = users.get_current_user()
    
    if user:
        logouturl = users.create_logout_url('/')
        nickname = user.nickname()
        n = 7
        '''check if integer n is a prime'''
        # make sure n is a positive integer
        n = abs(int(n))
    
    # 0 and 1 are not primes
        if n < 2:
            #return False
            pass
    
        # 2 is the only even prime number
        if n == 2: 
            #return True
            pass   
    
        # all other even numbers are not primes
        if not n & 1: 
            #return False
            pass
        
        # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                #return False
                pass
        #return True
        numbers = n
        memcache.add('numbers', '')
        number = 2
        if request.method == 'GET' and 'number_numbers' in request.args:
               number = request.args['number_numbers']
               number = memcache.get('numbers').split('/')
               if number in numbers:
                            memcache.incr(number)
               else:
                                   memcache.set('numbers', memcache.get('names') + '/' + number)
                                   memcache.set(number, 1)
                                   numbers = memcache.get('names').split('/')
                                   global primeNums
                                   for n in numbers:
                                          primeNums.append( (n, memcache.get(n) ) )
        return render_template('index.html', primeNums = primeNums, number = number, logouturl = logouturl, nickname = nickname)                                
    else:
      login_url = users.create_login_url('/')
      return 'Sorry, you are not logged in. <a href="%s">login</a>' % login_url, 200  
      
                           
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
