def cloud_function(json_input):
    TextBatch = json_input["TextBatch"]
    Pattern = json_input["Pattern"]
    result =  sum(Pattern in s for s in TextBatch)
    # return the result
    res = {
        "BatchOccurence": result
    }
    return res
