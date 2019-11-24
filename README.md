# Ansible Collection Demo

## Calc Server

Calc server is ADDITION ONLY calculator that is controlled by using REST-like API.

### Calc "10 + 20"

    $ curl http://localhost:8080/?value=10
    10 = 10

    $ curl http://localhost:8080/?value=20
    10 + 20 = 30

### Show current result

    $ curl http://localhost:8080/
    10 + 20 = 30

### Clear result

    $ curl http://localhost:8080/?command=clear
    0

## Run demo

### (1) Install Ansible Collection sample

See https://github.com/m-takahashi-if/ansible-collection-sample .

### (2) Get demo

    $ git clone https://github.com/m-takahashi-if/ansible-collection-demo.git

### (3) Run Calc Server

    $ cd ansible-collection-demo
    $ python3 calc-server.py

### (4) Run playbooks

Run module demo as below.

    $ ansible-playbook -i hosts.yml module-example-playbook.yml

To see the result, open web brower with http://localhost:8080/ .

Run role demo as below.

    $ ansible-playbook -i hosts.yml role-example-playbook.yml

To see the result, open web brower with http://localhost:8080/ .
