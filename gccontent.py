
def getGCSlidingWindow(sequence, window_size):
    '''Calculates %GC in sequence of sliding window window_size'''
    return map(lambda x: (x.count("G")+x.count("C")) / float(window_size), 
               map(lambda r: sequence[r:r+window_size], 
                   range(len(sequence)-window_size+1)))
