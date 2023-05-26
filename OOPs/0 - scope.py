"""
Here we mention scopes of variables (not fn) inside a nested fucntion or functions,
namely Local, Global Scope.                                     # nonlocal # global
"""

test = 'global'                  # test global to both main as well as its sub fn's  
def check_scope():
    
    test = 'default'             # test global to sub fn's (local to main fn)

    def local_scope():
        test = 'local test'
    
    def non_local_scope():
        nonlocal test            # when test is assigned as nonlocal, it affects the 'test' with value 'default' | here this test act as global to these sub fn's 
        test = 'non local test'

    def global_scope():
        global test              # when test is assigned as global, it affects the 'test' with value 'global' | here this test act as global to main fn itself (so global to sub fn's too)
        test = 'global test'


    local_scope()
    print('Test value after calling local_scope: ',test)      # all this print inside this fn will access 'test' that is global to them i.e local to main fn. 
                                                              # to access main global 'test' i.e o/s main fn, we need to print test o/s the fn.
    non_local_scope()
    print('Test value after calling non_local_scope: ',test)

    global_scope()
    print('Test value after calling global_scope: ',test)

check_scope()
print('Test value after main: ',test)                         # accessing main global 'test'


# Explanation    
# nonlocal - consider 'test' that is global to sub functions only, i.e. local to main function
# global - consider 'test' that is global to main function as well as its sub functions too 

"""
1) When local_scope is called the test value is shown as - 'default', becoz the test inside the local_scope is local scope it can't be accessed
   outside it. We can get its actual value if we print it inside that fn. Here we print test outside the fn, so we get value for test as default
   as it take the test value that is global or outside. # default

2) When non_local_scope is called the test value is shown as - 'non local test', rather than value get before coz, here we define test as nonlocal
   so that test inside this fn is no mora a local variable that cannot be accessed outside of it. Now its non-local as name says so that it can be
   accessed outside so that the test value is # non local test

3) When global_scope is called the test value is shown as - 'non local test', becoz after calling non_local() the test value is updated as 'non local test'
   as we saw in above ex. Even though here we access the test that is global to all fn's by setting this global keyword, we dont get 'global_test as
   o/p coz, to access the value in global 'test' i.e (test global to all fn) we have to print 'test' outside the function. Here we are printing 'test' 
   inside the fn. so that it will access the test with 'default' value i.e 'test global to sub fn's' not the global 'test'.

4) Here we are printing 'test' outside the fn so that we got access to main global 'test' and thus we got value in it # global test

 """