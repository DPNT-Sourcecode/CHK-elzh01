
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name) -> str:
        if isinstance(friend_name, str) or type(friend_name).__str__ is not object.__str__:
            return "Hello, {}!".format(friend_name)
        raise TypeError("The friend_name must be a str or explicitly implement __str__")
