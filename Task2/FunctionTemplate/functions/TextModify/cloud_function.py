def cloud_function(json_input):
    OriginTextStr = json_input["OriginTextStr"]
    Mnum = json_input["Mnum"]
    Text_list = list(OriginTextStr.split(" "))
    TextfirstMnum = Text_list[0:Mnum]
    result = " ".join(TextfirstMnum)
    # return the result
    res = {
        "TotalOccurence": result
    }
    return res
