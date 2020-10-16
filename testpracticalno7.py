class Hash:
    def _init_(self, keys, lrg, hrg):
        self.value = self.hashfunction(keys,lrg, hrg)

    def get_key_value(self):
        return self.value

    def hashfunction(self,keys,lrg, hrg):
        if lrg == 0 and hrg > 0:
            return keys%(hrg)

if __name__ == '__main__':
    list_of_keys = [23,43,1,87]
    list_of_list_index = [None,None,None,None]
    print("Before : " + str(list_of_list_index))
    for value in list_of_keys:
        list_index = Hash(value,0,len(list_of_keys)).get_key_value()
        if list_of_list_index[list_index]:
            print("Collission detected")
        else:
            list_of_list_index[list_index] = value

    print("After: " + str(list_of_list_index))
