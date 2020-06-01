import locale

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