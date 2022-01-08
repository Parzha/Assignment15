
string_sem = input("Please enter array of your choice-> ")
list_sem = string_sem.split()

len_sem = len(list_sem)
sem_detector = False
for i in range(len_sem):

     if list_sem[i] ==  list_sem[len_sem - 1]:
         sem_detector = True
     else :
         sem_detector = False
         break
     len_sem -= 1


if sem_detector == False:
    print("this array is not  symmetrical")
else:
    print("this array is symmetrical")