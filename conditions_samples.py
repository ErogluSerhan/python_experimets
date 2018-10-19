
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# hocanın çözümü

users = {"Serhan":"Test123", "Deneme":123}

print "Enter username"
v_name = raw_input()
# v_name = raw_input("Enter username")

print "password"
v_pwd = raw_input()


print users.get(v_name)

if str(users.get(v_name)) == v_pwd:
    print "Welcome", v_name
else:
    print "Try Again"





# ***** BİZİM DENEMELER *****

# users = {1: {"name":"Serhan", "PWD":"Test123"},
# #          2: {"name":"Deneme", "PWD":123}
# #         }
# #
# # print "Enter username"
# # v_name = raw_input()
# # # v_name = raw_input("Enter username")
# #
# # print "password"
# # v_pwd = raw_input()
#
#
# #for loop range kullanarak
# # v_len=len(users)
# # for i in range(1,v_len+1):
# #     if v_name == users[i]["name"] and v_pwd == users[i]["PWD"]:
# #         print "login successful"
# #         break
# #     else:
# #         print "no"


#while ile geleneksel metot
# i=len(users)
# a=1
#
# while a <= i:
#     print a
#     if v_name == users[a]["name"] and v_pwd == users[a]["PWD"]:
#         print "login successful"
#         break
#     else:
#         print "no"
#     a += 1



