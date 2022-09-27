class process:
    def __init__(self):
        self.pid = 0
        self.arrival_time = 0
        self.burst_time = 0
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = 0
n = None
p = [process() for _ in range(100)]
average_turn_around_time = None
avg_waiting_time = None
avg_response_time = None
cpu_utilisation = None
total_turnaround_time = 0
total_waiting_time = 0
total_response_time = 0
total_idle_time = 0
throughput = None
burst_remaining = [0]*100
is_completed = [0]*100

print("Enter the number of processes: ",end=' ')
n=int(input())
for i in range(0, n):
    print("Enter arrival time of process ",i+1,' :',end=' ')
    p[i].arrival_time=int(input())
    print("Enter burst time of process ",i+1,' :',end=' ')
    p[i].burst_time=int(input())
    p[i].pid = i+1
    burst_remaining[i] = p[i].burst_time
current_time = 0
completed = 0
prev = 0

while completed != n:
    idx = -1
    mn = 10000000
    for i in range(0, n):
        if p[i].arrival_time <= current_time and is_completed[i] == 0:
            if burst_remaining[i] < mn:
                mn = burst_remaining[i]
                idx = i
            if burst_remaining[i] == mn:
                if p[i].arrival_time < p[idx].arrival_time:
                    mn = burst_remaining[i]
                    idx = i

    if idx != -1:
        if burst_remaining[idx] == p[idx].burst_time:
            p[idx].start_time = current_time
            total_idle_time += p[idx].start_time - prev
        burst_remaining[idx] -= 1
        current_time += 1
        prev = current_time

        if burst_remaining[idx] == 0:
            p[idx].completion_time = current_time
            p[idx].turnaround_time = p[idx].completion_time - p[idx].arrival_time
            p[idx].waiting_time = p[idx].turnaround_time - p[idx].burst_time
            p[idx].response_time = p[idx].start_time - p[idx].arrival_time
            total_turnaround_time += p[idx].turnaround_time
            total_waiting_time += p[idx].waiting_time
            total_response_time += p[idx].response_time

            is_completed[idx] = 1
            completed += 1
    else:
        current_time += 1

min_arrival_time = 999999
max_completion_time = -1
for i in range(0, n):
    min_arrival_time = min(min_arrival_time,p[i].arrival_time)
    max_completion_time = max(max_completion_time,p[i].completion_time)

average_turn_around_time = float(total_turnaround_time) / n
avg_waiting_time = float(total_waiting_time) / n
avg_response_time = float(total_response_time) / n
cpu_utilisation = ((max_completion_time - total_idle_time) / float(max_completion_time))*100
throughput = float(n) / (max_completion_time - min_arrival_time)

print("Precess ID\t","Arrival time\t","Burst time\t","Start Time\t","Completion Time\t","Turnaround Time\t","Waiting Time\t","Response Time\n")
for i in range(0, n):
    print(p[i].pid,"\t\t\t\t",p[i].arrival_time,"\t\t\t\t",p[i].burst_time,"\t\t\t\t",p[i].start_time,"\t\t\t\t",p[i].completion_time,"\t\t\t\t",
          p[i].turnaround_time,"\t\t\t\t",p[i].waiting_time,"\t\t\t\t",p[i].response_time,"\n")
print("Average Turnaround Time = ",average_turn_around_time,"\nAverage Waiting Time = ",avg_waiting_time,"\nAverage Response Time = ",avg_response_time,"\nCPU Utilization = ",cpu_utilisation,
                                    "\nThroughput = ",throughput," process/unit time",)
