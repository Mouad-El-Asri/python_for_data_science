from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "Morocco!")
ft_set = {"Hello", "Benguerir!"}
ft_dict = {"Hello" : "1337Benguerir!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
