# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 2 tip user
# 1: Admin/Superuser
#     Ticket durumunu değiştir
#     Ticket açma
#     Login/Logout
#
# 2: User
#     Ticket açma
#     Ticket cevap verme
#     Kayıt olma
#     Login/Logout
# program sonsuz döngüde olsun

users = {"admin": {"password": "1234", "type": "admin"}}
tickets = {1: {1: {"commmented by": "admin", "comment": " "}}}
session = False
ticket_number = 2

while True:
    if not session:
        choice = raw_input("Enter a process: [1: Login, 2: Registration] ")
        username = raw_input("Enter Username: ")
        password = raw_input("Enter Password: ")

        if choice == "1":
            if users.get(username).get("password") == password:
                session = True

        if choice == "2":
            if not users.get(username):
                users.update({username: {"password": password, "type": "user"}})
                session = True

    else:
        choice = raw_input("Enter a process: [1: Logout, 2: Create Ticket, 3:Comment Ticket]")

        if choice == "1":
            session = False

        if choice == "2":
            if users.get(username).get("type") == "admin":
                print "Admin can not create tickets"

            if users.get(username).get("type") == "user":
                print tickets
                ticket_number = ticket_number +1
                comment = raw_input("Enter Comment: ")
                tickets.update({ticket_number: {1: {"commmented by": "user", "comment": comment}}})
                print tickets

        if choice == "3":
            print tickets
            ticket_number = raw_input("Ticket Number to comment: ")
            comment = raw_input("Enter Comment: ")

            if users.get(username).get("type") == "admin":
                thread_no = len(tickets.get(ticket_number))
                thread_no = thread_no + 1
                tickets.update({ticket_number: {thread_no: {"commmented by": "admin", "comment": comment}}})
                print tickets

            if users.get(username).get("type") == "user":
                print tickets.get(ticket_number)
                thread_no = len(tickets.get(int(ticket_number)))
                thread_no = thread_no + 1
                tickets.update({ticket_number: {thread_no: {"commmented by": "user", "comment": comment}}})
                print tickets