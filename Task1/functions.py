"""
Split function

Input: 
    Text (string) - the text to split to batches
    W (int) - size of batch
Returns: 
    (list of splitted text) - list containing the batchs of the given text string
"""
def Split(Text,W):
    Text_list = list(Text.split(" ")) 
    splitted_Text= lambda list, x: [list[i:i+x] for i in range(0, len(list), x)]
    return splitted_Text(Text_list,W)

"""
Search function

Input:
    TextBatch (string) - the batch from the original Text
    Pattern (string) - the pattern by which 
Output:
    (int) - the number of occuerence in a batch 
"""
def Search(TextBatch, Pattern):
    return sum(Pattern in s for s in TextBatch)

"""
Addition function

Input:
    BatchOccurence (int) - number of pattern occurence in batch
Output:
    (int) - total number of occuerence in a text
"""
def Addition(BatchOccurencelist):
    return sum(BatchOccurencelist)

