#  TASK 1:
#  to_dict(list)
#  ['a', 'b', 1, 2]  =>  {'a':'a', 'b':'b', 1:1, 2:2]

def to_dict(l):
    pass

#  TASK 2:
#  biggest_dict(**kwargs)
#  my_dict += **kwargs

my_dict = {"first": 'blyat'}
def biggest_dict(**kwargs):
    pass

#  TASK 3:
#  count_it(list) => {int: count}
#  [1, 3,3, 4,4,4, 5,5, 7,7,7,7] => {1:1, 3:2, 4:3, 5:2, 7:4}
def count_it(l):
    pass

#  TASK 4:
#  max_dct(dict1, dict2): {'a': 5, 'b': 6} {'a':7, 'b':5, 'c':2} => max ({'a':7, 'b':6, 'c':2})
#  sum_dct(dict1, dict2): {'a': 5, 'b': 6} {'a':7, 'b':5, 'c':2} => sum ({'a':12, 'b':11, 'c':2})

def max_dct(dict1, dict2):
    pass


def sum_dct(dict1, dict2):
    pass






#  _______________________________________________TESTING:
tasks = 0.0
_ = to_dict(['p1', 'p2', True, False, 5, 15, 25])
if _ != {'p1':'p1', 'p2':'p2', True:True, False:False, 5:5, 15:15, 25:25}:
    print("First task incomplete")
else:
    tasks += 1.0
biggest_dict(second='ebal', third='govno')
biggest_dict(fourth='v rotan')
if my_dict != {'first': 'blyat', 'second': 'ebal', 'third': 'govno', 'fourth': 'v rotan'}:
    print("Second task incomplete")
else:
    tasks += 1.0
_ = count_it([12,0,1,6,4,2,7,2,0,5,13,14,15,13,8,6,14,13,15,11,0,14,2,15,2,0,15,8,11,6,1,6,4,11,8,13,5,1,4,10,13,3,6,13,13])
if _ != {12: 1, 0: 4, 1: 3, 6: 5, 4: 3, 2: 4, 7: 1, 5: 2, 13: 7, 14: 3, 15: 4, 8: 3, 11: 3, 10: 1, 3: 1}:
    print("Third task incomplete")
else:
    tasks += 1.0
_ = max_dct({'Kate': 15, 'Vasya': 25, 'Vova': 4}, {'Kate': 25, 'Vasya': 15, 'Volodya': 4})
if _ != {'Kate': 25, 'Vasya': 25, 'Vova': 4, 'Volodya': 4}:
    print("Fourth task max func incomplete")
else:
    tasks += 0.5
_ = sum_dct({'Kate': 15, 'Vasya': 25, 'Vova': 4}, {'Kate': 25, 'Vasya': 15, 'Volodya': 4})
if _ != {'Kate': 40, 'Vasya': 40, 'Vova': 4, 'Volodya': 4}:
    print("Fourth task sum func incomplete")
else:
    tasks += 0.5


print(f"Tasks completed: {tasks}/4.0")
if tasks == 4.0:
    print("Great, now choose: anal fisting or cum on your face!!")
