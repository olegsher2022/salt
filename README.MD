

DOCKER RUN:
oleg@i5:~/workspace/docker$ docker run ubuntu_min
 * Serving Flask app 'server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 130-673-496


RUN TESTS:
oleg@i5:~/workspace/docker$ docker ps
CONTAINER ID   IMAGE        COMMAND                 CREATED         STATUS         PORTS                      NAMES
39878cc1d82c   ubuntu_min   "python3 ./server.py"   3 minutes ago   Up 3 minutes   127.0.0.1:5000->5000/tcp   tender_euclid
oleg@i5:~/workspace/docker$ 
oleg@i5:~/workspace/docker$ 
oleg@i5:~/workspace/docker$ docker exec -it 39878cc1d82c python3 -m pytest tests/test_server.py
=================================================================================== test session starts ===================================================================================
platform linux -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: /app, configfile: pytest.ini
collected 4 items                                                                                                                                                                         

tests/test_server.py::test_get_positive[0-sex-F] SKIPPED (unconditional skip)                                                                                                       [ 25%]
tests/test_server.py::test_get_positive[0-age-18] 
------------------------------------------------------------------------------------- live log setup --------------------------------------------------------------------------------------
2022-10-23 21:56:02 INFO ********* Test Setup *********
2022-10-23 21:56:02 INFO Server response code is 200
PASSED                                                                                                                                                                              [ 50%]
------------------------------------------------------------------------------------ live log teardown ------------------------------------------------------------------------------------
2022-10-23 21:56:02 INFO ********* Test Teardown *********

tests/test_server.py::test_get_positive[0-address-U] 
------------------------------------------------------------------------------------- live log setup --------------------------------------------------------------------------------------
2022-10-23 21:56:02 INFO ********* Test Setup *********
2022-10-23 21:56:02 INFO Server response code is 200
PASSED                                                                                                                                                                              [ 75%]
------------------------------------------------------------------------------------ live log teardown ------------------------------------------------------------------------------------
2022-10-23 21:56:02 INFO ********* Test Teardown *********

tests/test_server.py::test_get_positive[0-address-B] 
------------------------------------------------------------------------------------- live log setup --------------------------------------------------------------------------------------
2022-10-23 21:56:02 INFO ********* Test Setup *********
2022-10-23 21:56:02 INFO Server response code is 200
XFAIL                                                                                                                                                                               [100%]
------------------------------------------------------------------------------------ live log teardown ------------------------------------------------------------------------------------
2022-10-23 21:56:02 INFO ********* Test Teardown *********


========================================================================= 2 passed, 1 skipped, 1 xfailed in 0.07s =========================================================================
oleg@i5:~/workspace/docker$ 

ACCESS DOCKER:
oleg@i5:~/workspace/docker$ docker exec -it  4e2818b1d7cb /bin/bash
root@4e2818b1d7cb:/app# 


SERVER UP/DOWN
instead of shutdown / up server, iptables rule can be used like:
iptables -A INPUT -p tcp --destination-port 5000 -j DROP
docker should be started with:
docker run ubuntu_min --privileged
