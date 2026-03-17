import pandas as pd
import matplotlib.pyplot as plt

def generate_plots():
    
    # i am loading data from csv files
    df_dij_2d = pd.read_csv('dijkstra_2d_array.csv')
    df_dij_ll = pd.read_csv('dijkstra_ll.csv')
    df_floyd_2d = pd.read_csv('floyd_2d_array.csv')
    df_floyd_ll = pd.read_csv('floyd_ll.csv')

    #  Dijkstra's Algorithm Comparison
    plt.figure(figsize=(10, 6))
    
    plt.plot(df_dij_2d['file_id'], df_dij_2d['time'], marker='o', color='blue', linewidth=2, label='2D Array')
    plt.plot(df_dij_ll['file_id'], df_dij_ll['time'], marker='s', color='red', linewidth=2, label='Linked List')
    
    plt.title("Time Performance of Dijkstra's Algorithm", fontsize=14, fontweight='bold')
    plt.xlabel("Input File Index", fontsize=12)
    plt.ylabel("Total Time (in seconds)", fontsize=12)
    plt.xticks(range(1, 16))
    plt.legend(fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('Plot_Dijkstra_Time_Performance.png', dpi=300)
    plt.show()

    # Floyd Algorithm Comparison
    plt.figure(figsize=(10, 6))
    
    plt.plot(df_floyd_2d['file_id'], df_floyd_2d['time'], marker='o', color='blue', linewidth=2, label='2D Array')
    plt.plot(df_floyd_ll['file_id'], df_floyd_ll['time'], marker='s', color='red', linewidth=2, label='Linked List')
    
    plt.title("Time Performance of Floyd Algorithm", fontsize=14, fontweight='bold')
    plt.xlabel("Input File Index", fontsize=12)
    plt.ylabel("Total Time (in seconds)", fontsize=12)
    plt.xticks(range(1, 16))
    plt.legend(fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('Plot_Floyd_Time_Performance.png', dpi=300)
    plt.show()

    print("Yes, plots are generated")

if __name__ == "__main__":
    generate_plots()