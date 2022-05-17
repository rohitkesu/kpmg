
my_dict = {"a":{"b":{"c":"d"}}}

my_keys = ["a", "b", "c"]


for key in my_keys:
  if key in list(my_dict.keys()):
    print(key)    
  else:
    pass

  my_dict = my_dict.get(key)
  #print(my_dict)