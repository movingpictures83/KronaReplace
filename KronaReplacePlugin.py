import sys
import PyPluMA

class KronaReplacePlugin:
    def input(self, filename):
        infile = open(filename, 'r')
        self.parameters = dict()
        for line in infile:
            line = line.strip()
            contents = line.split('\t')
            self.parameters[contents[0]] = contents[1]

        self.kronafile = open(PyPluMA.prefix()+"/"+self.parameters["kronafile"], 'r')
        mapping = open(PyPluMA.prefix()+"/"+self.parameters["mapfile"], 'r')

        self.mymap = dict()
        for line in mapping:
           contents = line.strip().split(',')
           contents[0] = contents[0][1:len(contents[0])-1]
           contents[1] = contents[1][1:len(contents[1])-1]
           self.mymap[contents[0]] = contents[1]

    def run(self):
        pass

    def output(self, filename):
      lines = []
      for line in self.kronafile:
           contents = line.strip().split('\t')
           newcontents = []
           newline = ""
           for i in range(0, len(contents)):
               if (contents[i] in self.mymap):
                   newcontents.append(self.mymap[contents[i]])
               else:
                   newcontents.append(contents[i])
           for i in range(0, len(newcontents)):
               newline += newcontents[i]
               if (i == len(newcontents)-1):
                   newline += "\n"
               else:
                   newline += "\t"
           lines.append(newline)
      outfile = open(filename, 'w')
      for line in lines:
            outfile.write(line)

