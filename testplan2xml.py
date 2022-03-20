import xlsxwriter

class TSession:
    def __init__(self, id, objective):
        self.id = id
        self.objective = objective


class TObjective:
    def __init__(self, id, plan):
        self.id = id
        self.plan = plan
        self.sessions = []
 
        
class TPlan:
    def __init__(self, id):
       self.id = id
       self.objectives = []


def get_objective_ids(t_id):
    return [t_id+1, t_id+2]
        
def get_session_ids(o_id):
    return [o_id+11, o_id+12, o_id+13, o_id+14]


# collect data
t_ids = [100, 200] 
testplans = []
testobjectives = []
testsessions = []

for t_id in t_ids:
    t = TPlan(t_id)
    o_ids = get_objective_ids(t_id)
    for o_id in o_ids:
        o = TObjective(o_id, t)
        s_ids = get_session_ids(o_id)
        for s_id in s_ids:
            s = TSession(s_id, o)
            o.sessions.append(s)
            testsessions.append(s)
        t.objectives.append(o)
        testobjectives.append(o)
    testplans.append(t)




# debug output
for t in testplans:    
    print(t.id)
    for o in t.objectives:
        print(" " + str(o.id))
        for s in o.sessions:
            print("  " + str(s.id))
        

# create output structure



# write output
workbook = xlsxwriter.Workbook('Testplan.xlsx')

format_plan = workbook.add_format()
format_plan.set_bg_color('#0000FF')
format_objective = workbook.add_format()
format_objective.set_bg_color('#4040FF')
format_session = workbook.add_format()
format_session.set_bg_color('#9090FF')

worksheet = workbook.add_worksheet()

worksheet.write(0, 0, "ID")
worksheet.write(0, 1, "Category")
worksheet.write(0, 2, "Summary")
row = 1
for t in testplans:    
    worksheet.write(row, 0, t.id, format_plan)
    worksheet.write(row, 1, "Test Plan", format_plan)
    worksheet.set_row(row, None, None, {'level': 1})
    row += 1
    for o in t.objectives:
        worksheet.write(row, 0, o.id, format_objective)
        worksheet.write(row, 1, "Test Objective", format_objective)
        worksheet.set_row(row, None, None, {'level': 2})
        row += 1
        for s in o.sessions:
            worksheet.write(row, 0, s.id, format_session)
            worksheet.write(row, 1, "Test Session", format_session)
            worksheet.set_row(row, None, None, {'level': 3})
            row += 1



workbook.close()

