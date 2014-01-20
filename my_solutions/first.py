import survey

def Mean(t):
    '''
    computes the mean of a sequence of numbers
    Args:
      t: sequence of numbers
    Returns: float
    '''
    return float(sum(t)) / len(t)

def PartitionRecords(table):
    '''
    Divides records into two lists: first babies and others
    Args: 
      table: pregnancyTable from survey
    '''
    firsts = survey.Pregnancies()
    others = survey.Pregnancies()
    
    for pregnancy in table.records:
        # skip over none-live births
        if pregnancy.outcome != 1:
            continue
        if pregnancy.birthord == 1:
            firsts.AddRecord(pregnancy)
        else: 
            others.AddRecord(pregnancy)
    return firsts, others

def Process(table):
    '''
    Runs analysis on given table
    Args:
      table: table object
    '''            
    table.lengths = [p.prglength for p in table.records]
    table.n = len(table.lengths)
    table.mu = Mean(table.lengths)

def MakeTables(data_dir='.'):
    '''Reads survey data and returns tables for first babies and others
    '''
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    firsts, others = PartitionRecords(table)
    return table, firsts, others

def ProcessTables(*tables):
    '''processes a list of tables
    Args: 
      tables: gathered argument tuple of tables
    '''
    for table in tables:
        Process(table)

def Summarize(data_dir):
    '''Prints summary stats for first babies and others
    Returns: 
      tuple of Tables
    '''
    table, firsts, others = MakeTables(data_dir)
    ProcessTables(firsts, others)
    
    print 'Number of first babies', firsts.n
    print 'Number of others', others.n
    
    mu1, mu2 = firsts.mu, others.mu
    
    print 'mean gestation in weeks:'
    print '    First babies:', mu1
    print '    Other babies:', mu2
    
    print 'Difference in days', (mu1 - mu2) * 7.0

def main(name, data_dir='.'):
    Summarize(data_dir)

if __name__ == '__main__':
    import sys
    main(*sys.argv) 