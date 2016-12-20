import re;
import argparse;
import sys;


# make parser
parser = argparse.ArgumentParser(description='Parse regular expression input, check input and output file and give grade');
parser.add_argument('-l','--learner',help='learner input file contains regex');
parser.add_argument('-t','--test',help='test file contains line text for testing');
parser.add_argument('-s','--solution',help='solution file to check the output');


#parse argument
args = parser.parse_args(sys.argv[1:]);
#make array from argument
argobj = vars(args);

print(argobj); 

#open learner file
lfile = open(argobj['learner'],'r');
#read regex line (first line only)
regex = lfile.readline().rstrip();
lfile.close();

#open testCases file
testArr = [];
with open(argobj['test'],'r') as tfile:
#readlines
	testArr = [line.rstrip() for line in tfile];
	#testArr.append(readData);

#open solution array
solutionArr = [];
with open(argobj['solution'],'r') as sfile:
	solutionArr = [line.rstrip() for line in sfile];
	#solutionArr.append(readData);

print(regex);

#execute regular expression from test array using learner file and match it with solutionArr
i = 0;
for test in testArr:
	print(test)
	rcompile = re.compile(regex);
	data = rcompile.findall(test);
	if(data is not None):
		print('solution %s' % data);
	#for aha in data:
	#	print('solution %s' % aha);
	#print(solutionArr[i]);
	i = i + 1;