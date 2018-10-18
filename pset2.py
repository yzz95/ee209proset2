import numpy as np
L = 6
W = 6
H = 12 
# 12 heading
h = [0,1,2,3,4,5,6,7,8,9,10,11]
# action = rotation (left, right) firts with Pe + move (foward,backward)
# or only move  1-2Pe not rotate
# or stay still 
#      11,0,1
#8,9,10      2,3,4
#       5,6,7
# turn left h+1 right h-1 mod%12
S = np.zeros([L,W,H])
s = [0,0,0]
s_ = [0,0,0]
R = np.zeros([L,W,H])
A = ['UL','UR','US','DL','DR','DS','LL','LR','LS','RL','RR','RS','stay']
P = np.zeros([L,W])
def calculate psa(s,s_,Pe,a):
	if : s[0] = 
		pass
	if :
		pass
def reward (s,S):
	for i in range(L):
		for j in range(W):
			if i == 0 || i == L-1 :
				S[i][j] = -100
			if j == 0 || j == W-1 :
				S[i][j] = -100




if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)







