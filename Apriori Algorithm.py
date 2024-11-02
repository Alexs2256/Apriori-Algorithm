import time
class AprioriAlgo:
    def __init__(self, database):
        self.infrequent_item_Sets = {}
        self.item_hash = {}
        self.support_values = {}
        self.min_support = 0
        self.min_confidence = 0
        while True:
            try:
                print("Please enter minimum support: ")
                self.min_support = float(input())
                print("Please enter minimum confidence: ")
                self.min_confidence = float(input())
                break
            except ValueError:
                print("Value must be a decimal (e.g. [.2 for 20%]")
        try:
            f = open(database, 'r')
            self.data1 = f.read().split('\n')
        except FileNotFoundError:
            print(f"Error: The file {database} was not found.")
            return  # Early exit if file not found
        self.num_of_transactions = 0
        for i in self.data1:
            if len(i) > 0:
                self.num_of_transactions += 1
    def apriori_algorithm(self):
        def sort_set(set):
            list = []
            for val in set:
                list.append(val)
            for i in range(0, len(list) - 1):
                s1 = set_to_string(list[i])
                for j in range(i + 1, len(list)):
                    s2 = set_to_string(list[j])
                    if s1[0] > s2[0]: #change
                        temp = list[i]
                        list[i] = list[j]
                        list[j] = temp
            return list

        def set_to_string(curr_set):
            s = ""
            for i in curr_set: s+=i
            return s

        def string_to_set(string_list):
            string_list = str(string_list)
            s = set()
            s.add(string_list)
            return s

        def generate_candidates(candidates):
            dict = {}
            good_sets = set()
            for i in range(len(candidates)):
                candidates[i] = candidates[i].split(',')
                for j in range(len(candidates[i])):
                    if candidates[i][j] != '':
                        if candidates[i][j] not in dict:
                            dict[candidates[i][j]] = 1
                        else:
                            dict[candidates[i][j]] +=1
            for key in dict:
                if dict[key]/self.num_of_transactions >= self.min_support:
                    good_sets.add(key)
                else:
                    bad_sets = set()
                    bad_sets.add(key)
                    self.infrequent_item_Sets[key] = get_hash(bad_sets)
            return(good_sets)

        def hash_items(items):
            hash = 1
            for transaction in items:
                transaction = transaction.split(',')
                for item in transaction:
                    if item != '' and item not in self.item_hash:
                        self.item_hash[item] = hash
                        hash+=1
        hash_items(self.data1)

        def get_support(candidate, data):
            # Check to see if the candidate's support value has already been calculated
            sorted_candidate = sort_set(candidate)
            key, i = 0, 0
            for items in sorted_candidate:
                i = len(items)
                key += self.item_hash[items]*(100**i)*(ord(items[0])+ord(items[len(items)-1])) # Prevent Collisions
            if key in self.support_values: return self.support_values[key]
            # [If it hasn't, calculate and store it]
            self.support_values[key] = 0.2
            sup = 0
            for i in range(len(data)):
                s = set()
                transaction = data[i]
                for item in transaction:
                    s.add(item)
                if candidate.issubset(set(s)):
                    sup+=1
            self.support_values[key] = sup
            return sup

        def get_hash(curr_set):
            hash = 0
            for item in curr_set:
                hash += self.item_hash[item]**2
            return hash

        def prune(curr_set):
            curr_set = list(curr_set)
            n = len(curr_set)
            subsets = []
            for i in range(2**n): # Loop through all 2^n possible subsets
                subset = set()
                for j in range(n):
                    if i & (1 << j):  # Check if the j-th bit is set
                        subset.add(curr_set[j])
                        if get_hash(subset) in self.infrequent_item_Sets:
                            return True
            return False

        def generate_c2(good_sets):
            list = sort_set(good_sets)
            list_of_list = [list]
            set_size = 2
            while True:
                all_candidates = []
                for i in range(len(list)-1):
                    for j in range(i+1, len(list)):
                        if len(list_of_list) == 1:
                            s1, s2 = string_to_set(list[i]), string_to_set(list[j])
                        else: s1, s2 = list[i], list[j]
                        curr_set = s1.union(s2)
                        if len(curr_set) > set_size: continue
                        if prune(curr_set):
                            self.infrequent_item_Sets[set_to_string(curr_set)] = get_hash(curr_set)
                            continue
                        if get_support(curr_set, self.data1)/ self.num_of_transactions >= self.min_support and curr_set not in all_candidates:
                            all_candidates.append(curr_set)
                        else:
                            self.infrequent_item_Sets[set_to_string(curr_set)] = get_hash(curr_set)
                list = sort_set(all_candidates)
                if len(list) >= 1:
                    list_of_list.append(list)
                else:
                    break
                set_size+=1
            print(list_of_list)
            return list_of_list

        all_candidates = generate_c2(generate_candidates(self.data1))


        def get_association_rules(candidates):
            rule = 1
            store_name = database.split('.')[0]
            print(" ")
            print("Database: " + store_name)
            print(" ")
            for i in range(1, len(candidates)):
                curr_set = candidates[i]

                for j in range(len(candidates[i])):
                    items = sort_set(candidates[i][j])
                    if get_support(curr_set[j], self.data1)/self.num_of_transactions >= self.min_support:
                        print("Rule", rule, "("+str(len(items)), "item set:"+")")
                    inval_set1, inval_set2 = True, True

                    for k in range(len(items)):
                        diff_of_items = set() # Gets individual target item
                        diff_of_items.add(items[k]) # "Adds target item to set"
                        items[k] = string_to_set(items[k]) #change
                        confidence = get_support(candidates[i][j], self.data1)/get_support(diff_of_items, self.data1)# Calculates confidence
                        if confidence >= self.min_confidence:
                            inval_set1=False
                            print(str(diff_of_items) + " --> " + str(curr_set[j].difference(items[k])), "[" + str(round(get_support(curr_set[j], self.data1)/self.num_of_transactions*100, 1)) + "%" + ", " + str(round(confidence*100, 1)) + "%" + "]")
                        confidence = get_support(candidates[i][j], self.data1)/get_support(curr_set[j].difference(items[k]), self.data1)
                        if confidence >= self.min_confidence:
                            inval_set2=False
                            print(str(curr_set[j].difference(items[k])) + " --> " + str(diff_of_items), "[" + str(round(get_support(curr_set[j], self.data1)/self.num_of_transactions*100, 1)) + "%" + ", " + str(round(confidence*100, 1)) + "%" + "]")
                        if len(items) == 2:
                            break
                    if inval_set1==True and inval_set2==True: print("Invalid Rule")
                    print("-------------------------------")
                    rule+=1
        get_association_rules(all_candidates)

databases = ["Amazon.txt","Kmart.txt","Shoprite.txt","Walmart.txt","Nike.txt"]
for database in databases:
    apriori = AprioriAlgo(database)
    start_time = time.time()
    apriori.apriori_algorithm()
    end_time = time.time()

    execution_time = end_time - start_time
    print("")
    print(f"Apriori Algorithm Execution time: {execution_time:.6f} seconds")



