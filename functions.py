import locale
import numpy as np
import matplotlib.pyplot as plt

def get_binary_column(dfName, colName, qual_for_false):
    """
    Iterate through a column to append an additional binary (T/F) column to a DataFrame
    
    dfName = Name of Pandas DataFrame to pull information from
    colName = Name of column from DataFrame to pull information from
    qual_for_false = condition where value is <= qual_for_false returns a binary 0, else 1
    """
    newCol = []
    for val in dfName[colName]:
        if val <= qual_for_false:
            newCol.append('0')
        else:
            newCol.append('1')
    return newCol

def get_means(values, dfName, colName):
    mean_list = []
    for val in values:
        this_df = dfName.loc[dfName[colName]==val]
        mean_price = np.mean(this_df['price'])
        price_change_per_val = mean_price/len(this_df[colName])
        mean_list.append(price_change_per_val)
    return (mean_list)

def get_mean_diff(values, dfName, colName):
    list = get_means(values, dfName, colName)
    sum_list = sum(list)
    av_mean = round(sum_list/len(list), 2)
    print(av_mean)
    return

#PLOTTING Simple Linear Regression

def calc_slope(xs,ys):
    m = (((np.mean(xs)*np.mean(ys)) - np.mean(xs*ys)) /
         ((np.mean(xs)**2) - np.mean(xs*xs)))
    
    return m

def best_fit(xs,ys):
    m = calc_slope(xs,ys)
    c = np.mean(ys) - m*np.mean(xs)
    
    return m, c

def reg_line (m, c, xs):
    
    return [(m*x)+c for x in xs]

def plot_scatter_lin_reg(X, Y, regression_line, colName, Ycol):
    plt.scatter(X,Y,color='#003F72', label="Data points")
    plt.plot(X, regression_line, label= "Regression Line")
    plt.title(colName + ' vs. ' + Ycol)
    plt.ylabel(Ycol)
    plt.xlabel(colName)
    plt.legend()
    plt.show()
    return

def get_sim_lin_reg(dfName, Ycol, subset):
    for col in subset:
        X, Y = dfName[col], dfName[Ycol]
        m, c = best_fit(X, Y)
        regression_line = reg_line(m, c, X)
        plot_scatter_lin_reg(X, Y, regression_line, col, Ycol)
    return   

