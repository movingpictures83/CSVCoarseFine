class CSVCoarseFinePlugin:
    def input(self, infile):
        myfile = open(infile, 'r')
        
        # First line of file
        self.firstline = myfile.readline()

        # Dictionary to hold groups
        self.groups = dict()
       
        # Read file and sum groups
        for line in myfile:
            line = line.strip()
            firstcomma = line.find(',')
            secondcomma = line.find(',', firstcomma+1)
            coarse = line[:firstcomma]
            fine = line[firstcomma+1:secondcomma]
            if (coarse not in self.groups):
               self.groups[coarse] = dict()
            if (fine not in self.groups[coarse]):
               self.groups[coarse][fine] = [float(x) for x in line[secondcomma+1:].split(',')]
            else:
                self.groups[coarse][fine] += [float(x) for x in line[secondcomma+1:].split(',')]
               
    def run(self):
         pass

    def output(self, outputfile):
       outfile = open(outputfile, 'w')

       # Write first line
       outfile.write(self.firstline)

       # Write group sums
       for coarse in self.groups:
           for fine in self.groups[coarse]:
               mylist = str(self.groups[coarse][fine])
               mylist = mylist[1:len(mylist)-1]
               outfile.write(coarse+","+fine+","+mylist+"\n")


