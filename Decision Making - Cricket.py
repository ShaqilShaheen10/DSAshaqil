Decision Making - Cricket
Praveen is crazy about IPL. He was watching Mumbai Indians vs. Chennai Super Kings final match. Mumbai won the toss and elected to bat first. 
They finished batting with a score of X. Next, Chennai started to bat and scored Y runs in N number of balls. Now, Praveen wants to calculate the run rate
and check whether there is a probability for Chennai to win or not. Help him calculate the run rate and check the probability.

Input Format

Input consists of 4 integers. The first input corresponds to the total number of balls. The second input corresponds to the total number of runs.
The third input corresponds to the number of runs scored. The fourth input corresponds to the number of balls bowled.

Output Format
The first output corresponds to the total number of overs. The second output corresponds to the total number of overs finished. 
The third output corresponds to the current run rate. The fourth output corresponds to the total run rate. The fifth output corresponds to the eligibility. 
If eligible print "Eligible to Win" else print "Not Eligible to Win"

Sample Input 0
300
375
78
45
  
Sample Output 0
50
7.3
10.7
7.5
Eligible to Win
  
Sample Input 1
300
268
23
45
  
Sample Output 1
50
7.3
3.2
5.4
Not Eligible to Win

Python Code:

balls_total = int(input())
runs_total = int(input())
runs_scored = int(input())
balls_bowled = int(input())
overs_total = balls_total // 6
overs_finished = balls_bowled // 6 + (balls_bowled % 6) / 10
current_run_rate = runs_scored / overs_finished
total_run_rate = runs_total / overs_total
eligibility = "Eligible to Win" if current_run_rate >= total_run_rate else "Not Eligible to Win"
print(overs_total)
print("{:.1f}".format(overs_finished))
print("{:.1f}".format(current_run_rate))
print("{:.1f}".format(total_run_rate))
print(eligibility)
