import PyPluMA

class CSVCoarseFinePlugin:
    def input(self, infile):
        #####################################################################
        # More than one input
        # Inputfile becomes tab-delimited keyword-value pairs
        paramfile = open(infile, 'r')
        self.parameters = dict()
        for line in paramfile:
            contents = line.strip().split('\t')
            self.parameters[contents[0]] = contents[1]
        
        self.csvfile = PyPluMA.prefix()+"/"+self.parameters["csvfile"]
        self.doboth = self.parameters["doboth"]
        #####################################################################


    def run(self):
        myfile = open(self.csvfile, 'r')
        # First line of file
        self.firstline = myfile.readline()

        # Dictionary to hold groups
        self.coarsegroups = dict()
        self.finegroups = dict()
       
        # Read file and sum groups
        for line in myfile:
            line = line.strip()
            firstcomma = line.find(',')
            secondcomma = line.find(',', firstcomma+1)
            coarse = line[:firstcomma]
            fine = line[firstcomma+1:secondcomma]
            ###############################################################################################
            # ADDED
            if (coarse not in self.coarsegroups):
               self.coarsegroups[coarse] = [float(x) for x in line[secondcomma+1:].split(',')]
            else:
                self.coarsegroups[coarse] += [float(x) for x in line[secondcomma+1:].split(',')]
            ###############################################################################################
            if (coarse not in self.finegroups):
               self.finegroups[coarse] = dict()
            if (fine not in self.finegroups[coarse]):
               self.finegroups[coarse][fine] = [float(x) for x in line[secondcomma+1:].split(',')]
            else:
                self.finegroups[coarse][fine] += [float(x) for x in line[secondcomma+1:].split(',')]
               

    def output(self, outputfile):
       ########################################################################
       # We now have a prefix
       if (self.doboth == "True"):
          coarsefile = open(outputfile+".coarse.csv", 'w')
       finefile = open(outputfile+".fine.csv", 'w')
       ########################################################################
 
       ###################################################################################
       # Coarse file cannot have fine data in header
       if (self.doboth == "True"):
           firstcomma = self.firstline.find(',')
           secondcomma = self.firstline.find(',', firstcomma+1)
           coarsefile.write(self.firstline[:firstcomma]+self.firstline[secondcomma:])
       ###################################################################################

       # Write first line
       finefile.write(self.firstline)

       # Write coarsefine sums
       for coarse in self.finegroups:
           ####################################################################
           # For doing both
           if (self.doboth == "True"):
               mylist = str(self.coarsegroups[coarse])
               mylist = mylist[1:len(mylist)-1]
               coarsefile.write(coarse+","+mylist+"\n")
           ####################################################################
           for fine in self.finegroups[coarse]:
               mylist = str(self.finegroups[coarse][fine])
               mylist = mylist[1:len(mylist)-1]
               finefile.write(coarse+","+fine+","+mylist+"\n")


