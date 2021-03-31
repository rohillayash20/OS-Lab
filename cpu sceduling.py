#!/usr/bin/env python
# coding: utf-8

# ### FCFS

# In[12]:


def FCFS(process,n,bt):
    waitingtime=[]
    turnaround_time=[]
    for i in range(n): 
        if i==0:
            waitingtime.append(0)
        else:
            x=bt[i-1]+ waitingtime[i-1]
            waitingtime.append(x)
    #print(waitingtime)
    for i in range(n):
        if i==0:
            turnaround_time.append(bt[i])
        else:
            y=bt[i]+waitingtime[i]
            
            turnaround_time.append(y)
        
    #print(turnaaround_time)
    
    # Below code is simply for making a table
    
    totaltime_waiting=0
    total_turnaround=0
    print( "Processes Burst time " + " Waiting time " + " Turn around time")
    for i in range(n):
        totaltime_waiting=totaltime_waiting + waitingtime[i]
        total_turnaround=total_turnaround+turnaround_time[i]
        
        print(" " + str(i+1) + "\t\t\t"+str(bt[i])+"\t\t\t"+ str(waitingtime[i])+"\t\t\t"+ str(turnaround_time[i]))
    Average_waiting_time=(totaltime_waiting)/n
    Average_turnaround_time=(total_turnaround)/n

    print("Avg waiting time=",Average_waiting_time)
    print("Avg turnaround time=",Average_turnaround_time)


# In[13]:


process = [1 , 2 , 3 , 4]
bt = [4 , 2 , 1 , 7]
FCFS(process,4,bt)


# ### SJF

# In[16]:


def SJF(process,l,bt):
    
    
    for i in range(l):
        for j in range(i,l):
            if bt[i]>bt[j]:
                temp=bt[i]
                bt[i]=bt[j]
                bt[j]=temp
                temp=process[i]
                process[i]=process[j]
                process[j]=temp
    
    waitingtime=[]
    turnaaround_time=[]
    for i in range(l): 
        if i==0:
            waitingtime.append(0)
        else:
            x=bt[i-1]+ waitingtime[i-1]
            waitingtime.append(x)
    #print(waitingtime)
    for i in range(l):
        if i==0:
            turnaaround_time.append(bt[i])
        else:
            y=bt[i]+waitingtime[i]
            turnaaround_time.append(y)
    #print(turnaaround_time)
    
    # Below code is simply for making table
    
    totaltime_waiting=0
    total_turnaround=0
    print( "Processes Burst time " + " Waiting time " + " Turn around time")
    for i in range(l):
        totaltime_waiting=totaltime_waiting + waitingtime[i]
        total_turnaround=total_turnaround+turnaaround_time[i]
        
        print(" " + str(process[i]) + "\t\t\t"+str(bt[i])+"\t\t\t"+ str(waitingtime[i])+"\t\t\t"+ str(turnaaround_time[i]))
    Average_waiting_time=(totaltime_waiting)/l
    Average_turnaround_time=(total_turnaround)/l

    print("Avg waiting time=",Average_waiting_time)
    print("Avg turnaround time=",Average_turnaround_time) 


# In[17]:


process = [1 , 2 , 3 , 4]
bt = [4 , 2 , 1 , 7]
SJF(process,4,bt)


# ### Priority

# In[21]:



def Priority(p,l,bt,priority):
    for i in range(l):
        for j in range(i,l):
            if priority[i]>priority[j]:
                temp=priority[i]
                priority[i]=priority[j]
                priority[j]=temp
                y=p[i]
                p[i]=p[j]
                p[j]=y
                z=bt[i]
                bt[i]=bt[j]
                bt[j]=z
    waitingtime=[]
    turnaaround_time=[]
    for i in range(l): 
        if i==0:
            waitingtime.append(0)
        else:
            x=bt[i-1]+ waitingtime[i-1]
            waitingtime.append(x)
    #print(waitingtime)
    for i in range(l):
        if i==0:
            turnaaround_time.append(bt[i])
        else:
            y=bt[i]+waitingtime[i]
            turnaaround_time.append(y)
    #print(turnaaround_time)
    
    # Below code is for printing table
    
    totaltime_waiting=0
    total_turnaround=0
    print( "Processes Burst time " + " Waiting time " + " Turn around time")
    for i in range(l):
        
        
        print(" " + str(p[i]) + "\t\t\t"+str(bt[i])+"\t\t\t"+ str(waitingtime[i])+"\t\t\t"+ str(turnaaround_time[i]))
    Average_waiting_time=(totaltime_waiting)/l
    Average_turnaround_time=(total_turnaround)/l

    print("Avg waiting time=",Average_waiting_time)
    print("Avg turnaround time=",Average_turnaround_time)


# In[22]:


process = [1 , 2 , 3 , 4]
bt = [4 , 2 , 1 , 7]
priority = [2 , 1 , 3 , 4]
Priority(process,4,bt , priority)


# ### Round Robin

# In[23]:


def Round_robin(processes, n, bt, quantum):  
    wt = [0] * n 
    tat = [0] * n  
    rem_bt = [0] * n 
  
    for i in range(n):  
        rem_bt[i] = bt[i] 
    t = 0 
    while(1): 
        done = True
        for i in range(n): 
            if (rem_bt[i] > 0) : 
                done = False 
                if (rem_bt[i] > quantum) : 
                    t += quantum  
                    rem_bt[i] -= quantum                       
                else:
                    t = t + rem_bt[i]  
                    wt[i] = t - bt[i]                          
                    rem_bt[i] = 0
        #print(done)
        if (done == True):# checkif every thing is done 
            break
    #turn arount time 
    for i in range(n): 
        tat[i] = bt[i] + wt[i]
    print("Processes    Burst Time     Waiting",  
                     "Time    Turn-Around Time") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", process[i], "\t\t", bt[i],  
              "\t\t\t\t", wt[i], "\t\t\t\t", tat[i]) 
  
    print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
    print("Average turn around time = %.5f "% (total_tat / n))  
      


# In[25]:


processes = [1 , 2 , 3 , 4]
bt = [4 , 2 , 1 , 7]
Round_robin(processes,4,bt , 2)


# In[ ]:




