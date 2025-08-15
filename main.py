
todo=[]
markAsDone=[]

ch=1
exit=False

print("1.Add\n2.Mark as Done with index\n3.Display\n4.Exit\n")
while not exit :
    ch=int(input('enter your choice:'))

    match ch:
        case 1: 
            task=input("enter a task:")
            todo.append(task)
        case 2:
            index=int(input("enter the index of the task to mark as done:"))
            r=index-1
            if 0<r<=len(todo):
                markAsDone.append(todo[r])
                todo.pop(r)   
        case 3:
            n1=len(todo)
            
            print("To-DO---->")
            for i in range(n1):
                print(todo[i])
            print("Mark As Done---->")    
            n2=len(markAsDone)
            for i in range(n2):
                print(markAsDone[i])
        case 4:
            exit=True
            print('Exiting')          
        case _:
            print("Invalid choice")    

##https://youtu.be/EgpLj86ZHFQ?si=-9QnpkN9vtmAM-AN
##pytest learn