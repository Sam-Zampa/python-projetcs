"""
Basic DNA analysis project

-Check the sequence
-Counts nucleotide frequence
-Shows complementary band of DNA

---
code made in March 2024
"""

class DNA:
    def __init__(self, seq=''):
        self.nucleotides = ('A', 'T', 'C', 'G')
        self.seq = seq
    
    # 1
    def addDNASample(self, seq):
        self.seq = seq
    
    # 2
    def validDNASeq(self):
        tempSeq = self.seq.upper()
        for nuc in tempSeq:
            if nuc not in self.nucleotides:
                print("DNA sequence test failed\nCheck your sequence\n")
                return
        print("DNA sequence test approved\n")
            
    # 3
    def countNucFreq(self):
        tempFrequency = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for nuc in self.seq:
            tempFrequency[nuc] += 1
        print(f'{tempFrequency}\n')
    
    # 4
    def complementary(self):
        comp_map = str.maketrans('ATCG', 'TAGC')
        print(f'{self.seq.translate(comp_map)}\n')

# Main loop to interact with user
if __name__ == '__main__':
    dna = DNA()
    while True:
        print('-DNA basic analysis-')
        print('\nOptions')
        print('1 - Input your DNA sequence')
        print('2 - Check the DNA sequence')
        print('3 - Count nucleotide frequency')
        print('4 - Complementary sequence')
        print('5 - Exit')

        option = input('\nChoose an option: \n')

        if option == '1':
            DNASample = input('Input your DNA sequence: \n')
            dna.addDNASample(DNASample)  
        elif option == '2':
            dna.validDNASeq()
        elif option == '3':
            dna.countNucFreq()
        elif option == '4':
            dna.complementary()
        elif option == '5':
            break
        else:
            print('Choose a valid option\n')
