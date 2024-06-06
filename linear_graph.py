import matplotlib.pyplot as eng

def main():
    x_coords=([0,1,2,3,4])
    y_coords=([0,3,1,5,2])
    
    eng.plot(x_coords,y_coords,marker='o')
    
    eng.title('Sales by that year')
    
    eng.xlabel('Year')
    eng.ylabel('Sales')
    
    eng.xticks([0,1,2,3,4],
               ['2016', '2017', '2018', '2019', '2020'])
    
    eng.yticks([0,1,2,3,4,5],
               ['$0M', '$1M', '$2M', '$3M', '$4M', '$5M'])
    
    eng.grid(True)
    
    eng.show()
    
if __name__=='__main__':
    main()
