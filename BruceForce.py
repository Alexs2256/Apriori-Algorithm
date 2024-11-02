import math
import time

class BruteForce:
    def __init__(self, database):
        self.infrequent_item_Sets = {}
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
                self.num_of_transactions+=1

    def brute_force_method(self):
        def sort_set(set):
            list = []
            for val in set:
                list.append(val)
            for i in range(0, len(list) - 1):
                for j in range(i + 1, len(list)):
                    if list[i] > list[j]:
                        temp = list[i]
                        list[i] = list[j]
                        list[j] = temp
            return list
        good_sets = set()

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
            items = []
            for i in range(len(candidates) - 1):
                candidates[i] = candidates[i].split(',')  # change
                for j in range(len(candidates[i])):
                    items.append(candidates[i][j])
            for j in items:
                good_sets.add(j)
            return (good_sets)

        def get_support(candidate, data):
            sup = 0
            for i in range(len(data)):
                s = set()
                transaction = data[i]
                if isinstance(transaction, str):
                    transaction = transaction.split(',')  # Split transaction by commas
                for item in transaction:
                    s.add(item)
                if candidate.issubset(set(s)):
                    sup += 1
            return sup


        def generate_c2(good_sets):
            list = sort_set(good_sets)
            list_of_list = [list]
            set_size = 2
            while True:
                all_candidates = []
                for i in range(len(list)-1):
                    for j in range(i+1, len(list)):
                        if len(list_of_list) == 1:  # change
                            s1, s2 = string_to_set(list[i]), string_to_set(list[j])  # change
                        else:
                            s1, s2 = list[i], list[j]  # change
                        curr_set = s1.union(s2)  # change
                        if curr_set not in all_candidates and len(curr_set) == set_size:
                            all_candidates.append(curr_set)
                        else:
                            break
                list = sort_set(all_candidates)
                freq_count = 0
                for k in list:
                    if get_support(k, self.data1)/self.num_of_transactions >= self.min_support:
                        freq_count+=1
                if freq_count == 0: break
                list_of_list.append(list)
                set_size+=1
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
                    if get_support(curr_set[j], self.data1) == 0: continue
                    items = sort_set(candidates[i][j])
                    if get_support(curr_set[j], self.data1)/self.num_of_transactions >= self.min_support:
                        print("Rule", rule, "("+str(len(items)), "item set:"+")")
                    invalid1, invalid2 = True,True
                    for k in range(len(items)):
                        diff_of_items = set() # Gets individual target item
                        diff_of_items.add(items[k]) # "Adds target item to set"
                        items[k] = string_to_set(items[k]) #change
                        confidence = get_support(candidates[i][j], self.data1)/get_support(diff_of_items, self.data1)# Calculates confidence
                        if confidence >= self.min_confidence and get_support(curr_set[j], self.data1)/self.num_of_transactions >= self.min_support:
                            invalid1=False
                            print(str(diff_of_items) + " --> " + str(curr_set[j].difference(items[k])), "[" + str(round(get_support(curr_set[j], self.data1)/self.num_of_transactions*100, 1)) + "%" + ", " + str(round(confidence*100, 1)) + "%" + "]")
                        confidence = get_support(candidates[i][j], self.data1)/get_support(curr_set[j].difference(items[k]), self.data1)
                        if confidence >= self.min_confidence and get_support(curr_set[j], self.data1)/self.num_of_transactions >= float(self.min_support):
                            invalid2=False
                            print(str(curr_set[j].difference(items[k])) + " --> " + str(diff_of_items), "[" + str(round(get_support(curr_set[j], self.data1)/self.num_of_transactions*100, 1)) + "%" + ", " + str(round(confidence*100, 1)) + "%" + "]")
                        if len(items) == 2:
                            break
                    if get_support(curr_set[j], self.data1)/self.num_of_transactions >= self.min_support:
                        if invalid1==True and invalid2==True:
                            print("Invalid Rule")
                        print("-------------------------------")
                        rule+=1
        get_association_rules(generate_c2(good_sets))

databases = ["Amazon.txt","Kmart.txt","Shoprite.txt","Walmart.txt","Nike.txt"]
for database in databases:
    bruteforce = BruteForce(database)
    start_time = time.time()
    bruteforce.brute_force_method()
    end_time = time.time()

    execution_time = end_time - start_time
    print("")
    print(f"Brute Force Execution time: {execution_time:.6f} seconds")



