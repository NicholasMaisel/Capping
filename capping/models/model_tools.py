import pandas as pd
import seaborn as sns

def con_mat_to_df(con_mat, labels):
    con_mat = con_mat.tolist()
    con_mat_dict = {}
    for i in range(len(labels)):
        con_mat_dict[labels[i]] = con_mat[i]
    con_mat_df = pd.DataFrame(con_mat_dict, index = labels)
    sns.heatmap(con_mat_df, annot = True,cmap="YlGnBu")
    plt.show()
