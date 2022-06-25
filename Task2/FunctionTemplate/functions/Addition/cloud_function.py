def cloud_function(json_input):
    BatchOccurencelist = json_input["BatchOccurenceArr"]
    result = sum(BatchOccurencelist)
    # return the result
    res = {
        "TotalOccurence": result
    }
    return res
