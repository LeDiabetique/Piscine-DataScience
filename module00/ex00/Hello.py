def main():

	ft_list = ["Hello", "tata!"]
	ft_tuple = ("Hello", "toto!")
	ft_set = {"Hello", "tutu!"}
	ft_dict = {"Hello": "titi!"}

	ft_list[1] = "World!" # list is mutable
	ft_tuple = ("Hello", "France!") # tuple is immutable
	ft_set.remove("tutu!") # set is mutable and unique
	ft_set.add("Nice!")
	ft_dict["Hello"] = "42Nice!" # dict is mutable and accessed by a key

	print(ft_list)
	print(ft_tuple)
	print(ft_set)
	print(ft_dict)

if __name__ == "__main__":
	main()