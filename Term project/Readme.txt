Steps to run the Benchmarks on BFT-SMaRt

step-1 : 
	Install the latest Java Runtime Environment. Make sure the environment variables are set properly
	
step-2 :
	Git clone the BFT-SMaRt repo

step- 3 : 
	Build the gradle which we get in prior with the library to set up the library and make it ready to use.
	Command : ./gradlew build
	Make sure that the build is succesful

step -4 : 
	Running the benchmark server
	make sure you are in the root directory of the project. 
	ServerCommand : runscripts/smartrun.sh bftsmart.demo.microbenchmarks.ThroughputLatencyServer request/reply-size 
				<processId> <measurement interval> <reply size> <state size> <context?> <nosig | default | ecdsa> [rwd | rw]
	Default Parameters : all booleans are set false. All choices are set to Default
	
	Running the benchmark client
	make sure you are in the root directory of the project. 
	ClientCommand : runscripts/smartrun.sh bftsmart.demo.microbenchmarks.ThroughputLatencyClient <initial client id> 
	<number of clients> <number of operations> <request size> <interval (ms)> <read only?> <verbose?> <nosig | default | ecdsa>
	Default Parameters : all booleans are set false. All choices are set to Default

Step - 5 : 
	Run 4 instances of ServerCommand with 4 different Id's to start 4 servers. Tune reply size based on the requirement. Servers will log the throughput of the system after every 
	<measurement interval> seconds. Note them down to plot the graph
	
Step - 6 :
	After running sufficient number of servers for with CFT or BFT mode, only then start the client . ClientCommand starts <number of clients> clients with <number of operations> operations and <request size>
	with a gap between each operation of <interval (ms)>. After the operations from all forked clients done sending the operations, the latency numbers are displayed. 

Step - 7 :
	Collect the throughput  and Latency numbers and save them in a excel file.

Step - 8 :
	Give the path to excel file to Evaluate.py file and run the Definition corresponding to experiment. 

Step - 9 :
	The Graphs are Displayed.