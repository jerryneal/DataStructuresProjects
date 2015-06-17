'''
    Name        :  January_OptionA.py
    Author      :  Neal Bazirake and David Logan
    Description :  Making a Graph class and menu driver for use with adjacency  
                   Graph Algorithms giving the user the option to give the number
                   of nodes, state whether directed or undirected, labeled or unlabeled.
'''

from collections import defaultdict
import numpy as np

class GraphClass:
    def _init_(self):
        self.num_of_nodes = None
        self.direction = None
        self.labelling = None
        self.node = None
        self.nd_edge = None
        self.edge_label = None
        self.nodes = []

    def input_textfile(self,filename):
        
        f = open(filename,'r')
        self.num_of_nodes = f.readline()
        self.direction = f.readline()
        self.labelling = f.readline()
        self.nodes = []
        for i in range(int(self.num_of_nodes)):
                dt = f.readline()
                n = dt.split()
                self.node = int(n[0])
                self.nd_edge = int(n[1])
                self.edge_label = int(n[2]) 
                self.nodes.append([self.node,self.nd_edge,self.edge_label])
                
        return self.nodes

        
    def input_keyboard(self):
        self.num_of_nodes = eval(input("Enter the number of nodes: "))
        self.direction = input("Enter U or D indicating undirected or directed: ")
        self.labelling = input("U or L indicating labeled or unlabeled: ")
        self.nodes = []
        for num in range(0,self.num_of_nodes):
            entered_pts = input("Enter Node, Add Edge,Edge Label seperated by a comma: ")
            self.nodes.append([entered_pts])

        return self.nodes
      
    def graph_list(self):

        graph_list = defaultdict(lambda: defaultdict(lambda: 0))
        for i in self.nodes:
            graph_list[i[0],i[1]] = i[2]
        print("Result from list: \n:", graph_list)
        
    def graph_matrix(self):

        n = max(max(node,edge) for node,edge,label in self.nodes)
        graph_matrice = [[0]*n for i in range(n)]
        for node,edge,label in self.nodes:
            graph_matrice[node-1][edge-1] = label
        graph_matrice = graph_matrice[::-1]
        print("Result from graph matrix\n")
        for row in graph_matrice:
            print(row)
        
    def user_menu_options(self):
        print("---###---- Welcome to the Graph Menu Class----####---\n")
        print(" 1: Read a graph from a text file")
        print(" 2: Read a graph from the keyboard, appropriate prompts will")
        print("    be direct the user\n")
        

    def output_options(self):
        print("\nHow would you want your points to be displayed?\n")
        print(" 3: Display the adjacency list")
        print(" 4: Display the adjacency matrix")
        
def main():
    GC = GraphClass()
    GC.user_menu_options()
    user_input = eval(input("Enter a number from the above options: " ))
    '''
    Below are the input options
    '''
    
    #Using the keyboard option                                                    
    if user_input != 1:
        GC.input_keyboard()
        
    #Using the textfile option    
    else:
        print("Two textfiles are stored in memory.")
        print("1. Cities2014.txt")
        print("2. Eurocities.txt")
        text_file = eval(input("Which file would you want to use? "))

        if text_file == 1:
            textfile = 'cities2014.txt'
        else:
            textfile = 'eeurcities.txt'
            
        GC.input_textfile(textfile)
        
    '''
    Below are the output options
    '''
    
    if user_input is not 1:
        GC.output_options()
    else:
        GC.output_options()
        output_option = eval(input("Enter one of the above options: "))
        
    #Using the Graph Matrix
    if output_option != 4:
        GC.graph_list()
       
    #Using the textfile Option    
    else:
         GC.graph_matrix()
        
if __name__ == "__main__":
	GraphClass()
	main()
