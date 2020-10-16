class Hash:
    def __init__(self, keys, lrg, hrg):
        self.value = self.hashfunction(keys,lrg, hrg)

    def get_key_value(self):
        return self.value

    def hashfunction(self,keys,lrg, hrg):
        if lrg == 0 and hrg > 0:
            return keys%(hrg)

if __name__ == '__main__':
    linear_probing = True
    list_of_keys = [12,56,78,89]
    list_of_list_index = [None,None,None,None]
    print("Before : " + str(list_of_list_index))
    for value in list_of_keys:
        #print(Hash(value,0,len(list_of_keys)).get_key_value())
        list_index = Hash(value,0,len(list_of_keys)).get_key_value()
        print("hash value for " + str(value) + " is :" + str(list_index))
        if list_of_list_index[list_index]:
            print("Collission detected for " + str(value))
            if linear_probing:
                old_list_index = list_index
                if list_index == len(list_of_list_index)-1:
                    list_index = 0
                else:
                    list_index += 1
                list_full = False
                while list_of_list_index[list_index]:
                    if list_index == old_list_index:
                        list_full = True
                        break
                    if list_index+1 == len(list_of_list_index):
                        list_index = 0
                    else:
                        list_index += 1
                if list_full:
                    print("List was full . Could not save")
                else:
                    list_of_list_index[list_index] = value









        else:
            list_of_list_index[list_index] = value

    print("After: " + str(list_of_list_index))
