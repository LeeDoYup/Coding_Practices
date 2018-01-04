from data_structure import print_all_friends, print_all_friends_and_closeness

name_list = ['Summer' , 'John', 'Justin', 'Mike', 'May', 'Kim', 'Tom', 'Jerry']
fr_info = {'Summer': [name_list[1],name_list[2],name_list[3]], 'John':[name_list[0],name_list[3]], 'Justin':[name_list[1],name_list[0],name_list[3],name_list[4]], 'Mike':[name_list[0],name_list[2]], 'May':[name_list[2],name_list[5]], 'Kim':[name_list[4]], 'Tom':[name_list[-1]], 'Jerry':[name_list[-2]]}

print "print all connected friends of Summer"
print_all_friends(fr_info, 'Summer')
#Summer, John, Justin, Mike, May, Kim

print "print all connected friends and closeness of Summer"
print_all_friends_and_closeness(fr_info, 'Summer')