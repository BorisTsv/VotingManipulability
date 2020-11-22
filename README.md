# VotingManipulability

We explain the code used for carrying out the algorithm for finding the share of manipulable outcomes in the case of the Borda rule with m=4 alternatives.  With a few modifications to the code provided,  one can  perform analogous computations for scoring voting rules with different weights. 

Step 1. Create the array of possible preferences with the alternatives corresponding to numbers 0 to 3 arranged in increasing order. This array has 24 elements. Each element of the preferences' array is an array of its own with 4 elements (see lines 14-25 in the code). 

preferences[0]={[0],[1],[2],[3]},
	
preferences[1]={[0],[1],[3],[2]},
	
...
	
preferences[23]={[3],[2],[1],[0]}.
	
After this the point distribution array is created, i.e., the element (i,j) (here 0=< i =< 23 and  0=< j =< 3) is the number of points alternative j gets from preference i (lines 27-37).
	
Step 2. Now we are in position to store the inequalities responsible for the initial arrangement of alternatives. As usual we assume that this arrangement is (0,1,2,3) and we obtain the 3 PI inequalities responsible for this  (lines 3-8 and 38-41).
	
Step 3. Next generate a sample of n  (`trials' in the code) random points in the simplex. For this choose 24 random numbers on the closed interval [0;1], arrange them in a nondecreasing order and take the subsequent differences. The points created in this way have a uniform distribution in  the simplex.  The corresponding lines of the code are 43-54.
  
Step 4. The coalition arrays are established. These are 3 arrays of 24 elements, each element equal to 1 or 0, depending on whether preference i 
belongs to the coalition or not (lines 55-66).
	
Step 5. The difference arrays (see last paragraph of Section 2 for the definition) are generated (lines 67-105). 
	
Step 6. The remaining part of the code stores the inequalities responsible for the profile being manipulable by each of the coalitions separately (recall that  inequalities are  written in terms of the elements of difference arrays established in the previous step, see Section 3 in https://arxiv.org/pdf/1911.09173.pdf) and then checks  all sample points to determine how many of them satisfy the initial arrangement conditions and are manipulable by at least one coalition.
  
  
