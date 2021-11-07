 
# TODO
# use sets instead of lists

# class for requirements
class requirement:
    
    def __init__(self, id):
        self.id = id
        self.tests = set()
        self.inputs = set()

    def print(self):
        print("ID:", self.id, " Inputs: ", self.inputs, " Tests: ", self.tests)


class requirement_group:

    def __init__(self):
        self.reqs = set()
        self.tests = set()
        self.inputs = set()   

    def print(self):
        print("Requirements: ", self.reqs, " Inputs: ", self.inputs, " Tests: ", self.tests)

class testcase:
    
    def __init__(self, id):
        self.id = id
        self.reqs = set()

    def print(self):
        print("ID:", self.id, " Requirements: ", self.reqs)


def read_requirements_from_csv(filename):
    sep=';'
    input_id_col = 0
    test_id_col = 2
    req_id_col = 1
    
    
    req_list = []
    
    with open(filename) as myfile:
        # drop first line
        myfile.readline()
        
        for line in myfile:
            segments = line.split(sep)
            id = int(segments[req_id_col])
            req = requirement(id)

            # create list of inputs
            req.inputs = set(map(int, segments[input_id_col].split(',')))
            # create list of tests
            req.tests = set(map(int, segments[test_id_col].split(',')))
            
            req_list.append(req)
    
    return req_list


def read_testcases_from_csv(filename):
    sep=';'
    test_id_col = 0
    req_id_col = 1
    
    
    test_list = []
    
    with open(filename) as myfile:
        # drop first line
        myfile.readline()
        
        for line in myfile:
            segments = line.split(sep)
            id = int(segments[test_id_col])
            test = testcase(id)

            # create list of requirements
            test.reqs = set(map(int, segments[req_id_col].split(',')))
            
            test_list.append(test)
    
    return test_list



req_list = read_requirements_from_csv('requirements.csv')
# TODO 
# add check that all req ids are unique and each req has at least one test

# convert requirement list to dict
req_dict = {req.id: req for req in req_list}
print("\nRequirements: ")
for req in req_dict:
    req_dict[req].print()



test_list = read_testcases_from_csv('tests.csv')

# convert test list to dict
test_dict = {test.id: test for test in test_list}
print("\nTests: ")
for test in test_dict:
    test_dict[test].print()



req_ids_unprocessed = set(req_dict.keys())
print("\nUnprocessed Requirement IDs:")
print(req_ids_unprocessed)

req_groups = []
# create groups of requirements
for id in req_dict.keys():
    # check if the req belongs to a new group
    if id in req_ids_unprocessed:
        
        req_grp = requirement_group()         
        req_grp.tests = req_dict[id].tests
        req_grp.inputs = req_dict[id].inputs
        
        req_list = [id]
        i = 0
        req_ids_unprocessed.remove(id)
        
        while i < len(req_list):
            for test in req_dict[req_list[i]].tests:
                req_grp.tests.add(test)
                for req_id in test_dict[test].reqs:
                    if req_id in req_ids_unprocessed:
                        req_ids_unprocessed.remove(req_id)
                        req_list.append(req_id)
                        req_grp.inputs = req_grp.inputs | req_dict[req_id].inputs
                        
            i += 1
        
        req_grp.reqs = set(req_list)        
        req_groups.append(req_grp)



print("\n\n")
for req_grp in req_groups:
    req_grp.print()
    
print("\nUnprocessed Requirement IDs:")
print(req_ids_unprocessed)   
    