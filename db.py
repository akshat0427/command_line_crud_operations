from datetime import datetime

import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['test']

data = mydb['crud']



class interface:
    def __init__(self) :
        
        self.task = str
        self.Time = str
        self.done_or_not = bool
        
    
        
    def add_task(self, t):
        
        self.task = t
        self.Time = datetime.now().strftime("%I:%M:%S %p")
        self.done_or_not = False
        
        data.insert_one({"count":data.count_documents({})+1,"task":self.task,"time":self.Time, "is_completed":self.done_or_not})
        
        
        
        
    def remove_task(self, i):  # i would be the index
          # Replace with the ObjectID of the document to delete
        result = data.delete_one({'count': i})
        
        
        if result.deleted_count == 1:
            pass
        else:
            print("error came")
    
    def view(self):
        
        
        for i in data.find():
            print(i['count'],"\t", i['task'], "  time added-", i['time'], "  is completed", i['is_completed'])
            
    def update(self,c:int, new_task:str, completed_or_not:bool):
        
        myquery = { "count": c }
        newvalues = { "$set": { "task": new_task, "is_completed":completed_or_not } }

        data.update_one(myquery, newvalues)
        print("done")


d = interface()

C = 0

while True:
    C+=1
    
    if C>1:
        pass
        
    else:
        print("to do list- \n 1.add task \n 2.view task \n 3.delete task \n 4.update task  \n press q to quit ")
    
    
    
    k = str(input("--  "))
    
    
    
    if k == "q":        
        break
    
    if k == "1":
        i2 = input("your task here---   ")
        d.add_task(i2)
        
        # print("\n to do list- \n 1.add task \n 2.view task \n 3.delete a task \n 4. press q to quit ")
    if k == "2":
        print()
        
        d.view()
        print("\n")
        # print("\n to do list- \n 1.add task \n 2.view task \n 3.delete a task \n 4. press q to quit ")
        
    if k == "3":
        d.view()
        print("\n")
        i3 = int(input("which task to remove-  "))
        d.remove_task(i3)
        d.view()
        
    if k == "4":
        d.view()
        
        b = bool
        
        v = input("which task to update--  ")
        tsk = input("task -  ")
        completed = int(input("done or not - 0 or 1 "))
        if completed == 1:
            b = True
        if completed == 0:
            b = False
            
        d.update(int(v), tsk, b)
        
        
        
        
        