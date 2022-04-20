class mydict:
    size = 16
    def __init__(self):
        # create a list of empty lists of size 16
        self.data = [[] for i in range(self.size)]

    def _find(self,key):
        # return list and list index for location in dictionary.  
        # This is an internal method used by other methods
        # to determine where item belongs.   
        # If item is not in dictionary, return (list, None)
        # where list is where item belongs
        """
        Args:
        self (class instance)
        key (string)

        Returns:
        tuple
        """
        find_hash =  hash(key) % len(self.data)             #defining the remain of hash value over data's length
        for key_letter in self.data[find_hash]:             #making a for loop
            if key_letter[0] == key:                        #if the for loop finds correct key
                return (self.data[find_hash], self.data[find_hash].index(key_letter))   #return the sublist and its index
        return (self.data[find_hash], None)         #otherwise, just return the sublist and None

    def __getitem__(self,key):
        # if item matching key is dictionary, 
        # return the value otherwise raise KeyError
        # must use _find
        """
        Args:
        self (class instacne)
        key (string)

        Returns:
        list
        """
        if self._find(key)[1] == None:                          #making a condition if the key is not in the data
            raise KeyError                                      #raising KeyError
        else:
            return self._find(key)[0][self._find(key)[1]][1]    #returning the key's value
    def __setitem__(self,key,value):
        # Set value of item with key, or insert item 
        # with key in dictionary
        # must use _find
        """
        Args:
        self (class instance)
        key (string)
        value (integer)

        Returns:
        
        """
        if self._find(key)[1] == None:                                  #checking if the item exists
            self.data[hash(key) % len(self.data)].append([key, value])  #if it does not exist, append the item
        else:
            self._find(key)[0][self._find(key)[1]][1] = value           #otherwise, updating the value
            


    def __contains__(self,key):
        # if item matching key is in dictionary, 
        # return True otherwise return False
        # must use _find
        """
        Args:
        self (class instace)
        key (string)

        Returns:
        Boolean
        """
        return self._find(key)[1] != None       #check if the key exists in the data as boolean
   
    def keys(self):
        # return a list of the keys in the dictionary
        """
        Args:
        self (class instace)

        Returns:
        list
        """
        key_list = []                               #making an empty list to append keys
        for sub_list in self.data:                  #making a for loop to get in each sub_list in data
            for key_value in sub_list:              #mkaing a for loop to check every item for each sub_list
                key_list.append(key_value[0])       #appending every keys
        return key_list                             #returning the appended list

    def values(self):
        # return a list of values in dictionary
        """
        Args:
        self (class instance)

        Returns:
        list
        """
        value_list = []                         #making an empty list to append values
        for sub_list in self.data:              #making a for loop to get in each sub_list in data
            for key_value in sub_list:          #mkaing a for loop to check every item for each sub_list
                value_list.append(key_value[1]) #appending every values
        return value_list                       #returning the appended list

    def items(self):
        # return a list of items [(key,value),...]
        """
        Args:
        self (class instance)

        Returns:
        list
        """
        item_list = []                                          #making an empty list to append values
        for sub_list in self.data:                              #making a for loop to get in each sub_list in data
            for key_value in sub_list:                          #making a for loop to check every item for each sub_list
                item_list.append((key_value[0], key_value[1]))  #forming a tuple of key and value and appending it to the empty list
        return item_list                                        #returning the appended list


    def pop(self,key):
        # remove item with key from dictionary and 
        # return corresponding value
        # raise KeyError if item doesn't exist
        # must use _find
        """
        Args:
        self (class instance)
        key (string)

        Returns:
        integer
        """
        if self._find(key)[1] == None:              #checking if the key exists in the data
            raise ValueError                        #if it doesn't raising ValueError
        else:
            [sublist, index] = self._find(key)      #accessing the format of self._find(key)'s returning result
            value = sublist[index][1]               #defining value
            sublist.remove(sublist[index])          #removing the item
            return value                            #returning the value

    def __delitem__(self,key):
        # remove item with key from dictionary
        # raise KeyError if item doesn't exist
        # returns None
        """
        Args:
        self (class instance)
        key (string)

        Returns:
        
        """
        if self._find(key)[1] == None:              #checking if the item exists in the data
            raise ValueError                        #if it doesn't, raising ValueError
        else:
            [sublist, index] = self._find(key)      #accesing the format of self._find(key)'s returning result
            sublist.remove(sublist[index])          #removing the items 

    def __len__(self):
        # return the number of elements in the dictionary
        """
        Args:
        self (class instance)

        Returns:
        integer
        """
        item_list = []                  #making an empty list to append all the items
        for sub_list in self.data:      #making a for loop to check every sub_list in data
            for item in sub_list:       #making a for loop to check every item in sub_lists
                item_list.append(item)  #appending every item
        return len(item_list)           #returning the number of items in the list

    def __str__(self):
        """
        Args:
        self (class instance)

        Returns:
        string
        """
        dict_str = "{ "                             #starting string
        item_list = self.items()                    #defining every item by using self.items()
        for i in range(len(item_list)):             #making a for loop to check every item by using index
            (key,value) = item_list[i]              #accesing the format of the item_list
            dict_str += f"{key} : {value}, "        #adding keys and values following the format by using f string
        dict_str = dict_str[0:len(dict_str)-2]      #earasing the last space and comma
        dict_str += " }"                            #closing string
        return dict_str                             #returning completed string representing the dictionary

if __name__ == "__main__":
    d = mydict()
    d[1] = 33
    print(d[1])
    try:
        print(d[2])
    except KeyError:
        print("2 is not a valid key")
    d['a'] = 33
    d['b'] = 44
    print(d.keys())
    print(d.values())
    print(d.items())
    print(f'length {len(d)}')
    print(d)
    print('a' in d)
    print('xx' in d)
    print(d.pop('a'))
    print('a' in d)
    print(d['b'])
    del d['b']
    try:
        print(d['b'])
    except KeyError:
        print('b is not in d')
    
    e1 = None
    try:
        d2 = {}
        d2[['a']] = 33
    except Exception as e:
        e1 = e
    
    e2 = None
    try:
        d[['a']] = 33
    except Exception as e:
        e2 = e
        print(type(e).__name__,e)

    assert type(e1) is type(e2) and e1.args == e2.args